from typing import Any
from collections import namedtuple
from faker import Faker

fake = Faker()
GetStarshipsResponse = namedtuple('GetStarshipsResponse', 'status_code request response')
GetStarshipInformationResponse = namedtuple('GetStarshipInformationResponse', 'status_code request response')


def mock_starships():
    """mock data starships
        return dict w"""
    return {
        "name": fake.name(),
        "model": fake.name(),
        "manufacturer": fake.name(),
        "cost_in_credits": fake.random_int(),
        "length": fake.random_int(),
        "max_atmosphering_speed": fake.random_int(),
        "hyperdrive_rating": fake.random_int(),
        "MGLT": fake.random_int(),
        "url": f"https://swapi.dev/api/starships/{fake.random_int()}/"
    }


class SwapiApiConsumerSpy:
    ''' Spy for SwapiApiConsumer '''

    def __init__(self) -> None:
        self.get_starships_attributes: dict = {}
        self.get_starship_information_attributes: dict = {}

    def get_starships(self, page: int) -> Any:
        ''' mock to get_starships '''

        self.get_starships_attributes["page"] = page
        return GetStarshipsResponse(status_code=200,
                                    request=None,
                                    response={"results": [mock_starships(), mock_starships()]}
                                    )

    def get_starship_information(self, starship_id: int) -> Any:
        ''' mock to get_starship_information '''

        self.get_starship_information_attributes["starship_id"] = starship_id
        return GetStarshipInformationResponse(
            status_code=200,
            request=None,
            response=mock_starships()
        )
