from abc import ABC, abstractmethod
from typing import Dict


class StarshipInformationCollectorInterface(ABC):
    """StarshipsInformationCollectorInterface interface"""

    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> Dict:
        """Must implement"""
        raise NotImplementedError("Must implement find_starship method")
