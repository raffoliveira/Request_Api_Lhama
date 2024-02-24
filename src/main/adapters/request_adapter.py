from typing import Callable
from fastapi import APIRouter, Request as RequestFastApi


async def request_adapter(request: RequestFastApi, callback: Callable):
    """request adapter

    Args:
        request (RequestFastApi): _description_
        callback (Callable): _description_

    Returns:
        _type_: _description_
    """
    body = None

    try:
        body = await request.json()
    except:
        pass

    http_request = {
        "query_params": request.query_params,
        "body": body
    }
    try:
        return callback(http_request)
    except:
        print("An error has occurred")
