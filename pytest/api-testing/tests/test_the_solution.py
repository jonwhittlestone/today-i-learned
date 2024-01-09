import json
from http import HTTPStatus

import pytest
from api_testing import retrieve_weather, WeatherInfo


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
