from typing import Any
from collections import namedtuple
import requests
from requests import PreparedRequest

GetStartshipsResponse = namedtuple("GetStartshipsResponse", "status_code request response")


class SwapiApiConsumer:
    """Classe da SwapiApi"""

    def get_startships(self, page: int) -> Any:
        """Method to get starships

        Args:
            page (int): number of page

        Returns:
            Any: Data of response
        """

        req = requests.Request(
            method="GET",
            url="https://swapi.dev/api/starships",
            params={"page": page}
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared=req_prepared)

        return GetStartshipsResponse(response.status_code, req, response.json())

    @classmethod
    def __send_http_request(cls, req_prepared: PreparedRequest) -> Any:
        """Prepare session and send http request

        Args:
            req_prepared (Type[Request]): request object

        Returns:
            Any: http response raw
        """
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
