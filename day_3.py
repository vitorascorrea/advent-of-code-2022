def solve_second(lines):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabet_priorities = {y: x + 1 for x, y in enumerate(alphabet)}
  sum_priorities = 0

  for i in range(0, len(lines) - 2, 3):
    first_sack_dict = {x: 0 for x in lines[i]}

    for c in lines[i + 1]:
      if c in first_sack_dict and first_sack_dict[c] == 0:
        first_sack_dict[c] += 1

    for c in lines[i + 2]:
      if c in first_sack_dict and first_sack_dict[c] == 1:
        first_sack_dict[c] += 1

    for c, v in first_sack_dict.items():
        if v == 2:
          sum_priorities += alphabet_priorities[c]

  return sum_priorities

def solve_first(lines):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabet_priorities = {y: x + 1 for x, y in enumerate(alphabet)}
  sum_priorities = 0

  for rucksack in lines:
    first_half = rucksack[:len(rucksack)//2]
    second_half = rucksack[len(rucksack)//2:]
    first_half_dict = {x: False for x in first_half}

    for c in second_half:
      if c in first_half_dict:
        first_half_dict[c] = True

    for c, v in first_half_dict.items():
      if v:
        sum_priorities += alphabet_priorities[c]

  return sum_priorities




if __name__ == '__main__':
  f = open('inputs/day_3_1.txt')
  raw_input = f.read()

  lines = list(raw_input.splitlines())

  print(solve_first(lines))
  print(solve_second(lines))
