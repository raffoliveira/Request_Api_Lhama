from src.errors import HttpRequestError
from .swap_api_consumer import SwapiApiConsumer


def test_get_starships(requests_mock):
    """Testing get_starships"""

    swapi_api_consumer = SwapiApiConsumer()
    page = 1

    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some': 'thing', "results": [{}]})
    get_starships_response = swapi_api_consumer.get_starships(page=page)

    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_starships_response.request.params == {"page": page}

    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response["results"], list)


def test_get_starships_http_error(requests_mock):
    ''' Testing error in get_starships method '''

    swapi_api = SwapiApiConsumer()
    page = 100

    requests_mock.get('https://swapi.dev/api/starships/', status_code=404, json={'detail': 'something'})

    try:
        _ = swapi_api.get_starships(page=page)
        assert True is False
    except HttpRequestError as err:
        assert err.message is not None
        assert err.status_code is not None
