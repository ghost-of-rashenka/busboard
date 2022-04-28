from abc import ABC


class AbstractTrip(ABC):
    """A unique trip for a particular transit route."""

    def __init__(self):
        self._id = None             # The unique identifier for the trip
        self._route = None          # The route name/number
        self._suffix = None         # Any modifier to the route (e.g. a letter)
        self._direction = None      # The direction of the trip (e.g. "Eastbound")
        self._latitude = 0.0         # The last latitude reading.
        self._longitude = 0.0        # The last longitude reading.

    @property
    def id(self) -> str:
        return self._id

    @property
    def route(self) -> str:
        return self._route

    @property
    def suffix(self) -> str:
        return self._suffix

    @property
    def direction(self) -> str:
        return self._direction

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = float(value)

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = float(value)


class AbstractDeparture(ABC):
    """A unique departure of a Trip from a Stop."""

    def __init__(self):
        self._stop = None               # The Stop the Departure belongs to.
        self._trip = None               # The Trip leaving for the Departure.
        self._scheduled_time = None     # A scheduled time.
        self._actual_time = None        # The actual time as estimated by the system.
        self.live = False               # Whether the departure is updated in real time.

    @property
    def stop(self) -> str:
        return self._stop

    @property
    def trip(self) -> AbstractTrip:
        return self._trip

    @property
    def scheduled_time(self) -> int:
        return self._scheduled_time

    @property
    def actual_time(self) -> int:
        return self._actual_time

    @actual_time.setter
    def actual_time(self, value):
        # In reality this probably has to be overridden with something useful.
        self._actual_time = int(value)


class AbstractStop(ABC):
    """A unique stop that lists Departures."""

    def __init__(self):
        self._stop_id = None
        self._name = None
        self._latitude = 0.0
        self._longitude = 0.0
        self.open = True
        self.alerts = []
        self.departures = []

    @property
    def stop_id(self) -> str:
        return self.stop_id

    @property
    def name(self) -> str:
        return self.name

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude
