from typing import Callable
from fastapi import Request as RequestFastApi


async def request_adapter(request: RequestFastApi, callback: Callable):
    """request adapter

    Args:
        request (RequestFastApi): http request object with all properties
        callback (Callable): callback to process http request

    Returns:
        _type_: http response
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

    return callback(http_request)
