from typing import Any
from cerberus import Validator


def get_pagination_validator(request: Any):
    """Validate the pagination route

    Args:
        request (Any): request information

    Raises:
        Exception: Raise exception when is false
    """
    query_param_validator = Validator({
        "page": {"type": "string", "required": True, "allowed": ["1", "2", "3", "4"]}
    })
    response = query_param_validator.validate(request.query_params)

    if response is False:
        raise Exception(query_param_validator.errors)
