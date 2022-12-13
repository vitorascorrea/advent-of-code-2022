def solve_second(pairs):
  result = []
  all_pairs = [
    [[2]],
    [[6]]
  ]

  for left, right in pairs:
    all_pairs.append(left)
    all_pairs.append(right)

  not_in_order = True

  while not_in_order:
    not_in_order = False

    for i in range(1, len(all_pairs)):
      left = all_pairs[i - 1]
      right = all_pairs[i]

      if not in_order(left, right):
        aux = all_pairs[i]
        all_pairs[i] = all_pairs[i - 1]
        all_pairs[i - 1] = aux
        not_in_order = True

  for i in range(len(all_pairs)):
    pair = all_pairs[i]
    if pair == [[2]] or pair == [[6]]:
      result.append(i + 1)

  return result[0] * result[1]


def solve_first(pairs):
  result = 0
  for i in range(len(pairs)):
    left, right = pairs[i]

    if in_order(left, right):
      result += i + 1

  return result


def in_order(left, right):
  bigger = left if len(left) > len(right) else right

  for i in range(len(bigger)):
    if len(left) == i:
      return True
    if len(right) == i:
      return False

    left_val = left[i]
    right_val = right[i]

    if type(left_val) == int and type(right_val) == int:
      if left_val < right_val:
        return True
      if left_val > right_val:
        return False

    decided = None
    if type(left_val) == list:
      if type(right_val) == list:
        decided = in_order(left_val, right_val)
      if type(right_val) == int:
        decided = in_order(left_val, [right_val])
    else:
      if type(right_val) == list:
        decided = in_order([left_val], right_val)

    if decided != None:
      return decided


if __name__ == '__main__':
  f = open('inputs/day_13_1.txt')
  raw_input = f.read()

  pairs = [(eval(pair.split("\n")[0]), eval(pair.split("\n")[1])) for pair in raw_input.split("\n\n")]

  print(solve_first(pairs))
  print(solve_second(pairs))
