from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipsListCollectorInterface(ABC):
    """StarshipsListCollector interface"""

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        """Must implement"""
        raise NotImplementedError("Must implement list method")
