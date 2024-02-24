from typing import Type, Tuple, Dict, Any
from collections import namedtuple

import requests
from requests import PreparedRequest
from src.errors import HttpRequestError
from src.data.interfaces.swap_api_consumer import SwapiApiConsumerInterface

GetStarshipsResponse = namedtuple("GetStarshipsResponse", "status_code request response")
GetStarshipsInformationResponse = namedtuple("GetStarshipsInformationResponse", "status_code request response")


class SwapiApiConsumer(SwapiApiConsumerInterface):
    """Classe da SwapiApi"""

    def get_starships(self, page: int) -> Tuple[int, Type[PreparedRequest], Dict]:
        """Method to get starships

        Args:
            page (int): number of page

        Returns:
            Any: Data of response
        """

        req = requests.Request(
            method="GET",
            url="https://swapi.dev/api/starships/",
            params={"page": page}
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared=req_prepared)

        if response.status_code >= 200 and response.status_code <= 299:
            return GetStarshipsResponse(status_code=response.status_code, request=req, response=response.json())

        raise HttpRequestError(message=response.json()["detail"], status_code=response.status_code)

    def get_starship_information(self, starship_id: int) -> Tuple[int, Type[PreparedRequest], Dict]:
        """Method to get info starship

        Args:
            starship_id (int): number of starship_id

        Returns:
            Any: Data of response
        """

        req = requests.Request(
            method="GET",
            url=f"https://swapi.dev/api/starships/{starship_id}"
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared=req_prepared)

        if response.status_code >= 200 and response.status_code <= 299:
            return GetStarshipsInformationResponse(
                status_code=response.status_code,
                request=req,
                response=response.json()
            )

        raise HttpRequestError(message=response.json()["detail"], status_code=response.status_code)

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
