from math import lcm


class Monkey:
  @classmethod
  def build(cls, blueprint):
    lines = blueprint.splitlines()
    id = int(lines[0].split(" ")[1].split(":")[0])
    items = list(map(int, lines[1].split(": ")[1].split(", ")))
    operation = lines[2].split("new = ")[1]
    test_value = int(lines[3].split(" by ")[1])
    target_monkey_true = int(lines[4].split("monkey ")[1])
    target_monkey_false = int(lines[5].split("monkey ")[1])

    return Monkey(
      id, items, operation, test_value, target_monkey_true, target_monkey_false
    )


  def __init__(self, id, items, operation, test_value, target_monkey_true, target_monkey_false) -> None:
    self.id = id
    self.items = items
    self.operation = operation
    self.test_value = test_value
    self.target_monkey_true = target_monkey_true
    self.target_monkey_false = target_monkey_false
    self.inspected_items = 0


  def inspect(self, item):
    self.inspected_items += 1
    operation = self.operation.replace("old", str(item))
    return eval(operation)


  def test_target_monkey(self, worry_value):
    if worry_value % self.test_value == 0:
      return self.target_monkey_true
    else:
      return self.target_monkey_false


class Game:
  def __init__(self, monkeys) -> None:
    self.monkeys = monkeys
    self.lcm_value = lcm(*[monkey.test_value for monkey in self.monkeys])


  def round(self, use_lcm = False):
    for monkey in self.monkeys:
      while len(monkey.items) > 0:
        item = monkey.items.pop(0)
        value = monkey.inspect(item)

        if use_lcm:
          new_item_value = value % self.lcm_value
        else:
          new_item_value = value // 3

        target_monkey_id = monkey.test_target_monkey(new_item_value)
        target_monkey = self.get_monkey_by_id(target_monkey_id)
        target_monkey.items.append(new_item_value)


  def get_monkey_by_id(self, id):
    for monkey in self.monkeys:
      if monkey.id == id:
        return monkey


  def print_state(self):
    for monkey in self.monkeys:
      print("Monkey {} {}: inspected {} times".format(monkey.id, monkey.items, monkey.inspected_items))


def solve_second(blueprints):
  monkeys = []

  for blueprint in blueprints:
    monkeys.append(Monkey.build(blueprint))

  game = Game(monkeys)

  for i in range(1, 10001):
    game.round(use_lcm=True)

  sorted_inspected_values = list(reversed(list(sorted(list(map(lambda x: x.inspected_items, game.monkeys))))))

  return sorted_inspected_values[0] * sorted_inspected_values[1]


def solve_first(blueprints):
  monkeys = []

  for blueprint in blueprints:
    monkeys.append(Monkey.build(blueprint))

  game = Game(monkeys)

  for _ in range(20):
    game.round()

  sorted_inspected_values = list(reversed(list(sorted(list(map(lambda x: x.inspected_items, game.monkeys))))))

  return sorted_inspected_values[0] * sorted_inspected_values[1]


if __name__ == '__main__':
  f = open('inputs/day_11_1.txt')
  raw_input = f.read()

  blueprints = list(raw_input.split("\n\n"))

  print(solve_first(blueprints))
  print(solve_second(blueprints))
