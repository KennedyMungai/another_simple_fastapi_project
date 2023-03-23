"""A fle containing the custom exceptions"""


class StoryException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name
