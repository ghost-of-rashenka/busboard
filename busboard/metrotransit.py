from busboard.abstract import AbstractTrip


class MetroTransitTrip(AbstractTrip):

    def __init__(self,
                 trip_id=None,
                 route=None,
                 terminal=None,
                 direction=None,
                 latitude=None,
                 longitude=None):
        super().__init__()
        self._id = trip_id
        self._route = route
        self._suffix = terminal
        self._direction = direction
        self.latitude = latitude
        self.longitude = longitude
