class Node:
  def __init__(self, value, children = [], parent = None):
    self.value = value
    self.children = children
    self.parent = parent
    self.files = []


  def add_child(self, value):
    has_child_with_value = self.find_child_by_value(value)

    if has_child_with_value:
      return has_child_with_value

    new_child = Node(value, [], self)
    self.children.append(new_child)

    return new_child


  def find_child_by_value(self, value):
    for child in self.children:
      if child.value == value:
        return child

    return None


  def add_file(self, file_name, file_size):
    for (name, _) in self.files:
      if name == file_name:
        return

    self.files.append((file_name, file_size))


  def file_size_sum(self):
    file_sum = 0

    for (_, size) in self.files:
      file_sum += size

    return file_sum


  def total_dir_size(self):
    dir_sum = self.file_size_sum()

    if len(self.children) == 0:
      return dir_sum

    child_values = 0
    for child in self.children:
      child_dir_size = child.total_dir_size()
      child_values += child_dir_size

    return child_values + dir_sum


class DirectoryTree:
  def __init__(self):
    self.root = Node("/", [])


  def build(self, lines):
    current_node = self.root

    for i in range(1, len(lines)):
      line = lines[i]

      if line[0] == "$":  # executing my command
        if line == "$ ls":
          pass  # listing directories
        else:
          # moving to a different directory
          if line == "$ cd /":
            current_node = self.root
          elif line == "$ cd ..":
            current_node = current_node.parent or self.root
          else:
            current_node = current_node.find_child_by_value(line[5:])
      else:  # computer command
        if line[0:3] == "dir":
          current_node.add_child(line[4:])
        else:
          # files with size
          file_size, file_name = line.split(" ")
          current_node.add_file(file_name, int(file_size))

    return self


  def directory_list(self):
    directories = []
    self.directory_list_iterator(self.root, directories)

    return directories


  def directory_list_iterator(self, node, directories):
    directories.append(node)

    for child in node.children:
      self.directory_list_iterator(child, directories)


def solve_second(lines):
  directory_tree = DirectoryTree().build(lines)
  total_space = 70000000
  unused_space_needed = 30000000
  total_used_space = directory_tree.root.total_dir_size()
  diff = unused_space_needed - (total_space - total_used_space)


  directories = directory_tree.directory_list()

  smallest_dir_value = float('inf')

  for dir in directories:
    dir_size = dir.total_dir_size()

    if dir_size >= diff and dir_size <= smallest_dir_value:
      smallest_dir_value = dir_size

  return smallest_dir_value


def solve_first(lines):
  directory_tree = DirectoryTree().build(lines)
  max_dir_size = 100000

  directories = directory_tree.directory_list()

  total_sum = 0

  for dir in directories:
    dir_size = dir.total_dir_size()
    if dir_size <= max_dir_size:
      total_sum += dir_size

  return total_sum


if __name__ == '__main__':
  f = open('inputs/day_7_1.txt')
  raw_input = f.read()

  lines = list(raw_input.splitlines())

  print(solve_first(lines))
  print(solve_second(lines))
