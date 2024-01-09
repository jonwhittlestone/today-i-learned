# api-testing

This repo outlines a few techniques for unit testing external APIs with pytest.


### Prerequisites

* poetry
* [an API key for OpenWeather](https://openweathermap.org/api)

## Installation

```bash
git clone https://github.com/jonwhittlestone/today-i-learned.git

cd pytest/api-testing

poetry install
```

## Usage

- In the virtualenv, add API key as env var and run the Flask-based implementation
    ```bash
    poetry shell;

    export API_KEY=changeme;

    python3 api_testing/__init__.py
    ```
    visit http://127.0.0.0.1:8000

- Run tests
    1. Using mocks
        ```bash
        export API_KEY=changeme;
        
        alias t1=pytest tests -k "test_retrieve_weather_using_mocks";

        t1
        ```


## Resources

- https://opensource.com/article/21/9/unit-test-python