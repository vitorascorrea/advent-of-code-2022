def calculate_scenic_score(i, j, lines):
  current_tree = lines[i][j]

  # left view
  left_score = 0
  for left_j in range(j - 1, -1, -1):
    tree = lines[i][left_j]
    left_score += 1
    if tree >= current_tree:
      break

  # right view
  right_score = 0
  for right_j in range(j + 1, len(lines[i])):
    tree = lines[i][right_j]
    right_score += 1
    if tree >= current_tree:
      break

  column = [line[j] for line in lines]

  # top view
  top_score = 0
  for top_i in range(i - 1, -1, -1):
    tree = lines[top_i][j]
    top_score += 1
    if tree >= current_tree:
      break

  # bottom view
  bottom_score = 0
  for bottom_i in range(i + 1, len(column)):
    tree = lines[bottom_i][j]
    bottom_score += 1
    if tree >= current_tree:
      break

  return left_score * right_score * top_score * bottom_score


def solve_second(lines):
  biggest_scenic_score = 0

  for i in range(len(lines)):
    for j in range(len(lines[i])):
      scenic_score = calculate_scenic_score(i, j, lines)
      if scenic_score > biggest_scenic_score:
        biggest_scenic_score = scenic_score

  return biggest_scenic_score


def solve_first(lines):
  tree_map = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]

  # left to right
  for i in range(len(lines)):
    biggest_tree_before = -1
    for j in range(len(lines[i])):
      visible = lines[i][j] > biggest_tree_before
      tree_map[i][j] = visible
      if lines[i][j] > biggest_tree_before:
        biggest_tree_before = lines[i][j]

  # right to left
  for i in range(len(lines)):
    biggest_tree_before = -1
    for j in range(len(lines[i]) - 1, -1, -1):
      visible = lines[i][j] > biggest_tree_before
      tree_map[i][j] = tree_map[i][j] or visible
      if lines[i][j] > biggest_tree_before:
        biggest_tree_before = lines[i][j]

  # top to bottom
  transposed_lines = transpose(lines)
  for i in range(len(transposed_lines)):
    biggest_tree_before = -1
    for j in range(len(transposed_lines[i])):
      visible = transposed_lines[i][j] > biggest_tree_before
      tree_map[j][i] = tree_map[j][i] or visible
      if transposed_lines[i][j] > biggest_tree_before:
        biggest_tree_before = transposed_lines[i][j]

  # bottom to top
  transposed_lines = transpose(lines)
  for i in range(len(transposed_lines)):
    biggest_tree_before = -1
    for j in range(len(transposed_lines[i]) - 1, -1, -1):
      visible = transposed_lines[i][j] > biggest_tree_before
      tree_map[j][i] = tree_map[j][i] or visible
      if transposed_lines[i][j] > biggest_tree_before:
        biggest_tree_before = transposed_lines[i][j]

  tree_count = 0
  for row in tree_map:
    for tree in row:
      if tree:
        tree_count += 1

  return tree_count


def transpose(matrix):
  return [list(x) for x in zip(*matrix)]


if __name__ == '__main__':
  f = open('inputs/day_8_1.txt')
  raw_input = f.read()

  lines = [list(map(int, line)) for line in list(raw_input.splitlines())]

  print(solve_first(lines))
  print(solve_second(lines))
