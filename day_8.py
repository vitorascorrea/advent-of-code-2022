def calculate_scenic_score(i, j, lines):
  current_tree = lines[i][j]

  # left view
  left_score = 0
  left_loop_broke = False
  for left_j in range(j - 1, -1, -1):
    tree = lines[i][left_j]
    left_score += 1
    if tree >= current_tree:
      left_loop_broke = True
      break

  # right view
  right_score = 0
  right_loop_broke = False
  for right_j in range(j + 1, len(lines[i])):
    tree = lines[i][right_j]
    right_score += 1
    if tree >= current_tree:
      right_loop_broke = True
      break

  column = [line[j] for line in lines]

  # top view
  top_score = 0
  top_loop_broke = False
  for top_i in range(i - 1, -1, -1):
    tree = lines[top_i][j]
    top_score += 1
    if tree >= current_tree:
      top_loop_broke = True
      break

  # bottom view
  bottom_score = 0
  bottom_loop_broke = False
  for bottom_i in range(i + 1, len(column)):
    tree = lines[bottom_i][j]
    bottom_score += 1
    if tree >= current_tree:
      bottom_loop_broke = True
      break

  visible_to_outside = (not left_loop_broke) or (not right_loop_broke) or (not top_loop_broke) or (not bottom_loop_broke)

  return left_score * right_score * top_score * bottom_score, visible_to_outside



def solve_second(lines):
  biggest_scenic_score = 0

  for i in range(len(lines)):
    for j in range(len(lines[i])):
      scenic_score, _ = calculate_scenic_score(i, j, lines)
      if scenic_score > biggest_scenic_score:
        biggest_scenic_score = scenic_score

  return biggest_scenic_score


def solve_first(lines):
  tree_count = 0

  for i in range(len(lines)):
    for j in range(len(lines[i])):
      _, visible_from_outside = calculate_scenic_score(i, j, lines)
      if visible_from_outside:
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
