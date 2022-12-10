def cycle_decreaser(cycle):
  if cycle >= 201:
    return 200
  if cycle >= 161:
    return 160
  if cycle >= 121:
    return 120
  if cycle >= 81:
    return 80
  if cycle >= 41:
    return 40
  return 0


def solve_second(lines):
  register_x = 1
  cycle_values = []
  cycle_pixels_draw = []
  instructions = [i for i in lines]
  cycles_processing = 0
  pending_value = None

  for cycle in range(1, 1000):
    cycle_values.append(register_x)

    cycle_crt_value = cycle - cycle_decreaser(cycle) - 1
    crt_range = [cycle_crt_value - 1, cycle_crt_value, cycle_crt_value + 1]

    if register_x in crt_range:
      cycle_pixels_draw.append("#")
    else:
      cycle_pixels_draw.append(".")

    # start of cycle
    if cycles_processing == 0 and len(instructions) > 0 and pending_value == None:
      # process instruction
      instruction = instructions.pop(0)

      if instruction == "noop":
        cycles_processing = 1
      else:
        pending_value = int(instruction.split(" ")[1])
        cycles_processing = 2

    # end of cycle
    if cycles_processing > 0:
      cycles_processing -= 1

    if cycles_processing == 0 and pending_value:
        register_x += pending_value
        pending_value = None

    # break condition
    if len(instructions) == 0 and cycles_processing == 0 and pending_value == None:
      break


  print("".join(cycle_pixels_draw[:40]))
  print("".join(cycle_pixels_draw[40:80]))
  print("".join(cycle_pixels_draw[80:120]))
  print("".join(cycle_pixels_draw[120:160]))
  print("".join(cycle_pixels_draw[160:200]))
  print("".join(cycle_pixels_draw[200:240]))

  return


def solve_first(lines):
  register_x = 1
  cycle_values = []
  instructions = [i for i in lines]
  cycles_processing = 0
  pending_value = None

  for cycle in range(1, 1000):
    cycle_values.append(register_x)

    # start of cycle
    if cycles_processing == 0 and len(instructions) > 0 and pending_value == None:
      # process instruction
      instruction = instructions.pop(0)

      if instruction == "noop":
        cycles_processing = 1
      else:
        pending_value = int(instruction.split(" ")[1])
        cycles_processing = 2

    # end of cycle
    if cycles_processing > 0:
      cycles_processing -= 1

    if cycles_processing == 0 and pending_value:
        register_x += pending_value
        pending_value = None

    # break condition
    if len(instructions) == 0 and cycles_processing == 0 and pending_value == None:
      break

  cycles = [20, 60, 100, 140, 180, 220]
  _sum =  0

  for cycle in cycles:
    cycle_value = cycle_values[cycle - 1]
    signal_strength = cycle * cycle_value
    _sum += signal_strength

  return _sum


if __name__ == '__main__':
  f = open('inputs/day_10_1.txt')
  raw_input = f.read()

  lines = list(raw_input.splitlines())

  print(solve_first(lines))
  print(solve_second(lines))
