import os

GRID_LIMIT = 1000

class Coordinates:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  def __eq__(self, other):
    """Overrides the default implementation"""
    if isinstance(other, Coordinates):
        return self.x == other.x and self.y == other.y
    if isinstance(other, tuple):
        return self.x == other[0] and self.y == other[1]
    return False

  def __hash__(self):
    return hash((self.x, self.y))

  def to_tuple(self):
    return (self.x, self.y)


class Grid:
  def __init__(self, lines) -> None:
    self.lines = lines
    self.grid = [["." for _ in range(GRID_LIMIT)] for _ in range(GRID_LIMIT)]
    self.sand_pour_coordinates = Coordinates(0, 500)
    self.build_grid()


  def build_grid(self):
    for line in self.lines:
      coordinates = line.split(" -> ")
      for i in range(1, len(coordinates)):
        start = coordinates[i - 1]
        end = coordinates[i]

        # converting coordinates into rows and columns
        start_y, start_x = list(map(int, start.split(",")))
        end_y, end_x = list(map(int, end.split(",")))

        if start_x == end_x and start_y != end_y:
          bigger = start_y if start_y > end_y else end_y
          smaller = start_y if start_y < end_y else end_y

          for y in range(smaller, bigger + 1):
            self.grid[start_x][y] = "#"
        elif start_x != end_x and start_y == end_y:
          bigger = start_x if start_x > end_x else end_x
          smaller = start_x if start_x < end_x else end_x

          for x in range(smaller, bigger + 1):
            self.grid[x][start_y] = "#"
        else:
          pass # just a point?

    # sand pour coordinates
    self.grid[self.sand_pour_coordinates.x][self.sand_pour_coordinates.y] = "+"


  def set_floor(self):
    highest_row_with_floor = 0

    for i in range(len(self.grid)):
      if "#" in self.grid[i]:
        highest_row_with_floor = i

    for j in range(GRID_LIMIT):
      self.grid[highest_row_with_floor + 2][j] = "#"


  def print(self, x_cut_range=None, y_cut_range=None):
    os.system('clear')

    start_x = 0 if not x_cut_range else x_cut_range[0]
    end_x = len(self.grid) if not x_cut_range else x_cut_range[1]

    start_y = 0 if not y_cut_range else y_cut_range[0]
    end_y = len(self.grid[0]) if not y_cut_range else y_cut_range[1]

    for i in range(start_x, end_x):
      for j in range(start_y, end_y):
        cell = self.grid[i][j]
        print(cell, end="")
      print()


  def coordinate_at(self, coordinate):
    return self.grid[coordinate.x][coordinate.y]


  def pour_sand_grain(self):
    grain_coordinate = self.sand_pour_coordinates

    while True:
      if grain_coordinate.x >= GRID_LIMIT - 1:
        return "overflowing"

      next_possible_down = Coordinates(grain_coordinate.x + 1, grain_coordinate.y)
      next_possible_left = Coordinates(grain_coordinate.x + 1, grain_coordinate.y - 1)
      next_possible_right = Coordinates(grain_coordinate.x + 1, grain_coordinate.y + 1)

      blocked = True

      for coord in [next_possible_down, next_possible_left, next_possible_right]:
        if self.coordinate_at(coord) == ".":
          grain_coordinate = coord
          blocked = False
          break

      if blocked:
        break

    self.grid[grain_coordinate.x][grain_coordinate.y] = "o"

    if grain_coordinate != self.sand_pour_coordinates:
      return "ok"
    else:
      return "same as origin"


def solve_second(lines):
  grid = Grid(lines)
  grid.set_floor()

  value = None
  units = 0

  while value != "same as origin":
    value = grid.pour_sand_grain()
    units += 1

  return units


def solve_first(lines):
  grid = Grid(lines)
  value = None
  units = 0

  while value != "overflowing":
    value = grid.pour_sand_grain()
    if value != "overflowing":
      units += 1

  return units


if __name__ == '__main__':
  f = open('inputs/day_14_1.txt')
  raw_input = f.read()

  lines = list(raw_input.splitlines())

  print(solve_first(lines))
  print(solve_second(lines))
