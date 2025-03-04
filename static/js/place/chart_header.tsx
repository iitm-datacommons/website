/**
 * Copyright 2021 Google LLC
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

import React from "react";

import { intl, LocalizedLink } from "../i18n/i18n";

interface ChartHeaderPropType {
  /**
   * The header text.
   */
  text: string;
  /**
   * The place dcid.
   */
  place: string;
  /**
   * The place name.
   */
  isOverview: boolean;
  /**
   * Translated strings for categories.
   */
  categoryStrings: { string: string };
}

export class ChartHeader extends React.Component<ChartHeaderPropType> {
  constructor(props: ChartHeaderPropType) {
    super(props);
  }
  render(): JSX.Element {
    if (this.props.isOverview) {
      return (
        <h2 id={this.props.text}>
          <LocalizedLink
            href={`/place/${this.props.place}?category=${this.props.text}`}
            text={this.props.categoryStrings[this.props.text]}
          />
          <span className="more">
            <LocalizedLink
              href={`/place/${this.props.place}?category=${this.props.text}`}
              text={
                intl.formatMessage({
                  id: "more_charts",
                  defaultMessage: "More charts",
                  description:
                    "Link to explore more charts about a particular domain, such as Education or Health.",
                }) + " ›"
              }
            />
          </span>
        </h2>
      );
    }
    return <h3 id={this.props.text.replace(/ /g, "-")}>{this.props.text}</h3>;
  }
}
