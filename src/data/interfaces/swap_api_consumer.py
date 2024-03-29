from abc import ABC, abstractmethod
from typing import Tuple, Type, Dict

from requests import PreparedRequest


class SwapiApiConsumerInterface(ABC):
    """Api Consumer Interface"""

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[PreparedRequest], Dict]:
        """Must implement"""
        raise NotImplementedError("Must implement get_startships method")

    @abstractmethod
    def get_starship_information(self, starship_id: int) -> Tuple[int, Type[PreparedRequest], Dict]:
        """Must implement"""
        raise NotImplementedError("Must implement gget_starship_information method")
