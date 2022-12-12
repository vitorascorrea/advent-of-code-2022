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


class PriorityQueue:
  def __init__(self) -> None:
    self.queue = []


  def add(self, weight, value):
    self.queue.append((weight, value))


  def pop(self):
    if len(self.queue) == 0:
      return None

    min_val_index = 0
    for i in range(len(self.queue)):
      if self.queue[i][0] < self.queue[min_val_index][0]:
        min_val_index = i
    item = self.queue[min_val_index]
    del self.queue[min_val_index]

    return item


def solve_second(matrix, start_position, end_position):
  min_dist = float('inf')
  distances, _ = dijkstra(matrix, end_position, True)

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == "a" or matrix[i][j] == "S":
        coord = Coordinates(i, j)
        if coord in distances and distances[coord] < min_dist:
          min_dist = distances[coord]

  return min_dist


def solve_first(matrix, start_position, end_position):
  distances, parent = dijkstra(matrix, start_position)
  path = []
  get_path(parent, end_position.to_tuple(), path)
  # print(path)
  print(len(path))

  return distances[end_position]


def is_valid(matrix, position):
  # is inside the boundaries of the matrix?
  return position.x <= len(matrix) - 1 and position.x >= 0 and position.y <= len(matrix[0]) - 1 and position.y >= 0


def get_neighbors(matrix, current_position):
  neighbors = []
  # top (our topmost position is 0,0)
  top_position = Coordinates(current_position.x, current_position.y - 1)
  if is_valid(matrix, top_position):
    neighbors.append(top_position)

  # bottom
  bottom_position = Coordinates(current_position.x, current_position.y + 1)
  if is_valid(matrix, bottom_position):
    neighbors.append(bottom_position)

  # left
  left_position = Coordinates(current_position.x - 1, current_position.y)
  if is_valid(matrix, left_position):
    neighbors.append(left_position)

  # right
  right_position = Coordinates(current_position.x + 1, current_position.y)
  if is_valid(matrix, right_position):
    neighbors.append(right_position)

  return neighbors


def get_move_cost(matrix, current_position, next_position, reverse_move_cost = False):
  current_cost = get_position_cost(matrix, current_position)
  next_cost = get_position_cost(matrix, next_position)

  if reverse_move_cost:
    if next_cost >= current_cost or current_cost - next_cost == 1:
      return 0
  else:
    if current_cost >= next_cost or next_cost - current_cost == 1:
      return 0

  return float('inf')


def get_position_cost(matrix, position):
  value = matrix[position.x][position.y]
  if value == "S":
    value = ord("a")
  elif value == "E":
    value = ord("z")
  else:
    value = ord(value)

  return value


def dijkstra(matrix, start_position, reverse_move_cost = False):
  distances = {}
  distances[start_position] = 0
  visited = []
  parent = {}
  parent[start_position.to_tuple()] = None

  pq = PriorityQueue()
  pq.add(0, start_position)

  while len(pq.queue) > 0:
    _, current_position = pq.pop()
    visited.append(current_position)
    neighbors = get_neighbors(matrix, current_position)
    for neighbor in neighbors:
      move_cost = get_move_cost(matrix, current_position, neighbor, reverse_move_cost) + 1 # add the step cost

      if neighbor not in visited:
        if not neighbor in distances:
          distances[neighbor] = float('inf')

        old_cost = distances[neighbor]
        new_cost = distances[current_position] + move_cost
        if new_cost < old_cost:
          parent[neighbor.to_tuple()] = current_position.to_tuple()
          pq.add(new_cost, neighbor)
          distances[neighbor] = new_cost

  return distances, parent


def get_path(parent, position, path):
  if parent[position] == None:
    return

  get_path(parent, parent[position], path)

  path.append(position)


if __name__ == '__main__':
  f = open('inputs/day_12_1.txt')
  raw_input = f.read()

  matrix = [list(line) for line in raw_input.splitlines()]

  start_position = None
  end_position = None

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      cell = matrix[i][j]
      if cell == "S":
        start_position = Coordinates(i, j)
      if cell == "E":
        end_position = Coordinates(i, j)

  print(solve_first(matrix, start_position, end_position))
  print(solve_second(matrix, start_position, end_position))
