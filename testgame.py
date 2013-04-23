from judogame import *

Judo = Judo()
p1 = Player("Player 1")
p2 = Player("Player 2")

# draws

for move in ["Strike", "Block", "Throw"]:
	print ("P1 and P2 both playing %s" % move)
	p1.selectPlay(move)
	p2.selectPlay(move)
	Judo.play(p1, p2)

	assert Judo.winner == "Draw"

print ("\n")

# p1 wins
winningCombinations = [["Strike", "Throw"],
					   ["Throw", "Block"],
					   ["Block", "Strike"]]
for winMove, loseMove in winningCombinations:
	print ("P1 playing %s. P2 playing %s" % (p1.move, p2.move))

	p1.selectPlay(winMove)
	p2.selectPlay(loseMove)
	Judo.play(p1, p2)
	
	assert Judo.winner == p1
	print ("Winner is %s " % Judo.winner)

print ("\n")

# p2 wins
for winMove, loseMove in winningCombinations:
	print ("P1 playing %s. P2 playing %s" % (p1.move, p2.move))
	
	p1.selectPlay(loseMove)
	p2.selectPlay(winMove)
	Judo.play(p1, p2)
	
	assert Judo.winner == p2
	print ("Winner is %s " % Judo.winner)