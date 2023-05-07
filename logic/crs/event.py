from logic.crs.place import Place  # Importing the Place class


class Event:
    """
    A class representing an event.

    Attributes:
        location (Place): The Place object where the event takes place.
        id (int): The ID of the event.
        timeIn (int): The time when the event starts.
        timeOut (int): The time when the event ends.
        date (str): The date when the event takes place.
    """

    def __init__(self, location: Place, id: int = 0, timeIn: int = 0, timeOut: int = 0, date: str = 'date'):
        """
        Constructs a new Event object.

        Args:
            location (Place): The Place object where the event takes place.
            id (int, optional): The ID of the event. Defaults to 0.
            timeIn (int, optional): The time when the event starts. Defaults to 0.
            timeOut (int, optional): The time when the event ends. Defaults to 0.
            date (str, optional): The date when the event takes place. Defaults to 'date'.
        """

        self._id = id
        self._timeIn = timeIn
        self._timeOut = timeOut
        self._date = date
        self._location = location

    @property
    def id(self) -> int:
        """Getter for the ID of the event."""
        return self._id

    @id.setter
    def id(self, value) -> None:
        """Setter for the ID of the event."""
        self._id = value

    @property
    def timeIn(self) -> int:
        """Getter for the time when the event starts."""
        return self._timeIn

    @timeIn.setter
    def timeIn(self, value) -> None:
        """Setter for the time when the event starts."""
        self._timeIn = value

    @property
    def timeOut(self) -> int:
        """Getter for the time when the event ends."""
        return self._timeOut

    @timeOut.setter
    def timeOut(self, value) -> None:
        """Setter for the time when the event ends."""
        self._timeOut = value

    @property
    def date(self) -> str:
        """Getter for the date when the event takes place."""
        return self._date

    @date.setter
    def date(self, value) -> None:
        """Setter for the date when the event takes place."""
        self._date = value

    @property
    def location(self) -> Place:
        """Getter for the Place object where the event takes place."""
        return self._location

    @location.setter
    def location(self, value) -> None:
        """Setter for the Place object where the event takes place."""
        self._location = value

    def __str__(self) -> str:
        """Returns a string representation of the Event object."""
        return (f"\nInformacion del evento\n"
                f"\n* Nombre del lugar: {self.location.name}"
                f"\n* Ubicacion del lugar: {self.location.ubication}"
                f"\n* Tipo de lugar: {self.location.type_place}"
                f"\n* Id del evento: {self.id}"
                f"\n* Hora de entrada: {self.timeIn}"
                f"\n* Hora de salida: {self.timeOut}"
                f"\n* Fecha: {self.date}")

    def equals(self, other) -> bool:
        """Determines whether two Event objects are equal.

        Args:
            other (Event): The other Event object to compare.

        Returns:
            bool: True if the objects are equal, False otherwise."""

        if isinstance(other, Event):
            return (self.location == other.location and
                    self.id == other.id and
                    self.timeIn == other.timeIn and
                    self.timeOut == other.timeOut and
                    self.date == other.date)
        return False
