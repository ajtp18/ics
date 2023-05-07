class Person:
    """Represents a person with their personal information.

    Attributes:
    -----------
    name : str
        The name of the person.
    email : str
        The email of the person.
    telephone : str
        The telephone number of the person.
    id : int
        The identification number of the person.
    """

    def __init__(self, name: str = 'name', email: str = 'email', telephone: str = 'telephone', id: int = 0):
        """Creates a new instance of the Person class.

        Parameters:
        -----------
        name : str
            The name of the person (default is 'name').
        email : str
            The email of the person (default is 'email').
        telephone : str
            The telephone number of the person (default is 'telephone').
        id : int
            The identification number of the person (default is 0).
        """
        self.name = name
        self.email = email
        self.telephone = telephone
        self.id = id

    @property
    def name(self) -> str:
        """str: The name of the person."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Sets the name of the person.

        Parameters:
        -----------
        value : str
            The name of the person.
        """
        self._name = value

    @property
    def email(self) -> str:
        """str: The email of the person."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """Sets the email of the person.

        Parameters:
        -----------
        value : str
            The email of the person.
        """
        self._email = value

    @property
    def telephone(self) -> str:
        """str: The telephone number of the person."""
        return self._telephone

    @telephone.setter
    def telephone(self, value: str) -> None:
        """Sets the telephone number of the person.

        Parameters:
        -----------
        value : str
            The telephone number of the person.
        """
        self._telephone = value

    @property
    def id(self) -> int:
        """int: The identification number of the person."""
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Sets the identification number of the person.

        Parameters:
        -----------
        value : int
            The identification number of the person.
        """
        self._id = value

    def __str__(self) -> str:
        """Returns a string representation of the person.

        Returns:
        --------
        str
            A string representation of the person.
        """
        return (f"\nInformacion de la persona\n"
                f"\n* Nombre: {self.name}"
                f"\n* Email: {self.email}"
                f"\n* Telefono: {self.telephone}"
                f"\n* Id: {self.id}")

    def equals(self, other: object) -> bool:
        """Checks if two Person objects are equal.

        Parameters:
        -----------
        other : object
            The other Person object to compare with.

        Returns:
        --------
        bool
            True if the two objects are equal, False otherwise.
        """
        if isinstance(other, Person):
            return (self.name == other.name and
                    self.email == other.email and
                    self.telephone == other.telephone and
                    self.id == other.id)
        return False
