""" This defines the classes used in games of Dominion"""

# What to do next: Figure out __str__ methods for Collections of cards, Figure out how to structure gameplay (start coding game phases? figure out how to discard?)
import random
class Card():
	def __init__(self,Cost, Action=0,Treasure=0,Victory=0,Curse=0):
		""" Action, Treasure, and Victory are booleans that indicate the type of a card. Some cards can be multiple types, which is why they aren't exclusive.
		Cost is an non-negative integer indicating the cost of the card."""
		self.Action= Action
		self.Treasure=Treasure
		self.Victory=Victory
		self.Curse=Curse
		self.Cost=Cost 

	def playCard(self):
		# Removes Card from Hand such that its effect takes place
		pass



# This cards appear in every set, Copper, Silver, Gold; Estate, Duchy, Province; Curse
class Copper():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=0)
		self.Value = 1

	def __str__(self):
		return("Copper")

class Silver():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=3)
		self.Value = 2	

	def __str__(self):
		return("Silver")

class Gold():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=6)
		self.Value = 3	

	def __str__(self):
		return("Gold")


class Estate():
	def __init__(self):
		self.card=Card(Victory=1,Cost=2)
		self.Points = 1

	def __str__(self):
		return("Estate")

class Duchy():
	def __init__(self):
		self.card=Card(Victory=1,Cost=5)
		self.Points = 3

	def __str__(self):
		return("Duchy")

class Province():
	def __init__(self):
		self.card=Card(Victory=1,Cost=8)
		self.Points = 6

	def __str__(self):
		return("Province")


class Curse():
	def __init__(self):
		self.card=Card(Curse=1,Cost=0)
		self.Points = -1

	def __str__(self):
		return("Curse")

# Now I need a Deck, and in that, methods to draw cards, check the amount of cards left
class Deck():
	def __init__(self):
		# Initialized with 7 Coppers and 3 Estates in a random order
		# We play as if the last card in the list is on the top of the deck.
		self.ActualCards=[Copper(),Copper(),Copper(),Copper(),Copper(),Copper(),Copper(),Estate(),Estate(),Estate()]
		self.OutofPlay=[] #Cards that have been removed from the game (not trashed)
		random.shuffle(self.ActualCards)

	def __str__(self):
		shuffled = self.ActualCards[:]
		random.shuffle(shuffled)
		return("Working on it")

	def drawNewHand(self,amount):
		# Take an amount of cards from the deck, and put it in the player's hand
		newHand = draw(5,self.ActualCards)
		hand = Hand(newHand) # Could this cause errors with naming?
		return hand

class DiscardPile():
	def __init__(self):
		self.CardsDiscarded = []
		
# Next, we can make a list of Card instances that make up the hand. This will have methods associated with it as well
class Hand():
	def __init__(self,cardList):
		# To be filled in
		self.HandCards = cardList
	def __str__(self):
		# This will return the name of the cards in one's hand
		pass

class Game():
	def __init__(self,NumofPlayers):
		# A game is initialized with an integer amount of players, with each player receiving a deck of 10 cards
		pass


# General Methods For use by Deck, Hand, Trash, or any pile

def checkSize(listOfcards):
	# Check the amount of Cards in any collection of Cards (Deck,Pile, Hand, etc)
	return len(listOfcards)

def draw(amount,source):
	# Takes an amount of cards from the source, and moves it to the destination. This method is further extended in other classes
	cardsdrawn = []
	for i in range(amount):
		cardsdrawn.append(source.pop())
	return cardsdrawn



# Debugging
if __name__ == '__main__':
	print("Hello World!")
	deck1 = Deck()
	print(deck1)
	# print("Deck SIze: %s" %(checkSize(deck1.ActualCards)))
	# print("First Card: %s" %(deck1.ActualCards[-1]))
	# hand1 = deck1.draw(5)
	# print("Deck SIze: %s" %(checkSize(deck1.ActualCards)))
	# print("Hand SIze: %s" %(checkSize(hand1.HandCards)))
	# print("First Card: %s" %(deck1.ActualCards[-1]))