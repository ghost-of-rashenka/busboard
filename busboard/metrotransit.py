from busboard.abstract import AbstractTrip, AbstractDeparture, AbstractStop


class MetroTransitTrip(AbstractTrip):

    def __init__(self, *,
                 trip_id,
                 route,
                 terminal,
                 direction,
                 latitude,
                 longitude):
        super().__init__()
        self._id = trip_id
        self._route = route
        self._suffix = terminal
        self._direction = direction
        self.latitude = latitude
        self.longitude = longitude


class MetroTransitDeparture():

    def __init__(self, *,
                 stop,
                 trip,
                 departure_time,
                 departure_text,
                 actual):
        super().__init__()
        self._stop = stop
        self._trip = trip,
        self._scheduled_time = departure_time
        self.actual_time = departure_text
        self.live = actual
