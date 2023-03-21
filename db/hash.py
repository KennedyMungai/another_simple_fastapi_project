"""This file contains the hashing logic"""
from passlib.context import CryptContext


password_cxt = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash():
    """The Hash class"""

    def bcrypt(self, password: str):
        """Function encrypts the password

        Args:
            password (str): The password string provided

        Returns:
            hashed_password: The password after it has been hashed
        """
        return password_cxt.hash(password)

    def verify(self, hashed_password, plain_password):
        """A function to compare teh plain password with the hashed password

        Args:
            hashed_password (str): The password hash
            plain_password (str): A password argument before being ajhsged

        Returns:
            bool: Whether the two stings match
        """
        return password_cxt.verify(plain_password, hashed_password)
