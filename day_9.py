class Node:
  def __init__(self, x = 0, y = 0) -> None:
    self.x = x
    self.y = y
    self.next = None

  def __eq__(self, other):
    """Overrides the default implementation"""
    if isinstance(other, Node):
        return self.x == other.x and self.y == other.y
    if isinstance(other, tuple):
        return self.x == other[0] and self.y == other[1]
    return False


  def to_tuple(self):
    return (self.x, self.y)


class Snake:
  def __init__(self):
    self.nodes = []


  def add_node(self, node):
    if self.tail():
      tail = self.tail()
      tail.next = node

    self.nodes.append(node)


  def head(self):
    return self.nodes[0]


  def tail(self):
    if len(self.nodes) > 0:
      return self.nodes[-1]
    else:
      return None


def solve_second(lines):
  snake = Snake()
  tails_visits = [(0, 0)]

  for _ in range(10):
    node = Node()
    snake.add_node(node)

  for direction, value in lines:
    for _ in range(value):
      current_node = snake.head()
      next_node = current_node.next
      calculate_head_movement(current_node, direction)

      while next_node:
        calculate_immediate_movement(current_node, next_node)
        current_node = next_node
        next_node = current_node.next

      tails_visits.append(current_node.to_tuple())

  return len(set(tails_visits))


def solve_first(lines):
  tails_coordinate = Node()
  heads_coordinate = Node()
  tails_visits = [(0, 0)]

  for direction, value in lines:
    for _ in range(value):
      calculate_head_movement(heads_coordinate, direction)
      calculate_immediate_movement(heads_coordinate, tails_coordinate)
      tails_visits.append(tails_coordinate.to_tuple())

  return len(set(tails_visits))


def calculate_head_movement(heads_coordinate, direction):
  if direction == "U":
    heads_coordinate.y += 1
  elif direction == "D":
    heads_coordinate.y -= 1
  elif direction == "L":
    heads_coordinate.x -= 1
  else:
    heads_coordinate.x += 1


def calculate_immediate_movement(heads_coordinate, tails_coordinate):
  if coordinate_around_coordinate(heads_coordinate, tails_coordinate):
    return

  if tails_coordinate.x == heads_coordinate.x:
    if heads_coordinate.y > tails_coordinate.y:
      tails_coordinate.y += 1
    else:
      tails_coordinate.y -= 1
  elif tails_coordinate.y == heads_coordinate.y:
    if heads_coordinate.x > tails_coordinate.x:
      tails_coordinate.x += 1
    else:
      tails_coordinate.x -= 1
  else: # diagonal move
    if heads_coordinate.y > tails_coordinate.y:  # top two diagonals
      if heads_coordinate.x > tails_coordinate.x: # upper right diagonal
        tails_coordinate.x += 1
        tails_coordinate.y += 1
      else: # upper left diagonal
        tails_coordinate.x -= 1
        tails_coordinate.y += 1
    else: # bottom two diagonals
      if heads_coordinate.x > tails_coordinate.x:  # bottom right diagonal
        tails_coordinate.x += 1
        tails_coordinate.y -= 1
      else:  # bottom left diagonal
        tails_coordinate.x -= 1
        tails_coordinate.y -= 1


def coordinate_around_coordinate(coord_a, coord_b):
  # True if coord_a is anywhere in the 8 coordinates around coord_b or in the same as coord_b
  if coord_a == coord_b:
    return True
  if coord_a.x == coord_b.x:
    if coord_a.y == coord_b.y + 1:
      return True
    if coord_a.y == coord_b.y - 1:
      return True
  if coord_a.y == coord_b.y:
    if coord_a.x == coord_b.x + 1:
      return True
    if coord_a.x == coord_b.x - 1:
      return True
  if (coord_b.x + 1, coord_b.y + 1) == coord_a:
    return True
  if (coord_b.x - 1, coord_b.y + 1) == coord_a:
    return True
  if (coord_b.x + 1, coord_b.y - 1) == coord_a:
    return True
  if (coord_b.x - 1, coord_b.y - 1) == coord_a:
    return True

  return False


if __name__ == '__main__':
  f = open('inputs/day_9_1.txt')
  raw_input = f.read()

  lines = [(line.split(" ")[0], int(line.split(" ")[1])) for line in raw_input.splitlines()]

  print(solve_first(lines))
  print(solve_second(lines))
