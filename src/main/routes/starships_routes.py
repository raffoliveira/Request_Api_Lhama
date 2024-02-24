from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse

from src.validators import get_pagination_validator
from src.main.adapters import request_adapter
from src.main.composers import get_starships_in_pagination_composer

starships_routes = APIRouter()


@starships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: RequestFastApi):
    """get starships information

    Args:
        request (RequestFastApi): request to get route

    Returns:
        _type_: dic with information
    """
    get_pagination_validator(request=request)
    controller = get_starships_in_pagination_composer()

    response = await request_adapter(request=request, callback=controller.handle)

    return JSONResponse(
        status_code=response["status_code"],
        content={"data": response["data"]}
    )
