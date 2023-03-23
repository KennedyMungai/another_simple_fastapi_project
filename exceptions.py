"""A fle containing the custom exceptions"""


class StoryException(Exception):
    """A class that is the themplate for Story Exceptiond

    Args:
        Exception (Class): The main exception class
    """

    def __init__(self, name: str) -> None:
        self.name = name
