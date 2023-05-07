from logic.crs.visitor import Visitor


class Package:
    """
  This class represents a package or piece of correspondence that a visitor enters.

  Attributes:
    subject (Visitor): The person who will carry the package.
    name (str): The name of the package.
    description (str): The description of the package (e.g. weight, size, etc.).
    code (int): The code of the package.

  Methods:
    equals(self, other) -> bool: Checks if two packages are equal.

  """

    def __init__(self, subject: Visitor, name: str = 'name', description: str = 'description', code: int = 0):
        """
    The constructor of the Package class.

    Args:
      subject (Visitor): The person who will carry the package.
      name (str): The name of the package (default 'name').
      description (str): The description of the package (default 'description').
      code (int): The code of the package (default 0).
    """
        self._name = name
        self._description = description
        self._code = code
        self.subject = subject

    @property
    def name(self) -> str:
        """
    Get the name of the package.

    Returns:
      str: The name of the package.
    """
        return self._name

    @name.setter
    def name(self, value) -> None:
        """
    Set the name of the package.

    Args:
      value (str): The name of the package.
    """
        self._name = value

    @property
    def description(self) -> str:
        """
    Get the description of the package.

    Returns:
      str: The description of the package.
    """
        return self._description

    @description.setter
    def description(self, value) -> None:
        """
    Set the description of the package.

    Args:
      value (str): The description of the package.
    """
        self._description = value

    @property
    def code(self) -> int:
        """
    Get the code of the package.

    Returns:
      str: The code of the package.
    """
        return self._code

    @code.setter
    def code(self, value) -> None:
        """
    Set the code of the package.

    Args:
      value (int): The code of the package.
    """
        self._code = value

    @property
    def subject(self) -> Visitor:
        """
    Get the person who will carry the package.

    Returns:
      str: The person who will carry the package.
    """
        return self._subject

    @subject.setter
    def subject(self, value) -> None:
        """
    Set the person who will carry the package.

    Args:
      value (Visitor): The person who will carry the package.
    """
        self._subject = value

    def __str__(self):
        """
    Return a string with the information of the package.

    Returns:
      str: The information of the package.
    """
        return (f"\nInformacion del objeto\n"
                f"\n{self.subject}"
                f"\n* Nombre: {self.name}"
                f"\n* Descripcion: {self.description}"
                f"\n* Codigo: {self.code}")

    def equals(self, other) -> bool:
        """
    Compare two Package objects by their name, description, code, and subject.

    Args:
        other (Package): The other Package object to compare with.

    Returns:
        bool: True if both objects have the same attributes. False otherwise.
    """
        if isinstance(other, Package):
            return (self.name == other.name and
                    self.description == other.description and
                    self.code == other.code and
                    self.subject == other.subject)
        return False
