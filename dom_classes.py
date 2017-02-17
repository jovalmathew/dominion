""" This defines the classes used in games of Dominion"""

# What to do next:  Write the Action and Buy Phases, How to Play a Card? Also write Initialize Function. How to populate Field with Supply Piles?
import random
# import baseset
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

	def __repr__(self):
		return("Copper")

class Silver():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=3)
		self.Value = 2	

	def __repr__(self):
		return("Silver")

class Gold():
	def __init__(self):
		self.card=Card(Treasure=1,Cost=6)
		self.Value = 3	

	def __repr__(self):
		return("Gold")


class Estate():
	def __init__(self):
		self.card=Card(Victory=1,Cost=2)
		self.Points = 1

	def __repr__(self):
		return("Estate")

class Duchy():
	def __init__(self):
		self.card=Card(Victory=1,Cost=5)
		self.Points = 3

	def __repr__(self):
		return("Duchy")

class Province():
	def __init__(self):
		self.card=Card(Victory=1,Cost=8)
		self.Points = 6

	def __repr__(self):
		return("Province")


class Curse():
	def __init__(self):
		self.card=Card(Curse=1,Cost=0)
		self.Points = -1

	def __repr__(self):
		return("Curse")

# Now I need a Deck, and in that, methods to draw cards, check the amount of cards left
class Deck():
	def __init__(self):
		# Initialized with 7 Coppers and 3 Estates in a random order
		# We play as if the last card in the list is on the top of the deck.
		self.ActualCards=[Copper(),Copper(),Copper(),Copper(),Copper(),Copper(),Copper(),Estate(),Estate(),Estate()]
		self.OutofPlay=[] #Cards that have been removed from the game (not trashed)
		random.shuffle(self.ActualCards)

	def __repr__(self):
		shuffled = self.ActualCards[:]
		random.shuffle(shuffled)
		return str(shuffled[:])

	def drawNewHand(self):
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
		return str(self.HandCards)


class Player():
	# Each Player is initialized with a standard Deck
	def __init__(self,ID):
		self.PlayerID = ID
		self.Deck = Deck()
		self.VictoryPoints = 0 
		# self.name=""
	def __str__(self):
		return("Player%s" %(self.PlayerID))

# Game Hierarchy
# We can instantiate an instance of Game() to start playing. THis creates a deck for all players, randomizes the set of Action cards, designates 
# a player to go first. 
class Game():
	def __init__(self,NumofPlayers):
		# A game is initialized with an integer amount of players, with each player receiving a deck of 10 cards
		# self.PlayerList= []
		# self.PlayerName = ""
		self.Players = [Player(i) for i in range(NumofPlayers)]


		# We can also come up with the randomized list of Actions used this game

class Field():
	# The field consists of everything common to both players, the 10 Action Cards, the Trash, Treasures and Victory Cards
	def __init__():
		# Initializing the field will create an empty trash, 10 Supply Piles, Victory Cards and Treasures
		self.Trash=[] 



# General Functions for use by Deck, Hand, Trash, or any pile

def checkSize(listOfcards):
	# Check the amount of Cards in any collection of Cards (Deck,Pile, Hand, etc)
	return len(listOfcards)

def draw(amount,source):
	# Takes an amount of cards from the source, and moves it to the destination. This method is further extended in other classes
	cardsdrawn = []
	for i in range(amount):
		cardsdrawn.append(source.pop())
	return cardsdrawn
def howmanyactions():
	# A Player can Call this to check how many actions she has left
	pass
def howmuchmoney():
	# A Player can Call this to check how much money she has left (after buying things)
	pass
def howmanybuys():
	# A Player can Call this to check how many buys she has left
	pass
	
# def decrement():
# 	# Decrement the amount of buys or actions a player has 
# 	pass

# Here, define the functions that will actually run the game
def ActionPhase():
	# Check a CurrentPlayerActions counter to see how many Actions can be played, decrement this counter if an Action is played, 
	# increment it if the card increases the amount of actions the player has.
	# This needs a way to play cards that the player chooses, and a way to implement their effects. The played cards also need to 
	# be placed in a location where they can be moved to the discard pile at the end of the turn. 
	# While CurrentPlayerActions, allow Actions to be played 
	pass
def BuyPhase():
	# While CurrentPlayerBuys, allow Buys to be made
	pass
def ResidualEffects():
	# This function will execute events that take place at the start of a players turn
	pass


def InitializeGame():
	# This function will instantiate a Game() object, and Set up the basics of the game. When finished, it will
	# call CurrentplayerTurn
	pass

def CurrentplayerTurn():
	# This will check the global variable for the current player, and go through the phases of the turn
	# any initial draws, then Action Phase, then Buy phase. After all of this, we can call EndofTurn(), 
	pass

def EndofTurn():
	# Move played cards to a players discard pile, draw her a new hand, clean up all loose ends
	# change currentPlayer variable to the next player in the list (change a global variable?)
	# Check to see if end of game conditions are met. If so, call EndofGame, else call CurrentplayerTurn

	pass

def EndofGame():
	# If end conditions are met, this function will add up the Victory points of all the players, and declare 
	# the winner! After which it will ask the users to play again. If so, restart game, If not, exit
	pass


# Debugging
if __name__ == '__main__':
	deck1 = Deck()
	print(deck1)
	game1 = Game(2)
	print('Cards in Player%s\'s Deck: %s' %(game1.Players[0].PlayerID+1, game1.Players[0].Deck.ActualCards)) # Incongruity in printing the deck
	game1.Players[0].hand1= game1.Players[0].Deck.drawNewHand()
	print('Cards in Player%s\'s hand: %s' %(game1.Players[0].PlayerID,game1.Players[0].hand1))