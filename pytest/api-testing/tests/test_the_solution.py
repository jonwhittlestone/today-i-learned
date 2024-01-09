import json
from http import HTTPStatus

import pytest
import responses
from api_testing import (
    retrieve_weather,
    retrieve_weather_with_adapter,
    WeatherInfo,
    API,
    API_KEY,
)
import vcr


@pytest.fixture()
def fake_weather_info():
    """Fixture that returns a static weather data."""
    with open("tests/weather_fixture.json") as f:
        return json.load(f)


def test_retrieve_weather_using_mocks(mocker, fake_weather_info):
    """Given a city name, test that a HTML report about the weather is generated
    correctly."""
    # Creates a fake requests response object
    fake_resp = mocker.Mock()
    # Mock the json method to return the static weather data
    fake_resp.json = mocker.Mock(return_value=fake_weather_info)
    # Mock the status code
    fake_resp.status_code = HTTPStatus.OK

    mocker.patch("api_testing.requests.get", return_value=fake_resp)

    weather_info = retrieve_weather(city="London")
    assert weather_info == WeatherInfo.from_dict(fake_weather_info)


@responses.activate
def test_retrieve_weather_using_responses(fake_weather_info):
    """Given a city name, test that a HTML report about the weather is generated
    correctly."""
    api_uri = API.format(city_name="London", api_key=API_KEY)
    responses.add(responses.GET, api_uri, json=fake_weather_info, status=HTTPStatus.OK)

    weather_info = retrieve_weather(city="London")
    assert weather_info == WeatherInfo.from_dict(fake_weather_info)


@responses.activate
def test_retrieve_weather_using_adapter(
    fake_weather_info,
):
    def fake_adapter(url: str):
        return fake_weather_info

    weather_info = retrieve_weather_with_adapter(city="London", adapter=fake_adapter)
    assert weather_info == WeatherInfo.from_dict(fake_weather_info)


@pytest.mark.vcr()
def test_retrieve_weather_using_vcr(fake_weather_info):
    weather_info = retrieve_weather(city="London")
    assert weather_info == WeatherInfo.from_dict(fake_weather_info)
