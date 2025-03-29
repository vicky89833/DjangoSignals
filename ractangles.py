class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._iter_index = 0  # Tracks iteration state

    def __iter__(self):
        self._iter_index = 0  # Reset iterator for each new iteration
        return self

    def __next__(self):
        if self._iter_index == 0:
            self._iter_index += 1
            return {'length': self.length}
        elif self._iter_index == 1:
            self._iter_index += 1
            return {'width': self.width}
        else:
            raise StopIteration

    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

rect = Rectangle(5, 3)

# Iteration works
for dimension in rect:
    print(dimension)
