# constants
NAME = "Template App"
VERSION = "0.1.2"


class AppClass:
    """
    App class to store values and perform operations.
    """

    def __init__(self):
        self.a = 0
        self.b = 0

    def go(self):
        return round(self.a * self.b, 2)

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b
