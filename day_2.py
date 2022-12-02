POINTS_PER_TYPE = {
  "ROCK": 1,
  "PAPER": 2,
  "SCISSORS": 3,
}

ROCK_PAPER_SCISSORS_ENUM = {
  "A": "ROCK",
  "B": "PAPER",
  "C": "SCISSORS",
  "X": "ROCK",
  "Y": "PAPER",
  "Z": "SCISSORS",
}

STRATEGIES = {
    "ROCK": {
      "X": "SCISSORS",
      "Y": "ROCK",
      "Z": "PAPER"
    },
    "PAPER": {
        "X": "ROCK",
        "Y": "PAPER",
        "Z": "SCISSORS"
    },
    "SCISSORS": {
        "X": "PAPER",
        "Y": "SCISSORS",
        "Z": "ROCK"
    },
}

def resolve_match(player_a_move, player_b_move):
  if player_a_move == "ROCK":
    if player_b_move == "ROCK":
      return 3
    if player_b_move == "PAPER":
      return 0
    if player_b_move == "SCISSORS":
      return 6
  if player_a_move == "PAPER":
    if player_b_move == "ROCK":
      return 6
    if player_b_move == "PAPER":
      return 3
    if player_b_move == "SCISSORS":
      return 0
  if player_a_move == "SCISSORS":
    if player_b_move == "ROCK":
      return 0
    if player_b_move == "PAPER":
      return 6
    if player_b_move == "SCISSORS":
      return 3


def solve_second(lines):
  total_points = 0

  for opponent_move, player_move in lines:
    enum_opp_move = ROCK_PAPER_SCISSORS_ENUM[opponent_move]
    final_player_move = STRATEGIES[enum_opp_move][player_move]
    total_points += resolve_match(final_player_move, enum_opp_move) + POINTS_PER_TYPE[final_player_move]

  return total_points

def solve_first(lines):
  total_points = 0

  for opponent_move, player_move in lines:
    enum_opp_move = ROCK_PAPER_SCISSORS_ENUM[opponent_move]
    enum_player_move = ROCK_PAPER_SCISSORS_ENUM[player_move]
    total_points += resolve_match(enum_player_move, enum_opp_move) + POINTS_PER_TYPE[enum_player_move]

  return total_points


if __name__ == '__main__':
  f = open('inputs/day_2_1.txt')
  raw_input = f.read()

  lines = list(map(lambda x: [x[0], x[2]], raw_input.splitlines()))

  print(solve_first(lines))
  print(solve_second(lines))
