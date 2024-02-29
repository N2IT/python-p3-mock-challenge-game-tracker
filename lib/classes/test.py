from many_to_many import Game
from many_to_many import Player
from many_to_many import Result

g = Game("Mega Awesome Game")
g1 = Game("EA FC 24")
g2 = Game("Chess")
p = Player("Travis")
p1 = Player("Xaviman")
p2 = Player("Tony")

p1_g2 = Result(p1, g2, 45000)
p_g = Result(p, g, 2200)
p2_g = Result(p2, g, 2205)
p_g2 = Result(p, g2, 45005)
p1_g1 = Result(p1, g1, 35000)
p2_g2 = Result(p2, g2, 45010)

# print(Result.all[0].game.title)
print(g2.average_score(p1))


    