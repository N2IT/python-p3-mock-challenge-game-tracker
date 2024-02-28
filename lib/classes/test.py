from many_to_many import Game
from many_to_many import Player
from many_to_many import Result

g = Game("Mega Awesome Game")
p = Player("Travis")

result = Result(p, g, 2200)

print(result)