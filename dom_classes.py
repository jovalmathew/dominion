""" This defines the classes used in games of Dominion"""

class Card():
	def __init__(self,Cost, Action=0,Treasure=0,Victory=0,Curse=0):
		""" Action, Treasure, and Victory are booleans that indicate the type of a card. Some cards can be multiple types, which is why they aren't exclusive.
		Cost is an non-negative integer indicating the cost of the card."""
		self.Action= Action
		self.Treasure=Treasure
		self.Victory=Victory
		self.Curse=Curse
		self.Cost=Cost 

	def playCard():
		# Removes Card from Hand such that its effect takes place, then goes to Discard Pile
		pass

	def Discard():
		# Removes Cards (a list of Card instances) from Hand and moves it to the Discard Pile
		pass

# This cards appear in every set, Copper, Silver, Gold; Estate, Duchy, Province; Curse
class Copper():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=0)
		self.Value = 1
class Silver():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=3)
		self.Value = 2	
class Gold():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=6)
		self.Value = 3	

class Estate():
	def __init__():
		self.card=Card(Victory=1,Cost=2)
		self.Points = 1
class Duchy():
	def __init__():
		self.card=Card(Victory=1,Cost=5)
		self.Points = 3
class Province():
	def __init__():
		self.card=Card(Victory=1,Cost=8)
		self.Points = 6

class Curse():
	def __init__():
		self.card=Card(Curse=1,Cost=0)
		self.Points = -1

# Now I need a Deck, and in that, methods to draw cards, check the amount of cards left
class Deck():
	def __init__(self):
		# To be filled in
		pass
	def draw(amount):
		# Take an amount of cards from the deck, and put it in the player's hand
		pass
	def checkDeckSize():
		# Check the amount of Cards in a Deck
		return len(Deck())


class DiscardPile():
	def __init__(self):
		# To be filled in 
		pass
# Next, we can make a list of Card instances that make up the hand. This will have methods associated with it as well
class Hand():
	def __init__(self):
		# To be filled in
		pass
class Game():
	def __init__(self):
		# A game is initialized with an integer amount of players, with each player receiving a deck of 10 cards
		pass

if __name__ == '__main__':
	print("Hello World!")