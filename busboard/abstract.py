from abc import ABC


class AbstractTrip(ABC):
    """A unique trip for a particular transit route."""

    def __init__(self):
        self._id = None             # The unique identifier for the trip
        self._route = None          # The route name/number
        self._suffix = None         # Any modifier to the route (e.g. a letter)
        self._direction = None      # The direction of the trip (e.g. "Eastbound")
        self.latitude = 0.0         # The last latitude reading.
        self.longitude = 0.0        # The last longitude reading.

    @property
    def id(self):
        return self._id

    @property
    def route(self):
        return self._route

    @property
    def suffix(self):
        return self._suffix



