JudoMoves = ["Strike", "Block", "Throw"]

class Player:
	def __init__(self, playerName = "NoName"):
		self.score = 0
		self.move = None
		self.playerName = playerName
		
	def selectPlay(self, move):
		if not move in JudoMoves:
			raise Exception("Not a valid move")
		self.move = move
	
	def __str__(self):
		return self.playerName

class Judo:
	def __init__(self):
		self.winner = None
		
	def play(self, p1, p2):
		if p1.move is None:
		   raise Exception("No move found for p1")
		if p2.move is None:
		   raise Exception("No move found for p2")
				
		if p1.move == p2.move:
			self.winner = "Draw"
		else:
		
			# first entry is move to check,
			# second entry is move that it beats
			# third entry is move that loses to it
			moveMatrix = [["Strike", "Throw", "Block"],
						  ["Throw", "Block", "Strike"],
						  ["Block", "Strike", "Throw"]]		
			
			# check who wins
			for move, winningMove, losingMove in moveMatrix:
				if p1.move == move:
					if p2.move == winningMove:
						self.winner = p1
					elif p2.move == losingMove:
						self.winner = p2
					else:
						raise Exception("Not a valid move")
					
		
	def winner():
		return self.winner