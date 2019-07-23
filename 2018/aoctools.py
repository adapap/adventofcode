"""A collection of data structures and algorithms for Advent of Code puzzles."""
import heapq
import os
import requests

TOKEN = os.getenv('AOC_TOKEN')
if not TOKEN:
    with open('token.txt') as f:
        TOKEN = f.read()

URL = 'https://adventofcode.com/{year}/day/{day}/input'
LOCAL = 'inputs/{year}/day{day}.txt'

class Data:
    """
    Retrieves puzzle inputs for one puzzle given the day and year.
    Requires TOKEN to be present in environment or a text file.
    """
    @staticmethod
    def fetch(*, day: int, year: int, no_strip=False):
        """Retrieves the raw data from the website."""
        if year < 2015 or not 1 <= day <= 25:
            raise ValueError('Day must be within range 1-25 and year must be after 2015.')

        url = URL.format(year=year, day=day)
        local_path = os.path.join(os.pardir, LOCAL.format(year=year, day=day))
        if os.path.exists(local_path):
            with open(local_path) as f:
                if no_strip:
                    return f.read()
                else:
                    return f.read().strip()
        response = requests.get(url, cookies={'session': TOKEN})
        with open(local_path, 'w') as f:
            f.write(response.text)
        if no_strip:
            return response.text
        else:
            return response.text.strip()

    @staticmethod
    def generator(iterable):
        """Helper method to use generators for parsing data."""
        yield from iterable

    @staticmethod
    def fetch_by_line(*, day: int, year: int, gen=False, no_strip=False):
        """
        Returns an iterable to get data by line.
        Set gen to True to return a generator.
        """
        data_str = Data.fetch(day=day, year=year, no_strip=no_strip)
        if no_strip:
            lines = data_str.split('\n')
        else:
            lines = data_str.strip().split('\n')
        return Data.generator(data_str) if gen else lines

    @staticmethod
    def double_enum(iterable):
        """Nested iteration yielding indices and elements at each loop."""
        for i, row in enumerate(iterable):
            for j, item in enumerate(row):
                yield i, j, item


class Grid:
    """
    General purpose infinite grid with management of states.
    States can be manipulated using dictionary notation:
        Setting states: custom_grid[4, 3] = 12
        Getting states: custom_grid[4, 3] -> 12
    """
    def __init__(self, *, bounds={}, default=None):
        """
        Bounds is a dictionary of tuples for each axis.
        x: (0, 3) would make the bound equal to 0 <= x <= 3
        """
        self.bounds = bounds
        self.points = {}
        self.default = default

    def __setitem__(self, point, value):
        """Sets a point using dictionary notation."""
        self.points[point] = value

    def __getitem__(self, point):
        """Retrieves a value using dictionary notation."""
        if self.bounds:
            x, y = point
            x1, x2 = self.bounds['x']
            y1, y2 = self.bounds['y']
            if not x1 <= x <= x2:
                raise IndexError('X value out of bounds')
            if not y1 <= y <= y2:
                raise IndexError('Y value out of bounds')
        return self.points.get(point, self.default)

    def __contains__(self, point):
        """Check if a point is set in the grid."""
        return point in self.points

    def __repr__(self):
        return f'Grid(bounds={self.bounds}, default={self.default})'

class Grid2D:
    """Utility class which allows mapping of points onto a grid and 2D movement."""
    def __init__(self, *, default=None):
        self.points = {}
        self.default = default

    # Movement
    intercardinal = [-1 - 1j, 0 - 1j, 1 - 1j, -1, 1, -1 + 1j, 0 + 1j, 1 + 1j]
    cardinal = [0 - 1j, -1 + 0j, 1 + 0j, 0 + 1j]
    north, west, south, east = cardinal

    @staticmethod
    def item(pos):
        """Returns the current item at the point."""
        return self[self.convert(pos)]

    @staticmethod
    def convert(item):
        """Converts tuples to complex numbers."""
        if type(item) != complex:
            return complex(*item)
        return item

    @staticmethod
    def revert(comp):
        """Converts complex numbers to a tuple (x, y)."""
        return (comp.real, comp.imag)

    def manhattan(self, p1, p2):
        """Computes the manhattan distance to another point."""
        p1, p2 = map(self.convert, (p1, p2))
        return abs(p1.real - p2.real) + abs(p1.imag - p2.imag)

    def __contains__(self, item):
        return self.convert(item) in self.points

    def __getitem__(self, item):
        return self.points[self.convert(item)]

    def __setitem__(self, item, value):
        self.points[self.convert(item)] = value

    def __repr__(self):
        return f'Grid2D(default={self.default})'

class IntTuple(tuple):
    """Custom tuple which can handle operations on integers."""
    def __new__(cls, *data):
        return super().__new__(cls, tuple(int(x) for x in data))

    def __add__(self, other):
        return tuple(x + y for x, y in zip(self, other))
    __radd__ = __add__

    def __sub__(self, other):
        return tuple(x - y for x, y in zip(self, other))
    __rsub__ = __sub__

class Vector:
    """Standard operations on <x, y> vectors."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    __radd__ = __add__

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    __rsub__ = __sub__

    def __repr__(self):
        return f'<{self.x}, {self.y}>'

class Geometry:
    """Collection of common geometrical methods and values."""
    @staticmethod
    def manhattan(p1, p2):
        """Computes the manhattan distance between two points."""
        return sum(abs(a2 - a1) for a1, a2 in zip(p1, p2))

    cardinal = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    intercardinal = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    @staticmethod
    def neighbors(p):
        """Returns points directly neighboring a given point."""
        return [(p[0] + d[0], p[1] + d[1]) for d in Geometry.cardinal]

    @staticmethod
    def adjacent(p):
        """Returns points adjacent to a point (including diagonals)."""
        return [(p[0] + d[0], p[1] + d[1]) for d in Geometry.intercardinal]

    @staticmethod
    def border_rect(min_p, max_p):
        """A generator which yields points corresponding to the border of a rectangle."""
        x0, y0 = min_p
        x1, y1 = max_p
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if y0 < y < y1 and x0 < x < x1:
                    continue
                yield (x, y)

class PriorityQueue:
    """A data structure in which elements get added according to priority values"""
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def print_ans(puzzle, answer):
    print(f'Day {puzzle}: {answer}')