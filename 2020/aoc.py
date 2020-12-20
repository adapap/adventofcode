"""A collection of data structures and algorithms for Advent of Code puzzles."""
import heapq
import os
import re
import requests
import sys
from collections import defaultdict
from itertools import cycle, product
from typing import Any, Sequence, Union

URL = 'https://adventofcode.com/{year}/day/{day}'
LOCAL = 'inputs/{day}.txt'

class Puzzle:
    """
    Manages retrieval and submission for Advent of Code puzzles.
    Requires token to be present in environment or `token.txt`.
    """
    def __init__(self, *, day: int, year: int, input_path: str=LOCAL) -> None:
        self.day = day
        self.year = year
        if self.year <= 2015 or not 1 <= self.day <= 25:
            raise ValueError('Day must be within range 1-25 and year cannot be before 2015.')
    
        TOKEN = os.getenv('AOC_TOKEN')
        if not TOKEN:
            if not os.path.exists(os.path.relpath('../token.txt')):
                print('Missing token file. Find your token (in developer tools: Application -> Cookies -> "session") on Advent of Code.')
                sys.exit(1)
            with open('../token.txt') as f:
                TOKEN = f.read().strip()
        self.token = TOKEN
        self.input_path = input_path.format(day=day)
    
    @property
    def base_url(self) -> str:
        """Returns the base url for HTTP requests to adventofcode.com"""
        return URL.format(year=self.year, day=self.day)
        
    def fetch(self, *, no_strip=False, numeric=False) -> Union[str, int]:
        """Retrieves the puzzle input as a single string."""
        if os.path.exists(self.input_path):
            with open(self.input_path) as f:
                if no_strip:
                    return f.read()
                else:
                    return f.read().strip()
        response = requests.get(self.base_url + '/input', cookies={'session': self.token}).text
        if 'Puzzle inputs differ by user.  Please log in to get your puzzle input.' in response:
            raise ValueError('Token has expired. Please go to Applications -> Cookies and get the new token.')
        else:
            with open(self.input_path, 'w') as f:
                f.write(response)
        if numeric:
            return int(response)
        if no_strip:
            return response
        else:
            return response.strip()

    def fetch_by_line(self, *, no_strip=False, numeric=False) -> Sequence[Any]:
        """Returns the puzzle input split by newlines."""
        data = str(self.fetch(no_strip=no_strip))
        if no_strip:
            lines = data.split('\n')
        else:
            lines = data.strip().split('\n')
        if numeric:
            return list(map(int, lines))
        return lines
    
    def submit(self, part: int, answer: Any):
        res = requests.post(self.base_url + '/answer',
                            cookies={'session': self.token},
                            data={
                                'level': part,
                                'answer': str(answer),
                            })
        body = re.search(r'<article>(.+)</article>', res.text, re.DOTALL)
        if not body or not len(body.groups()):
            print('Error submitting answer - response:\n', res.text)
            return
        text = body.groups()[0]
        text = re.sub(r'(<.+?>|</.+?>)', '', text)
        text = re.sub(r' +', ' ', text)
        print(text)

class Grid2D:
    """Utility class which allows mapping of points onto a grid and 2D movement."""
    def __init__(self, *, default=None):
        self.points = defaultdict(lambda: default)
        self.default = default
        self.max_x = self.max_y = -float('inf')
        self.min_x = self.min_y = float('inf')

    # Movement
    cardinal = [-1 - 1j, 0 - 1j, 1 - 1j, -1, 1, -1 + 1j, 0 + 1j, 1 + 1j]
    orthogonal = [0 - 1j, -1 + 0j, 0 + 1j, 1 + 0j]
    diagonal = [-1 - 1j, 1 - 1j, -1 + 1j, 1 + 1j]
    north, west, south, east = orthogonal
    
    @property
    def corners(self) -> list:
        return [(self.min_x, self.min_y), (self.min_x, self.max_y), (self.max_x, self.min_y), (self.max_x, self.max_y)]
    
    @property
    def x_range(self) -> int:
        """Returns the width of the grid."""
        return self.max_x - self.min_x
    
    @property
    def y_range(self) -> int:
        """Returns the height of the grid."""
        return self.max_y - self.min_y

    def item(self, pos):
        """Returns the current item at the point."""
        return self[self.convert(pos)]

    def convert(self, item) -> complex:
        """Converts tuples to complex numbers."""
        if type(item) != complex:
            return complex(*item)
        return item

    def revert(self, comp):
        """Converts complex numbers to a tuple (x, y)."""
        return (comp.real, comp.imag)
    
    def render(self, keys={}):
        """Visualizes the grid in 2D ASCII characters."""
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                char = self[x, y]
                print(keys.get(char, char), end='')
            print()

    def manhattan(self, p1, p2) -> float:
        """Computes the manhattan distance to another point."""
        p1, p2 = map(self.convert, (p1, p2))
        return abs(p1.real - p2.real) + abs(p1.imag - p2.imag)

    def __contains__(self, item):
        return self.convert(item) in self.points

    def __getitem__(self, item):
        return self.points[self.convert(item)]

    def __setitem__(self, item, value):
        item = self.convert(item)
        if item.real > self.max_x:
            self.max_x = int(item.real)
        if item.real < self.min_x:
            self.min_x = int(item.real)
        if item.imag > self.max_y:
            self.max_y = int(item.imag)
        if item.imag < self.min_y:
            self.min_y = int(item.imag)
        self.points[item] = value

    def __repr__(self):
        return f'Grid2D(default=\'{self.default}\')'

class Vector:
    """Operations on numeric sequence and <x, y, z> vectors."""
    def __init__(self, *seq):
        self.sequence = seq

    @property
    def x(self):
        """Returns the first element of the sequence."""
        try:
            return self.sequence[0]
        except IndexError:
            print('Vector has no x element.')

    @property
    def y(self):
        """Returns the second element of the sequence."""
        try:
            return self.sequence[1]
        except IndexError:
            print('Vector has no y element.')

    @property
    def z(self):
        """Returns the third element of the sequence."""
        try:
            return self.sequence[2]
        except IndexError:
            print('Vector has no z element.')

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self.sequence, other.sequence)))
    __radd__ = __add__

    def __sub__(self, other):
        return Vector(*(a - b for a, b in zip(self.sequence, other.sequence)))
    __rsub__ = __sub__

    def __repr__(self):
        return f'<{", ".join(map(str, self.sequence))}>'

class Geometry:
    """Collection of common geometrical methods and values."""
    cardinal = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    intercardinal = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    @staticmethod
    def manhattan(p1, p2):
        """Computes the manhattan distance between two points."""
        return sum(abs(a2 - a1) for a1, a2 in zip(p1, p2))

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

class defaultlist(list):
    def __init__(self, factory=None):
        """List extending automatically to the maximum requested length.
        Same functionality as collections.defaultdict."""
        self.__factory = factory or defaultlist.__nonefactory

    @staticmethod
    def __nonefactory():
        return None

    def __fill(self, index):
        missing = index - len(self) + 1
        if missing > 0:
            self += [self.__factory() for idx in range(missing)]

    def __setitem__(self, index, value):
        self.__fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__getslice(index.start, index.stop, index.step)
        else:
            self.__fill(index)
            return list.__getitem__(self, index)

    def __getslice__(self, start, stop, step=None):
        return self.__getslice(start, stop, step)

    def __normidx(self, idx, default):
        if idx is None:
            idx = default
        elif idx < 0:
            idx += len(self)
        return idx

    def __getslice(self, start, stop, step):
        end = max((start or 0, stop or 0, 0))
        if end:
            self.__fill(end)
        start = self.__normidx(start, 0)
        stop = self.__normidx(stop, len(self))
        step = step or 1
        r = defaultlist(factory=self.__factory)
        for idx in range(start, stop, step):
            r.append(list.__getitem__(self, idx))
        return r

    def __add__(self, other):
        if isinstance(other, list):
            r = self.copy()
            r += other
            return r
        else:
            return list.__add__(self, other)

    def copy(self):
        """Return a shallow copy of the list. Equivalent to a[:]."""
        r = defaultlist(factory=self.__factory)
        r += self
        return r
        
# Utility methods
def nested_enum(iterable: Sequence[Any], indices=tuple(), depth=2):
    """Nested iteration yielding indices and elements at each loop."""
    for i, x in enumerate(iterable):
        if depth == 0:
            yield indices, x
        else:
            yield from nested_enum(x, indices=(i,) + indices, depth=depth - 1)

def print_ans(puzzle: str, answer: Any):
    """Prints the answer to a puzzle in the form `puzzle: answer`."""
    print('Day {}: {}'.format(puzzle, answer))

class Math:
    @staticmethod
    def prod(*values: int) -> int:
        """Calculates the product of a list."""
        p = 1
        for x in values:
            p *= x
        return p

    @staticmethod
    def compare(a: Any, b: Any) -> int:
        """Returns +1 or -1 if a is different from b, otherwise 0."""
        return (a > b) - (a < b)
