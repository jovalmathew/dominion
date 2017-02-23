#!/usr/bin/env python3

# C:\Users\Owner\AppData\Local\Programs\Python\Python35-32\python.exe C:\Users\Owner\Documents\Github\dominion\dom_classes.py 
""" This defines the classes used in games of Dominion
	We will use a list for everything, except for cards that have effects. 
	These cards will call a dictionary from the base set, in which the effects will be called."""

# What to do next: Create a visualization for Kingdom Cards and their costs. Implement Action Cards!!!!
# Make sure that I know where we're drawing from and keep that consistent.
# implement a time limit

import random
from collections import Counter # This is a dictionary that can be added with other dictionaries
from baseset import *

# The value of these dictionaries is a TUPLE (act_tup, treas_tup, vict_tup, curse_tup, cost_tup), which represents 
# (Action, Treasure, Victory, Curse, Cost, Number in Supply Piles).  The treasure and victory components can be greater than one,
# which represents their value. the Cost components represents how much they cost to buy. 
act_tup = 0
treas_tup = 1
vict_tup = 2
curse_tup = 3
cost_tup = 4
supply_tup = 5
common_cards = {'Copper':(0,1,0,0,0,60),'Silver':(0,2,0,0,3,40),'Gold':(0,3,0,0,6,30),'Estate':(0,0,1,0,2,8),'Duchy':(0,0,3,0,5,8),'Province':(0,0,6,0,8,8),'Curse':(0,0,0,1,0,10)}

		
# Next, we can make a list of Card instances that make up the hand. This will have methods associated with it as well
class Hand():
	def __init__(self,cardList):
		# To be filled in
		self.HandCards = cardList
	def __str__(self):
		# This will return the name of the cards in one's hand
		return str(self.HandCards)
	def __iter__(self):
		return iter(self.HandCards)


class Player():
	# Each Player is initialized with a standard Deck
	def __init__(self,ID):
		self.PlayerID = ID
		self.Deck = ['Copper','Copper','Copper','Copper','Copper',
					'Copper','Copper','Estate','Estate','Estate'] 
		random.shuffle(self.Deck)
		self.Discard = []
		self.InPlay = []		# When Cards are played out of the hand, they are placed here, then moved to Discard at the end of the turn
		self.Hand = self.draw_hand()


		# self.name=""
	def __str__(self):
		return("Player%s" %(self.PlayerID))

	def draw_hand(self):
		# Take an amount of cards from the deck, and put it in the player's hand
		# Shuffle discard pile into deck if there are no cards left.
		if len(self.Deck)<5:
			# This is much too long and cumbersome
			len_mod = 5 - len(self.Deck)%5
			newHand_1 = move_cards(len(self.Deck),self.Deck)
			# print("not enough cards!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			self.Deck = list(self.Discard)
			random.shuffle(self.Deck)
			self.Discard = []
			newHand_2 = move_cards(len_mod,self.Deck)
			newHand = newHand_1+newHand_2
		else:
			newHand = move_cards(5,self.Deck)
		return newHand


	def put_in_play(self,card_index, source):
		# card_name must be a string that exists as a key in the cards dictionary
		# source must be a list

		# move card to InPlay list
		self.InPlay.append(source.pop(card_index))

# Game Hierarchy
# We can instantiate an instance of Game() to start playing. THis creates a deck for all players, randomizes the set of Action cards, designates 
# a player to go first. 
class Game():

		 

	def __init__(self,NumofPlayers):
		# A game is initialized with an integer amount of players, with each player receiving a deck of 10 cards
		# self.PlayerList= []
		# self.PlayerName = ""
		self.Players = [Player(i) for i in range(NumofPlayers)]
		self.Trash = []
		#### Figure out the Kingdom cards for use this game, and create the supply piles. Also add the kingdom cards to the common_cards dictionary

		kingdom_cards = dict(random.sample(list(base_set.items()),10)) # This takes 10 random cards from the base_set, puts them in the new dictionary kingdom_cards
		common_cards.update(kingdom_cards) # This adds the newly minted kingdom cards to the game.

		common_list = list(common_cards.items())
		supply_keys = [i[0] for i in common_list]
		supply_vals = [i[1][supply_tup] for i in common_list]

		self.Supply = dict(zip(supply_keys, supply_vals)) # This creates the supply piles!
		# Subtract out Coppers and add Victories if need be. 
		self.Supply['Copper'] -= 7*NumofPlayers



# General Functions for use by Deck, Hand, Trash, or any pile

def checkSize(listOfcards):
	# Check the amount of Cards in any collection of Cards (Deck,Pile, Hand, etc)
	return len(listOfcards)

def move_cards(amount,source):
	# Pop, with no index, defaults to taking the last item out of the list
	# Takes an amount of cards from the source, and moves it to the destination. This method is further extended in other classes
	cardsdrawn = []
	if amount == 0: # Return nothing if we are told to draw no cards
		return cardsdrawn

	for i in range(amount):
		cardsdrawn.append(source.pop())
	return cardsdrawn

def discard_all(source, destination):
	# Both destination and source must be lists
	destination+=source
	source = []

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
	# Check a action_count counter to see how many Actions can be played, decrement this counter if an Action is played, 
	# increment it if the card increases the amount of actions the player has.
	# This needs a way to play cards that the player chooses, and a way to implement their effects. The played cards also need to 
	# be placed in a location where they can be moved to the discard pile at the end of the turn. 
	# While action_count, allow Actions to be played 
	curr_hand = curr_game.Players[currentPlayer].Hand # will change later
	action_count = 1
	effect = Counter({'Actions':1, 'Buys':1, 'Money':0})
	while action_count:
		cont =input("Would you like to play an Action? y/n: ")
		#if cont, execute loop, else break. 
		if cont == 'n': 
			effect['Actions'] = 0
			return effect

		cardtoplay = input("What action will you play? : ")

		cardtoplay = cardtoplay.title()
		# Check if input card exists in hand ([x.lower() for x in curr_hand])
		if cardtoplay in curr_hand:
			# Find the index
			cardindex = curr_hand.index(cardtoplay)

			# Check if the card is an action card
			if common_cards[curr_hand[cardindex]][act_tup]:
				# move card to in play
				curr_game.Players[currentPlayer].put_in_play(cardindex,curr_hand)
				# Call the effect of the card
				## This needs to be done next!!!!!!!!!!!!!!!
				return effect
			else:
				print("This card is not an Action card")
		else:	
			print("Card not in hand")
			continue

	return effect
def BuyPhase(effects_dictionary):
	# While CurrentPlayerBuys, allow Buys to be made
	curr_hand = curr_game.Players[currentPlayer].Hand # will change later
	buy_count = effects_dictionary.get("Buys", 1)	
	# Count the number of treasure in our hand. Add that up with the money from the dictionary. Allow gaining a card from the supply piles, 
	# subtract that cost from the available money. 
	total_money = effects_dictionary.get("Money",0)
	# print(curr_game.Supply)
	for i in curr_hand:
		total_money += common_cards[i][treas_tup]
	while buy_count:
		cont =input("Would you like to buy something? y/n : ")
		if cont == 'n': 
			buy_count = 0
			return
		else:
			cardtobuy = input("What would you like to buy? :")
			cardtobuy = cardtobuy.title()
			# check if card exists in supply pile, and if we have enough money. if so, Add it to discard, subtract cost from total_money
			if common_cards[cardtobuy][cost_tup]<=total_money and curr_game.Supply[cardtobuy]>0:
				curr_game.Players[currentPlayer].Discard.append(cardtobuy)	# Add Card to Discard Pile (make a gain function) 
				curr_game.Supply[cardtobuy] -= 1 							# Decrement Supply Pile
				total_money -= common_cards[cardtobuy][cost_tup] 			# Decrease money
				buy_count -=1  												# Decrease buys
				
			else: 
				print('You cannot buy this card')

	return 
def ResidualEffects():
	# This function will execute events that take place at the start of a players turn
	pass


def InitializeGame(numplayers):
	# This function will instantiate a Game() object, and Set up the basics of the game. When finished, it will
	# call CurrentplayerTurn
	global curr_game, currentPlayer, totalplayers

	totalplayers=numplayers

	curr_game = Game(numplayers)
	currentPlayer = 0

	# print(curr_game.Players[0].Deck)
	# for i in range(0,numplayers):
	# 	print(i)
	# 	curr_game.Players[i].Hand= curr_game.Players[i].draw_hand() # This calls the drawing far too much!

	CurrentplayerTurn(currentPlayer)

def CurrentplayerTurn(currentPlayer):
	# This will check the global variable for the current player, and go through the phases of the turn
	# any initial draws, then Action Phase, then Buy phase. After all of this, we can call EndofTurn(), 

	curr_hand = curr_game.Players[currentPlayer].Hand
	# print(currentPlayer)
	# print('This is the deck')
	# print(curr_game.Players[currentPlayer].Deck)
	# print("This is the hand")
	# print(curr_hand)
	# print("This is the Discard Pile")
	# print(curr_game.Players[currentPlayer].Discard)
	effect = ActionPhase()
	BuyPhase(effect)
	EndofTurn()
	pass

def EndofTurn():
	# Move played cards to a players discard pile, draw her a new hand, clean up all loose ends
	# change currentPlayer variable to the next player in the list (change a global variable?)
	# Check to see if end of game conditions are met. If so, call EndofGame, else call CurrentplayerTurn

	if list(curr_game.Supply.values()).count(0)>2 or ~curr_game.Supply['Province']==0:
		EndofGame()
	else: 
		global currentPlayer
		# Move everything to discard pile, draw new hand 
		# print('This is the Discard Pile')
		# print(curr_game.Players[currentPlayer].Discard)
		discard_all(curr_game.Players[currentPlayer].Hand, curr_game.Players[currentPlayer].Discard)
		discard_all(curr_game.Players[currentPlayer].InPlay, curr_game.Players[currentPlayer].Discard)

		# print('This is the new Discard Pile at the end of the turn')
		# print(curr_game.Players[currentPlayer].Discard)

		# print('This is the current deck')
		# print(curr_game.Players[currentPlayer].Deck)
		curr_game.Players[currentPlayer].Hand= curr_game.Players[currentPlayer].draw_hand()
		# print('This is the Deck after drawing')
		# print(curr_game.Players[currentPlayer].Deck)
		# Change Player
		currentPlayer= (currentPlayer+1)%totalplayers
		CurrentplayerTurn(currentPlayer)
	pass

def EndofGame():
	# If end conditions are met, this function will add up the Victory points of all the players, and declare 
	# the winner! After which it will ask the users to play again. If so, restart game, If not, exit

	pass


# Debugging
if __name__ == '__main__':

	numplayers = 2

	InitializeGame(numplayers)