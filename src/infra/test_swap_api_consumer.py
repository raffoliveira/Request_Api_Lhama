from .swap_api_consumer import SwapiApiConsumer


def test_get_starships():
    """Testing get_starships"""

    swapi_api = SwapiApiConsumer()
    page = 1
    response = swapi_api.get_startships(page=page)

    assert response.request.method == 'GET'
    assert response.request.url == 'https://swapi.dev/api/starships'
    assert response.request.params == {"page": page}
    assert response.status_code == 200
    assert isinstance(response.response["results"], list)
