from typing import Dict, List, Type

from src.domain.usecases import StarshipsListCollectorInterface
from src.data.interfaces.swap_api_consumer import SwapiApiConsumerInterface


class StarshipsListCollector(StarshipsListCollectorInterface):
    """StarshipsListCollector """

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        response = self.__api_consumer.get_startships(page=page)
        print(response)
