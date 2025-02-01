class TomorrowAPIError(Exception):
    """Base exception for Tomorrow.io API errors."""

    def __init__(self, code: int, message: str, type: str):
        self.message = message
        self.code = code
        self.type = type
        super().__init__(f"{message} (code: {code}, type: {type})")
