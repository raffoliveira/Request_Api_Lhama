from typing import Dict
from abc import ABC, abstractmethod


class ControllersInterface(ABC):
    """ Interface to COntrollers """

    @abstractmethod
    def handle(self, http_request: Dict):
        """ Method to handle request """
        raise NotImplementedError("Should implement handler method")
