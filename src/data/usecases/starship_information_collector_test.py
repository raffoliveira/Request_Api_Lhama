from src.data.usecases.starship_information_collector import StarshipInformationCollector
from src.infra.test.swap_api_consumer import SwapiApiConsumerSpy


def test_find_starship():
    """ Testing find_starship method """

    api_consumer = SwapiApiConsumerSpy()
    starship_information_colector = StarshipInformationCollector(api_consumer)

    starship_id = 9
    time = 4

    response = starship_information_colector.find_starship(starship_id, time)

    assert api_consumer.get_starship_information_attributes["starship_id"] == starship_id
    assert isinstance(response, dict)
    assert "MGLT" in response
    assert "distance_traveled" in response
