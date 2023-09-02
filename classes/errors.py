class WatchlistNotFoundError(Exception):
    def __init__(self, message="Watchlist elements not found on page"):
        super().__init__(message)