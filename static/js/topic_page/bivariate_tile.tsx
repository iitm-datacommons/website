/**
 * Copyright 2022 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Component for rendering a bivariate type tile.
 */

import axios from "axios";
import _ from "lodash";
import React, { useEffect, useRef, useState } from "react";
import ReactDOMServer from "react-dom/server";

import { BivariateProperties, drawBivariate } from "../chart/draw_bivariate";
import { Point } from "../chart/draw_scatter";
import { GeoJsonData } from "../chart/types";
import { USA_PLACE_DCID } from "../shared/constants";
import { GetStatSetResponse, StatApiResponse } from "../shared/stat_types";
import { NamedPlace, NamedTypedPlace } from "../shared/types";
import { getStatsWithinPlace } from "../tools/scatter/util";
import { isChildPlaceOf, shouldShowMapBoundaries } from "../tools/shared_util";
import { StatVarMetadata } from "../types/stat_var";
import { getStringOrNA } from "../utils/number_utils";
import { getPlaceScatterData } from "../utils/scatter_data_utils";
import { ChartTileContainer } from "./chart_tile";
import { CHART_HEIGHT } from "./constants";
import { getStatVarName, ReplacementStrings } from "./string_utils";

interface BivariateTilePropType {
  id: string;
  title: string;
  place: NamedTypedPlace;
  enclosedPlaceType: string;
  statVarMetadata: StatVarMetadata[];
}

interface RawData {
  geoJson: GeoJsonData;
  placeStats: GetStatSetResponse;
  population: StatApiResponse;
  placeNames: { [placeDcid: string]: string };
  parentPlaces: NamedTypedPlace[];
}

interface BivariateChartData {
  xStatVar: StatVarMetadata;
  yStatVar: StatVarMetadata;
  points: { [placeDcid: string]: Point };
  geoJson: GeoJsonData;
  sources: Set<string>;
  isUsaPlace: boolean;
  showMapBoundaries: boolean;
}

export function BivariateTile(props: BivariateTilePropType): JSX.Element {
  const svgContainer = useRef(null);
  const legend = useRef(null);
  const [rawData, setRawData] = useState<RawData | undefined>(null);
  const [bivariateChartData, setBivariateChartData] = useState<
    BivariateChartData | undefined
  >(null);

  useEffect(() => {
    fetchData(
      props.place.dcid,
      props.enclosedPlaceType,
      props.statVarMetadata,
      setRawData
    );
  }, [props]);

  useEffect(() => {
    if (rawData) {
      processData(
        rawData,
        props.statVarMetadata,
        props.place,
        props.enclosedPlaceType,
        setBivariateChartData
      );
    }
  }, [props, rawData]);

  useEffect(() => {
    if (bivariateChartData) {
      draw(bivariateChartData, props, svgContainer, legend);
    }
  }, [bivariateChartData, props]);

  if (!bivariateChartData) {
    return null;
  }
  const rs: ReplacementStrings = {
    place: props.place.dcid,
    date: "",
  };
  return (
    <ChartTileContainer
      title={props.title}
      sources={bivariateChartData.sources}
      replacementStrings={rs}
      className="bivariate-chart"
    >
      <div
        id={props.id}
        className="bivariate-svg-container"
        ref={svgContainer}
      />
      <div id="bivariate-legend-container" ref={legend} />
    </ChartTileContainer>
  );
}

function getPopulationPromise(
  placeDcid: string,
  enclosedPlaceType: string,
  statVarMetadata: StatVarMetadata[]
): Promise<StatApiResponse> {
  let statVarParams = "";
  for (const sv of statVarMetadata) {
    if (sv.denom) {
      statVarParams += `&stat_vars=${sv.denom}`;
    }
  }
  if (_.isEmpty(statVarParams)) {
    return Promise.resolve({});
  } else {
    return axios
      .get(
        `/api/stats/set/series/within-place?parent_place=${placeDcid}&child_type=${enclosedPlaceType}${statVarParams}`
      )
      .then((resp) => resp.data);
  }
}

function fetchData(
  placeDcid: string,
  enclosedPlaceType: string,
  statVarMetadata: StatVarMetadata[],
  setRawData: (data: RawData) => void
): void {
  if (statVarMetadata.length < 2) {
    // TODO: add error message
    return;
  }
  const geoJsonPromise: Promise<GeoJsonData> = axios
    .get(
      `/api/choropleth/geojson?placeDcid=${placeDcid}&placeType=${enclosedPlaceType}`
    )
    .then((resp) => resp.data);
  const placeStatsPromise: Promise<GetStatSetResponse> = getStatsWithinPlace(
    placeDcid,
    enclosedPlaceType,
    [
      { statVarDcid: statVarMetadata[0].statVar },
      { statVarDcid: statVarMetadata[1].statVar },
    ]
  );
  const populationPromise: Promise<StatApiResponse> = getPopulationPromise(
    placeDcid,
    enclosedPlaceType,
    statVarMetadata
  );
  const placeNamesPromise = axios
    .get(
      `/api/place/places-in-names?dcid=${placeDcid}&placeType=${enclosedPlaceType}`
    )
    .then((resp) => resp.data);
  const parentPlacesPromise = axios
    .get(`/api/place/parent/${placeDcid}`)
    .then((resp) => resp.data);
  Promise.all([
    placeStatsPromise,
    populationPromise,
    placeNamesPromise,
    geoJsonPromise,
    parentPlacesPromise,
  ])
    .then(([placeStats, population, placeNames, geoJson, parentPlaces]) => {
      setRawData({
        geoJson,
        placeStats,
        population,
        placeNames,
        parentPlaces,
      });
    })
    .catch(() => {
      // TODO: add error message
      setRawData(null);
    });
}

function processData(
  rawData: RawData,
  statVarMetadata: StatVarMetadata[],
  place: NamedTypedPlace,
  enclosedPlaceType: string,
  setChartdata: (data: BivariateChartData) => void
): void {
  const xStatVar = statVarMetadata[0];
  const yStatVar = statVarMetadata[1];
  const xPlacePointStat = rawData.placeStats.data[xStatVar.statVar];
  const yPlacePointStat = rawData.placeStats.data[yStatVar.statVar];
  if (!xPlacePointStat || !yPlacePointStat) {
    return;
  }
  const points = {};
  const sources: Set<string> = new Set();
  for (const place in xPlacePointStat.stat) {
    const namedPlace = {
      dcid: place,
      name: rawData.placeNames[place] || place,
    };
    const placeChartData = getPlaceScatterData(
      namedPlace,
      xPlacePointStat,
      yPlacePointStat,
      rawData.population,
      rawData.placeStats.metadata,
      xStatVar.denom,
      yStatVar.denom,
      null,
      xStatVar.scaling,
      yStatVar.scaling
    );
    if (!placeChartData) {
      console.log(`BIVARIATE: No data for ${place}, skipping`);
      continue;
    }
    placeChartData.sources.forEach((source) => {
      if (!_.isEmpty(source)) {
        sources.add(source);
      }
    });
    points[place] = placeChartData.point;
  }
  setChartdata({
    xStatVar,
    yStatVar,
    points,
    sources,
    geoJson: rawData.geoJson,
    isUsaPlace: isChildPlaceOf(
      place.dcid,
      USA_PLACE_DCID,
      rawData.parentPlaces
    ),
    showMapBoundaries: shouldShowMapBoundaries(place, enclosedPlaceType),
  });
}

const getTooltipHtml = (
  points: { [placeDcid: string]: Point },
  xLabel: string,
  yLabel: string
) => (place: NamedPlace) => {
  const point = points[place.dcid];
  if (_.isEmpty(point)) {
    return (
      `<header><b>${place.name || place.dcid}</b></header>` + "Data Unavailable"
    );
  }
  const element = (
    <>
      <header>
        <b>{point.place.name || point.place.dcid}</b>
      </header>
      {xLabel} ({point.xDate}): <b>{getStringOrNA(point.xVal)}</b>
      <br />
      {yLabel} ({point.yDate}): <b>{getStringOrNA(point.yVal)}</b>
      <br />
    </>
  );
  return ReactDOMServer.renderToStaticMarkup(element);
};

function draw(
  chartData: BivariateChartData,
  props: BivariateTilePropType,
  svgContainer: React.RefObject<HTMLDivElement>,
  legend: React.RefObject<HTMLDivElement>
): void {
  const width = svgContainer.current.offsetWidth;
  const yLabel = getStatVarName(
    chartData.yStatVar.statVar,
    [chartData.yStatVar],
    !_.isEmpty(chartData.yStatVar.denom)
  );
  const xLabel = getStatVarName(
    chartData.xStatVar.statVar,
    [chartData.xStatVar],
    !_.isEmpty(chartData.xStatVar.denom)
  );
  const properties: BivariateProperties = {
    width,
    height: CHART_HEIGHT,
    xLabel,
    yLabel,
    xUnit: chartData.xStatVar.unit,
    yUnit: chartData.yStatVar.unit,
    xLog: chartData.xStatVar.log,
    yLog: chartData.yStatVar.log,
    isUsaPlace: chartData.isUsaPlace,
    showMapBoundaries: chartData.showMapBoundaries,
    placeDcid: props.place.dcid,
  };

  drawBivariate(
    props.id,
    legend,
    chartData.points,
    chartData.geoJson,
    properties,
    _.noop,
    getTooltipHtml(chartData.points, xLabel, yLabel)
  );
}
