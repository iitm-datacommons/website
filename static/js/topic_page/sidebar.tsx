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
import _ from "lodash";
import React from "react";

import { randDomId } from "../shared/util";
import { getRelLink } from "./string_utils";
import { CategoryConfig } from "./topic_config";

interface SidebarPropsType {
  /**
   * Categories from the page config.
   */
  categories: CategoryConfig[];
}

export function Sidebar(props: SidebarPropsType): JSX.Element {
  return (
    <ul id="nav-topics" className="nav flex-column accordion">
      {!_.isEmpty(props.categories) &&
        props.categories.map((category) => {
          // Add the category
          const elements = [renderItem(category.title, true)];
          // Add all child blocks
          category.blocks.forEach((block) => {
            if (block.title) {
              elements.push(renderItem(block.title, false));
            }
          });
          return elements;
        })}
    </ul>
  );
}

function renderItem(title: string, isCategory: boolean): JSX.Element {
  return (
    <li
      key={randDomId()}
      className={`nav-item ${isCategory ? "category" : ""}`}
    >
      <a href={`#${getRelLink(title)}`}>{title}</a>
    </li>
  );
}
