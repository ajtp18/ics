"""the classes of person and place are imported so
that this class can be a relationship between these two"""
from logic.crs.person import Person
from logic.crs.place import Place

"""the registration class that will serve to register the entry of people is initialized"""


class Register:
    """
    the constructor of the class is made, through which we are going to call the place class and the person class
    subject: is the subject that will represent the person class
    zone: is the area that will represent the place where the person was
    """

    def __init__(self, subject: Person, zone: Place):
        self.subject = subject
        self.zone = zone

    """
    gets the subject that is part of person hat enters

    return to subject
    """

    @property
    def subject(self) -> Person:
        return self._subject

    """
    sets the subject that enters

    Args:
        value (str): gives a value to the subject that enters
    """

    @subject.setter
    def subject(self, value) -> None:
        self._subject = value

    """
    gets the zone by referencing the place class

    return to the zone 
    """

    @property
    def zone(self) -> Place:
        return self._zone

    """
    sets the zone the subject entered

    Args:
        value (str): gives a value to the zone that the subject entereds
    """

    @zone.setter
    def zone(self, value):
        self._zone = value

    def __str__(self):
        return (f"{self.subject}"
                f"\n{self.zone}")

    def equals(self, other) -> bool:
        if isinstance(other, Register):
            return (self.subject == other.subject and
                    self.zone == other.zone)
        return False
