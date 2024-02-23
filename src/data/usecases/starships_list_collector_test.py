from .starships_list_collector import StarshipsListCollector
from src.infra import SwapiApiConsumer


def test_list():
    ''' testing list method '''

    api_consumer = SwapiApiConsumer()
    starships_list_colector = StarshipsListCollector(api_consumer)

    page = 1
    starships_list_colector.list(page)

    # assert api_consumer.get_starships_attributes == {"page": page}
    # assert isinstance(response, list)
    # assert "id" in response[0]
    # assert "MGLT" in response[0]
