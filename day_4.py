def contains(range_1, range_2):
  start_1, end_1 = range_1
  start_2, end_2 = range_2

  # range 1 == range 2
  if start_1 == start_2 and end_1 == end_2:
    return True

  # range 1 contains range 2
  if start_1 <= start_2 and end_1 >= end_2:
    return True

  # range 2 contains range 1
  if start_2 <= start_1 and end_2 >= end_1:
    return True

  return False

def overlaps(range_1, range_2):
  start_1, end_1 = range_1
  start_2, end_2 = range_2

  # range 1 contains part of range 2
  # 1212, 1221, 2112, 2121
  if (start_1 <= start_2 and \
      end_1 >= start_2) or \
      (start_1 <= end_2 and \
      end_1 >= end_2):
    return True

  # range 2 contains part of range 1
  if (start_2 <= start_1 and \
      end_2 >= start_1) or \
      (start_2 <= end_1 and \
      end_2 >= end_1):
    return True

  return False

def solve_second(lines):
  sum_pairs = 0
  for range_1, range_2 in lines:
    if overlaps(range_1, range_2):
      sum_pairs += 1

  return sum_pairs

def solve_first(lines):
  sum_pairs = 0
  for range_1, range_2 in lines:
    if contains(range_1, range_2):
      sum_pairs += 1

  return sum_pairs


def process_line(line):
  result = []
  splitted = line.split(",")
  for range in splitted:
    result.append(list(map(int, range.split("-"))))

  return result

if __name__ == '__main__':
  f = open('inputs/day_4_1.txt')
  raw_input = f.read()

  lines = list(map(process_line, raw_input.splitlines()))

  print(solve_first(lines))
  print(solve_second(lines))
