from src.cli import welcome
from src.games.lcm_game import lcm_alg
from src.games.progression_game import progression

user_name = welcome()
game_num = int(
    input("What game do you like to play? LCM or Progression? Write '1' to play LCM or '2' to play Progression"))
if game_num == 1:
    lcm_alg(user_name)
elif game_num == 2:
    progression(user_name)
