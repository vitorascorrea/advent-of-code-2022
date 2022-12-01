def build_elves_calories(lines):
  elves = []

  current_elf = 0
  for line in lines:
    if line == -1:
      elves.append(current_elf)
      current_elf = 0
    else:
      current_elf += line

  elves.sort()
  return elves

def solve_second(lines):
  elves = build_elves_calories(lines)

  return sum(elves[-3:])

def solve_first(lines):
  elves = build_elves_calories(lines)

  return elves[-1]


if __name__ == '__main__':
  f = open('inputs/day_1_1.txt')
  raw_input = f.read()

  lines = list(map(lambda x: int(x) if x else -1, raw_input.splitlines()))

  print(solve_first(lines))
  print(solve_second(lines))
