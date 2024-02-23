class HttpRequestError(Exception):
    """Classe personalizada de Http"""

    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
