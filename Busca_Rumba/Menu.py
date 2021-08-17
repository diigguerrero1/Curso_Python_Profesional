class Menu:
    id = int
    message = str
    value = input

    def __init__(self, id, message, value):
        self._id = id
        self.message = message
        self._value = value
