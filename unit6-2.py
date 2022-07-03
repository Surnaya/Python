class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * 125

a = Road(20, 5000)
print(a.mass())