def solve(input, length):
  processed_chars = 0

  for i in range(len(input) - length):
    processed_chars += 1
    is_unique = len(set(input[i:i+length])) == len(input[i:i+length])

    if is_unique:
      processed_chars += length - 1
      break

  return processed_chars

def solve_second(input):
  return solve(input, 14)


def solve_first(input):
  return solve(input, 4)


if __name__ == '__main__':
  f = open('inputs/day_6_1.txt')
  raw_input = f.read()

  print(solve_first(raw_input))
  print(solve_second(raw_input))
