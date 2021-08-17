class user:
    id = int
    name = str
    age = int

    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age