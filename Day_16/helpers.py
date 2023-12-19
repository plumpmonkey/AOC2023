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

# Define the vectors that can be used to move around the grid
class Vectors(Enum):
    N = (0,-1)
    E = (1,0)
    S = (0,1)
    W = (-1,0)

def get_enum_name_from_value(enum_class, value):
    """Return the name of an enum member for a given value."""
    for member in enum_class:
        if member.value == value:
            return member.name
    return None  


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
            return [Point(self.x + dx, self.y + dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0]
        else:
            # Adjacent points only (no diagonals)
            return [Point(self.x + dx, self.y) for dx in range(-1, 2) if dx != 0] + \
                   [Point(self.x, self.y + dy) for dy in range(-1, 2) if dy != 0]
   
    
    # Use the __repr__ function to print the point
    def __repr__(self) -> str:
        return (f'({self.x}, {self.y})')


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

    def rows_as_str(self):
        """ Render rows as str. Returns: list of str """
        return ["".join(str(char) for char in row) for row in self._grid_array]
    
    def cols_as_str(self):
        """ Render columns as str. Returns: list of str """
        cols_list = list(zip(*self._grid_array))
        return ["".join(str(char) for char in col) for col in cols_list]
    
    def insert_empty_row(self, row_index: int, blank_char) -> None:
        """ Insert an empty row at the specified index. """
        self._grid_array.insert(row_index, [blank_char] * self._width)
        self._height += 1

    def insert_empty_col(self, col_index: int, blank_char) -> None:
        """ Insert an empty column at the specified index. """
        for row in self._grid_array:
            row.insert(col_index, blank_char)
        self._width += 1

    def transpose(self) -> None:
        """ Transpose the grid. """
        self._grid_array = list(zip(*self._grid_array))
        self._width, self._height = self._height, self._width   

    def manhattan_distance(self, point_a: Point, point_b: Point) -> int:
        """ Return the Manhattan distance between two points. """
        return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)
    
    def __repr__(self) -> str:
        return f'Grid(size={self._width}x{self._height})'
    
    def __str__(self) -> str:
        """ Return a string representation of the grid. """
        return "\n".join(["".join(map(str,row)) for row in self._grid_array])
    


