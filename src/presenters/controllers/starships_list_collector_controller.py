from typing import Dict

from src.domain.usecases.starships_list_collector import StarshipsListCollectorInterface
from src.presenters.interface.controllers import ControllersInterface


class StarshipsListCollectorController(ControllersInterface):
    """Interface

    Args:
        ControllersInterface (_type_): _description_
    """

    def __init__(self, starships_list_collector: StarshipsListCollectorInterface) -> None:
        self.__use_case = starships_list_collector

    def handle(self, http_request: Dict) -> Dict:
        """handle collector list

        Args:
            http_request (Dict): _description_

        Returns:
            _type_: _description_
        """
        page = http_request["query_params"]["page"]
        starships_list = self.__use_case.list(page=page)
        http_response = {
            "status_code": 200,
            "data": {
                "data": starships_list
            }
        }
        return http_response
