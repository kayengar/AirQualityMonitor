#!/usr/bin/env python
"""
The entry point for Air Quality Monitor
"""
from os import environ
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# from twilio_helper import send_message

AQI_THRESHOLD = float(environ.get("AQI_THRESHOLD"))
LIST_OF_STATES = environ.get("LIST_OF_STATES").split(",")


def initialize_headless_chrome():
    """
    Initializes a headless chrome window of size 1920 x 1200
    :return:
    """
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


def scrape_data_from_website(
    chrome_driver,
    url: str,
    state: str,
    list_of_cities_aqi: list,
) -> None:
    """

    :param chrome_driver: The WebDriver for chrome
    :param state: the state for which aqi should be scraped
    :param list_of_cities_aqi: the cities' aqi of a given
    state populated as a list
    :param url: The base url of aqi website
    :return:
    """
    chrome_driver.get(url)
    state_html_doc = chrome_driver.page_source
    soup = BeautifulSoup(state_html_doc, "html.parser")
    current_aqi_table = soup.find(id="currentAQI")
    all_table_rows = current_aqi_table.find_all("tr")
    for table_row in all_table_rows:
        city = pollutant_type = pollutant_value = None
        if table_row.contents:
            for table_data_cell in table_row.contents:
                if "state-city-cell-link" in str(table_data_cell):
                    city = table_data_cell.contents[0].text
                if "currentAirQualityColumn" in str(table_data_cell):
                    if "PM2.5" in table_data_cell.text:
                        pollutant_type = "PM2.5"
                        pollutant_value = int(
                            table_data_cell.contents[0].contents[0].text
                        )
                    elif "PM10" in table_data_cell.text:
                        pollutant_type = "PM10"
                        pollutant_value = int(
                            table_data_cell.contents[0].contents[0].text
                        )
                    elif "O3" in table_data_cell.text:
                        pollutant_type = "OZONE"
                        pollutant_value = int(
                            table_data_cell.contents[0].contents[0].text
                        )
        if city and pollutant_type and pollutant_value:
            aqi_dict = {
                "State": state.capitalize(),
                "City": city,
                "PollutantType": pollutant_type,
                "AQI": pollutant_value,
            }
            list_of_cities_aqi.append(aqi_dict)


def populate_data_for_list_of_states(list_of_states: list) -> list:
    """
    This function opens airnow website for the given state in the
    list of states and scrapes data form the list of
    rows in the table with id currentAQI
    :param list_of_states:
    :return: list of cities in the given state with given AQI
    """
    list_of_cities_aqi: list = []
    chrome_driver = initialize_headless_chrome()
    for state in list_of_states:
        state_url = f"https://www.airnow.gov/state/?name={state}"
        scrape_data_from_website(chrome_driver, state_url, state, list_of_cities_aqi)
    chrome_driver.quit()
    return list_of_cities_aqi


def air_quality_monitor(aqi_threshold: float, list_of_states: list) -> list:
    """
    The entry point that returns a filtered list of relevant
    :param aqi_threshold:
    :param list_of_states:
    :return:
    """
    filtered_list_of_cities_aqi = list()
    list_of_cities_aqi = populate_data_for_list_of_states(list_of_states)
    for aqi_data in list_of_cities_aqi:
        if aqi_data["AQI"] > aqi_threshold:
            filtered_list_of_cities_aqi.append(aqi_data)
    return filtered_list_of_cities_aqi


def pretty_print_json(list_of_aqi_data: list) -> str:
    """
    Format the list of dict into a YAML like format for better readability
    in the SMS
    """
    messages = "\n"
    for index, aqi_item in enumerate(list_of_aqi_data, start=1):
        message = (
            f"\n{index}. State: {aqi_item['State']}\n"
            f"   City: {aqi_item['City']}\n"
            f"   Pollutant: {aqi_item['PollutantType']}\n"
            f"   AQI: {aqi_item['AQI']}\n"
        )
        messages += message

    return messages


if __name__ == "__main__":
    # """
    # The entry point that calls air_quality monitor and sends message
    # """
    list_of_cities = air_quality_monitor(AQI_THRESHOLD, LIST_OF_STATES)
    if list_of_cities:
        pretty_string = pretty_print_json(list_of_cities)
        print(pretty_string)
        # send_message(pretty_string)
        # This currently doesn't send emails
        # send_email(pretty_string)
