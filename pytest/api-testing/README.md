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
    1. Using mocks, specifically `pytest-mock`
        ```bash
        export API_KEY=changeme;
        
        alias t1=pytest tests -k "test_retrieve_weather_using_mocks";

        t1
        ```

    2. Using `responses` which intercepts `requests` calls and patches them avoiding the length set up.
        ```bash
        export API_KEY=changeme;
        
        alias t2=pytest tests -k "test_retrieve_weather_using_responses";

        t2
        ```

    3. Using [dependency injection](https://stackoverflow.com/a/140655) to inject a fake adapter during test time. 
    
    This way the behaviour doesn't change if we decide to change the implementation because all we've done is change the adapters (from one that uses `responses` to one that uses `urllib` for example)

        ```bash
        export API_KEY=changeme;
        
        alias t3=pytest tests -k "test_retrieve_weather_using_adapter";

        t3
        ```


## Resources

- https://opensource.com/article/21/9/unit-test-python