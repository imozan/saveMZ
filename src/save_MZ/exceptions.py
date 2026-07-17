class SaveMZError(Exception):
    """Base exception for SaveMZ."""
    pass

class PathNotFoundError(SaveMZError):
    """Raised when the specified path does not exist."""
    pass

class InvalidEventError(SaveMZError):
    """Raised when an invalid event name is used."""
    pass

class InvalidDataError(SaveMZError):
    """Raised when invalid data is provided."""
    pass
