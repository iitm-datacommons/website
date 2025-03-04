# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import urllib.request

from webdriver_tests.base_test import WebdriverBaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

MTV_URL = '/place/geoId/0649670'
USA_URL = '/place/country/USA'
CA_URL = '/place/geoId/06'
PLACE_SEARCH = 'California, USA'


class TestPlaceExplorer(WebdriverBaseTest):
    """Class to test place explorer tool."""

    def test_page_serve_usa(self):
        """Test the place explorer page for USA can be loaded successfullly."""
        TITLE_TEXT = "United States of America - Place Explorer - Data Commons"
        PLACE_TYPE_TEXT = "Country in North America"

        # Load USA page.
        self.driver.get(self.url_ + USA_URL)

        # Wait until the place-type is correct.
        element_present = EC.text_to_be_present_in_element(
            (By.ID, 'place-type'), PLACE_TYPE_TEXT)
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(element_present)

        # Assert 200 HTTP code: successful page load.
        req = urllib.request.Request(self.driver.current_url)
        with urllib.request.urlopen(req) as response:
            self.assertEqual(response.getcode(), 200)

        # Assert 200 HTTP code: successful JS generation.
        req = urllib.request.Request(self.url_ + "/place.js")
        with urllib.request.urlopen(req) as response:
            self.assertEqual(response.getcode(), 200)

        # Wait until the page loads and the title is correct.
        WebDriverWait(self.driver,
                      self.TIMEOUT_SEC).until(EC.title_contains(TITLE_TEXT))
        self.assertEqual(TITLE_TEXT, self.driver.title)

        # Assert place title is correct.
        title = self.driver.find_element_by_id("place-name")
        self.assertEqual("United States of America", title.text)

        # Assert place type is correct.
        subtitle = self.driver.find_element_by_id("place-type")
        self.assertEqual("Country in North America", subtitle.text)

    def test_page_serve_mtv(self):
        """Test the place explorer page for MTV can be loaded successfullly."""
        PLACE_TYPE_TITLE = "City in Santa Clara County, California, United States of America, North America"
        TITLE_TEXT = "Mountain View - Place Explorer - Data Commons"

        # Load Mountain View Page.
        self.driver.get(self.url_ + MTV_URL)

        # Wait until the page loads and the title is correct.
        WebDriverWait(self.driver,
                      self.TIMEOUT_SEC).until(EC.title_contains(TITLE_TEXT))

        # Assert title is correct.
        self.assertEqual(TITLE_TEXT, self.driver.title)

        # Wait until the place name has loaded.
        element_present = EC.text_to_be_present_in_element(
            (By.ID, 'place-name'), "Mountain View")
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(element_present)
        place_name = self.driver.find_element_by_id("place-name").text

        # Assert place name is correct.
        self.assertEqual("Mountain View", place_name)

        # Wait until the place type has loaded.
        element_present = EC.text_to_be_present_in_element(
            (By.ID, 'place-type'), PLACE_TYPE_TITLE)
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(element_present)

        # Assert place type is correct.
        place_type = self.driver.find_element_by_id("place-type").text
        self.assertEqual(PLACE_TYPE_TITLE, place_type)

    def test_place_search(self):
        """Test the place search box can work correctly."""
        CALIFORNIA_TITLE = "California - Place Explorer - Data Commons"
        # Load USA page.
        self.driver.get(self.url_ + USA_URL)

        # Wait until the place name has loaded.
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, 'pac-target-input'))
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(element_present)

        search_box = self.driver.find_element_by_class_name("pac-target-input")

        search_box.send_keys(PLACE_SEARCH)

        # Wait until the place name has loaded.
        element_present = EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.pac-item:nth-child(1)'))
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(element_present)

        # Select the first result from the list and click on it.
        first_result = self.driver.find_element_by_css_selector(
            '.pac-item:nth-child(1)')
        first_result.click()

        # Wait until the page loads and the title is correct.
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(
            EC.title_contains(CALIFORNIA_TITLE))

        # Assert page title is correct.
        self.assertEqual(CALIFORNIA_TITLE, self.driver.title)

    def test_demographics_link(self):
        """
        Test the demographics link can work correctly.
        """
        CHART_TITLE = "Median age by gender: states near California(2020)"
        # Load California page.
        self.driver.get(self.url_ + CA_URL)

        # Wait until the Demographics link is present.
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="Demographics"]/a'))
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(element_present)

        # Find and click on the Demographics URL.
        demographics = self.driver.find_element_by_xpath(
            '//*[@id="Demographics"]/a')
        demographics.click()

        # Wait until the new page has loaded.
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main-pane"]/section[4]/div/div[2]/div/h4'))
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(element_present)

        # Assert that Demographics is part of the new url.
        self.assertTrue("Demographics" in self.driver.current_url)

        # Get the chart_title text.
        chart_title = self.driver.find_element_by_xpath(
            '//*[@id="main-pane"]/section[4]/div/div[2]/div/h4').text

        # Assert chart title is correct.
        self.assertEqual(CHART_TITLE, chart_title)

    def test_demographics_redirect_link(self):
        """
        Test a place page with demographics after a redirect.
        """
        # Load California's Demographics page.
        start_url = self.url_ + '/place?dcid=geoId/06&category=Demographics&utm_medium=um'
        self.driver.get(start_url)

        # Wait for redirect.
        WebDriverWait(self.driver, self.TIMEOUT_SEC).until(
            lambda driver: driver.current_url != start_url)
        self.assertTrue("category=Demographics" in self.driver.current_url)
        self.assertTrue("utm_medium=um" in self.driver.current_url)

        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main-pane"]/section[4]/div/div[2]/div/h4'))
        WebDriverWait(self.driver, self.TIMEOUT_SEC * 2).until(element_present)

        chart_title = self.driver.find_element_by_xpath(
            '//*[@id="main-pane"]/section[4]/div/div[2]/div/h4').text

        # Assert chart title is correct.
        self.assertEqual("Median age by gender: states near California(2020)",
                         chart_title)
