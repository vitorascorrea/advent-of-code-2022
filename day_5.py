class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Column:
  def __init__(self, values = []):
    self.root = self.build_stack(values)


  def build_stack(self, values):
    if len(values) == 0:
      return Node(None)

    reversed_values = list(reversed(values))
    root = Node(reversed_values[0])
    current = root

    for i in range(1, len(reversed_values)):
      if reversed_values[i] == "0":
        break
      new_node = Node(reversed_values[i])
      current.next = new_node
      current = new_node

    return root


  def get_top_of_stack(self):
    if self.root == None:
      return None

    current = self.root

    while current.next:
      current = current.next

    return current


  def add_crate(self, value):
    top_of_stack = self.get_top_of_stack()
    if top_of_stack == None:
      self.root = Node(value)
    else:
      top_of_stack.next = Node(value)


  def pop(self):
    if self.root.next == None:
      aux = self.root
      self.root = None
      return aux

    previous = None
    current = self.root

    while current.next:
      previous = current
      current = current.next

    previous.next = None

    return current


class Crates:
  def __init__(self, initial_matrix):
    self.base_nodes = self.build_base_nodes(initial_matrix)


  def build_base_nodes(self, matrix):
    nodes = []
    num_columns = len(matrix[0])

    for i in range(num_columns):
      column = [row[i] for row in matrix]
      column_root = Column(column)
      nodes.append(column_root)

    return nodes


  def get_top_crate_for_each_stack(self):
    result = ""
    for node in self.base_nodes:
      top_node = node.get_top_of_stack()
      if top_node:
        result += top_node.value
      else:
        result += "0"

    return result


def solve_second(crates, instructions):
  crates_obj = Crates(crates)

  for instruction in instructions:
    quantity = instruction[0]
    origin = instruction[1] - 1  # zero indexed
    target = instruction[2] - 1

    origin_column = crates_obj.base_nodes[origin]
    target_column = crates_obj.base_nodes[target]

    popped_nodes = []
    for _ in range(quantity):
      popped_nodes.append(origin_column.pop())

    for node in reversed(popped_nodes):
      target_column.add_crate(node.value)

  return crates_obj.get_top_crate_for_each_stack()


def solve_first(crates, instructions):
  crates_obj = Crates(crates)

  for instruction in instructions:
    quantity = instruction[0]
    origin = instruction[1] - 1 # zero indexed
    target = instruction[2] - 1

    origin_column = crates_obj.base_nodes[origin]
    target_column = crates_obj.base_nodes[target]

    for _ in range(quantity):
      origin_crate = origin_column.pop()
      target_column.add_crate(origin_crate.value)

  return crates_obj.get_top_crate_for_each_stack()


def parse_input(lines):
  crates = []
  instructions = []
  parsing_crates = True

  for line in lines:
    if line == "" or line[1] == "1":
      parsing_crates = False
      continue

    if parsing_crates:
      crates.append(parse_crates_line(line))
    else:
      instructions.append(parse_instructions_line(line))

  return crates, instructions


def parse_crates_line(line):
  formatted_line = []

  for i in range(0, len(line), 4):
    crate = line[i: i + 3]
    formatted_crate = crate.replace("]", "").replace("[", "")
    formatted_crate = formatted_crate.replace("   ", "0")
    formatted_line.append(formatted_crate)

  return formatted_line


def parse_instructions_line(line):
  return list(map(int, line.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")))


if __name__ == '__main__':
  f = open('inputs/day_5_1.txt')
  raw_input = f.read()

  lines = list(raw_input.splitlines())
  crates, instructions = parse_input(lines)

  print(solve_first(crates, instructions))
  print(solve_second(crates, instructions))
