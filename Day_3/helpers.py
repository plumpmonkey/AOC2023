from enum import Enum
from dataclasses import dataclass

# Define the colours used for text printing
class Colours(Enum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    NORMAL = "\033[0m"

# (defined as a dataclass - new in Python 3.7 - https://realpython.com/python-data-classes/)
@dataclass(frozen=True)
class Point:
    """ Define the x,y coordinates that make a point """
    x: int
    y: int

    # Add a vector to the point and return a new point
    def __add__(self, vector_point):
        return Point(self.x + vector_point.x, self.y + vector_point.y)

    def neighbours(self, include_diagonals=True):
        """ Return a list of the points that are adjacent to this point. """
        if include_diagonals:
            return [Point(self.x + x, self.y + y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]
        else:
            return [Point(self.x + x, self.y + y) for x in range(-1, 2, 2) for y in range(-1, 2, 2) if x != 0 or y != 0]
    
    # Use the __repr__ function to print the point
    def __repr__(self) -> str:
        return (f'({self.x}, {self.y})')


@dataclass(frozen=True)
class Grid:
    """ A 2D grid of points. """
    def __init__(self, grid_array: list) -> None:
        self._grid_array = grid_array
        self._width = len(self._grid_array[0])
        self._height = len(self._grid_array)

    def get_value(self, point: Point) -> str:
        """ Return the value of a point in the grid. """
        return self._grid_array[point.y][point.x]
    
    def set_value(self, point: Point, value: str) -> None:
        """ Set the value of a point in the grid. """
        self._grid_array[point.y][point.x] = value

    def validate_point(self, point: Point) -> bool:
        """ Check if a point is within the grid. """
        if point.x < 0 or point.x >= self._width:
            return False
        if point.y < 0 or point.y >= self._height:
            return False
        return True

    def width(self) -> int:
        """ Return the width of the grid. """
        return self._width
    
    def height(self) -> int:
        """ Return the height of the grid. """
        return self._height
    
    def all_points(self) -> list[Point]:
        """ Return a list of all the points in the grid. """
        return [Point(x, y) for y in range(self._height) for x in range(self._width)]

    def cols_as_str(self):
        """ Render columns as str. Returns: list of str """
        cols_list = list(zip(*self._grid_array))
        return ["".join(str(char) for char in col) for col in cols_list]
    
    def __repr__(self) -> str:
        return f'Grid(size={self._width}x{self._height})'
    
    def __str__(self) -> str:
        """ Return a string representation of the grid. """
        return "\n".join(["".join(map(str,row)) for row in self._grid_array])
    
