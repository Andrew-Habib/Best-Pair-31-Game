'''
Andrew Habib
16 October 2021
Best Pair 31 Program
'''
# From the tkinter library import the following modules to aid in creating a Graphical User Interface
# These modules enable one to create objects that may be used to formulate enhanced and essential features to create a functioning interface
from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry, messagebox, simpledialog, END

# From the PIL library, import Image and ImageTk for more options related to manipulating imagery
# Contains greater facilities that are not included in PhotoImage to help adjust image dimensions
from PIL import Image, ImageTk

# Andrew's Card Game Module that contains options to create and manipulate a card from a deck of cards
from card import Card

# Andrew's Card Game Module that contains options to create and manipulate a deck of cards containing card objects from the card class
from DeckOfCards import Deck

# Define a function that will be responsible for initializing basic game objects, variables, lists and other components whenever the game starts, during the game when new rounds must occur, and if the user would like to play again
def initializeObjects():

	# Declare the following variables, lists, and other components as global variables
	# They may be now accessed and manipulated within this function 
	global list2DCardsPlayer, list2DCardsBanker, deckOfCards, listPlayerCards
	global listBankerCards, indexPlayingCards
	global stage, bankerhand, playerhand, bottomRowIndex, readyForNextStage
	global highestCardPlayerS2, highestCardBankerS2, highestPlayerSuitS2, highestBankerSuitS2

	# Declare and (re)-initialize an intger variable that stores the current stage (Stage 1 is the first stage)
	stage = 1

	# Declare and (re)-initialize two integer variables containing the banker and player hands to 0 - The round or the game is over and therefore the hands need to be reset to start again from stage 1
	bankerhand, playerhand = 0, 0

	# Declare and (re)-initialize the bottom Row index to value of -1 (variable that will store which column we are in within the bottom row during stage 3)
	bottomRowIndex = -1

	# Declare and (re)-initialize a boolean variable to true that determines whether it is suitable to move on to the next stage yet
	readyForNextStage = True

	# Declare and (re)-initialize two jagged 2 Dimensional lists that will store the 6 labels containing images of the card objects of the player and the banker
	# Lists must be jagged and in the form of a triangle (Row 1: 1 column, Row 2: 2 columns, Row 3: 3 columns) since the game cards will be set up this way
	# Each row corresponds to each stage of the game 
	list2DCardsPlayer = [[] for row in range(3)]

	# Row 1: 1 Column: Initial None Value - Stage 1 - Best Section 
	list2DCardsPlayer[0] = [None] * 1

	# Row 2: 2 Columns: Initial None Values - Stage 2 - Pair Section 
	list2DCardsPlayer[1] = [None] * 2

	# Row 3: 3 Columns: Initial None Values - Stage 3 - 31 Section 
	list2DCardsPlayer[2] = [None] * 3

	# Same as above but for the banker's cards
	list2DCardsBanker = [[] for row in range(3)]
	list2DCardsBanker[0] = [None] * 1
	list2DCardsBanker[1] = [None] * 2
	list2DCardsBanker[2] = [None] * 3
	
	# Declare and initialize 4 integer variables that will store the highest card and the highest suits of the player and banker's first 3 cards
	# These variables will only come into play in the case of a tie after round 2 with 31 cards each
	# Therefore, if both players have exactly 31 cards after stage 2, the winner of the hand will be deteremined by the highest card or highest suit if they have tied high cards
	highestCardPlayerS2 = 0
	highestCardBankerS2 = 0
	highestPlayerSuitS2 = 0
	highestBankerSuitS2 = 0

	# Create a deck of cards object using the class created
	deckOfCards = Deck()

	# Using a class function within the deck module, generate the deck by actually replacing the empty initialized lists within the class with actual cards and back-sides
	deckOfCards._generateDeck()

	# Shuffle the generated deck of cards using a class function within the deck of cards module - Randomly re-arrange the cards within the deck
	deckOfCards.shuffleDeck()

	# Declare and intialize 2 empty lists that will contain the 6 playing card objects that the user (player) and the computer (banker) will play with during the current hand
	listPlayerCards = []
	listBankerCards = []

	# Declare and intialize an integer variable that will store the current index determining which card from the list of 6 playing cards are currently being used
	indexPlayingCards = 0

	# Iterate 12 times using a counted for-loop that will keep track of the number of iterations using a counter
	# Each iteration will add a card to the playing cards for one round (6 cards for the player and 6 cards for the banker)
	for counter in range(12):

		# Using a variable, store the card that will be dealt (Returns the first card within the shuffled deck - Takes card from the top)
		card = deckOfCards.dealCard()
		
		# Set the height of the current dealt card using the card class function to 160 pixels
		card.set_Height(160)

		# Set the width of the currently dealt card using the card class function to 112 pixels
		card.set_Width(112)

		# Using a variable, store the back of the current card - Technically the same card
		backCard = deckOfCards.getBackOfCard()

		# Set the height of the current back-card using the card class function to 160 pixels - Match the dimensions of the actual face-side
		backCard.set_Height(160)

		# Set the width of the current back-card using the card class function to 112 pixels - Match the dimensions of the actual face-side
		backCard.set_Width(112)

		# Check if the currently dealt card's value is greater than 10 and less than 14 - (Jack --> King)
		if card.get_Value() > 10 and card.get_Value() < 14:

			# Set the value of the currently dealt card to 10 (Every card equal to higher than 9 and less than ace should be worth 10 within this game)
			card.set_Value(10)

			# Set the corresponding back side of the card to the same value of 10 because they are technically the same card
			backCard.set_Value(10)

		# If not, check if the currently dealt card's value is equivalent to 14 (Check if it is an ace)
		elif card.get_Value() == 14:

			# Set the value of the currently dealt card to 11 (Ace is worth 11 hand points in this game)
			card.set_Value(11)

		# Check if the for-loop counter is less than or equal to 5 
		if counter <= 5:

			# Append a small list containing the dealt card and its correspondent back side to the player's list of playing cards
			# The first six iterations of the for loop should create the cards for the player
			listPlayerCards.append([card, backCard])

		# If not, check if the counter is greater than or equal to 6
		elif counter >= 6:
			# Append a small list containing the dealt card and its correspondent back side to the banker's list of playing cards
			# The last six iterations of the for loop should create the cards for the banker
			listBankerCards.append([card, backCard])

	# Will iterate through each item on the 2 dimensional labels list (Will contain the images of the playing cards) and Player cards list and to ensure all their events are being handled 

	# Using a counted for loop, iterate based on the number of rows within the 2 dimensional card labels list (length of 2D list card labels)
	for row in range(len(list2DCardsPlayer)):
		# Using a for loop, iterate based on the number of columns within each row of the 2 dimensional card labels list (length of 2D list card labels at each row index)
		for column in range(len(list2DCardsPlayer[row])):

			# Create a label object at the current row and column that will contain the image of the card for the player
			# Assign the image of the current label to the list of the player cards at the currently specified index 
			# The row of the list of playing card objects represents the current card that is being placed and the column represents that it is the back-side not the front that is being outputted
			list2DCardsPlayer[row][column] = Label(canvas, image=listPlayerCards[indexPlayingCards][1].get_Image())
			
			# Output the label using the place function and use the specific algorithms below to attain the x and the y position of each card based on row and column
			# The way the code is designed ensures that cards overlap and place in a pyramid shape
			list2DCardsPlayer[row][column].place(y=225 + list2DCardsPlayer[row][column].winfo_reqheight() // 2 * row, 
				x=((320 - list2DCardsPlayer[row][column].winfo_reqwidth() // 2) - list2DCardsPlayer[row][column].winfo_reqwidth() // 4 * (len(list2DCardsPlayer[row]) - 1)) + list2DCardsPlayer[row][column].winfo_reqwidth() // 2 * column)
			
			# Check if the current index of the playing card objects is less than 3 - Checking the first 2 rows of cards
			if indexPlayingCards < 3:
				# Algorithm below determines the highest card and suit within the first 3 of the player's cards in case a tie occurs later in the game
				# Check if the highest card in the player's deck is less than or equal to the rank of the list of player card's face-side at the current index
				if highestCardPlayerS2 <= listPlayerCards[indexPlayingCards][0].get_Rank():

					oldPlayerCard = highestCardPlayerS2

					# Assign the rank of the list of player cards at the current index to the highest player card variable as a new high card has been found
					highestCardPlayerS2 = listPlayerCards[indexPlayingCards][0].get_Rank()
				
					# Iterate through each suit item within the list of suit rankings (List contains the different card suits from least valuable to the most valuable)
					# Keep track of the index using the enumerate function as well
					for index, suit in enumerate(suitRankings):

						# Check if the current suit within the list of suits is equivalent to the suit of the list of player cards at the current index
						if suit == listPlayerCards[indexPlayingCards][0].get_Suit():

							# Check if the current index of the for loop is greater than the variable storing the value of the highest suit (Checking whether the current suit is the highest suit so far) and the old player card is equivalent to the current one
							# This ensures that the highest suit could be found among similar high cards 
							# Or check if the old player card value is less than the current one so that suit rank is determined only for the highest card
							# The higher the index, the higher the suit value
							if oldPlayerCard < highestCardPlayerS2 or (oldPlayerCard == highestCardPlayerS2 and index > highestPlayerSuitS2):

								# Update the highest suit variable to the value of the current index - New highest suit has been found
								highestPlayerSuitS2 = index

			# Increment the variable storing the current index of the playing cards by 1 to move onto the next card object image to outputted it next
			indexPlayingCards = indexPlayingCards + 1
			
			# Check if the playing cards index is equal to 6 - All 6 player cards have been displayed
			if indexPlayingCards == 6:

				# Re-initialize the integer variable for the index of playing cards to 0 so it may be used to iterate through the banker cards too
				indexPlayingCards = 0

	# Perform the same algorithms seen above for the player section for the banker labels and cards 
	for row in range(len(list2DCardsBanker)):
		for column in range(len(list2DCardsBanker[row])):
			list2DCardsBanker[row][column] = Label(canvas, image=listBankerCards[indexPlayingCards][1].get_Image())
			list2DCardsBanker[row][column].place(y=225 + list2DCardsBanker[row][column].winfo_reqheight() // 2 * row, 
				x=((670 - list2DCardsBanker[row][column].winfo_reqwidth() // 2) - list2DCardsBanker[row][column].winfo_reqwidth() // 4 * (len(list2DCardsBanker[row]) - 1)) + list2DCardsBanker[row][column].winfo_reqwidth() // 2 * column)
			if indexPlayingCards < 3:
				if highestCardBankerS2 <= listBankerCards[indexPlayingCards][0].get_Rank():
					oldBankerCard = highestCardBankerS2
					highestCardBankerS2 = listBankerCards[indexPlayingCards][0].get_Rank()
					for index, suit in enumerate(suitRankings):
						if suit == listBankerCards[indexPlayingCards][0].get_Suit():
							if oldBankerCard < highestCardBankerS2 or (oldBankerCard == highestCardBankerS2 and index > highestBankerSuitS2):
								highestBankerSuitS2 = index
			indexPlayingCards = indexPlayingCards + 1
			if indexPlayingCards == 6:
				indexPlayingCards = 0

	# Console Test --> Checking the highest cards and highest suits
	print("Check Rankings:", highestCardPlayerS2, highestPlayerSuitS2, highestCardBankerS2, highestBankerSuitS2)

	# Update and configure the stand button by changing its state to disabled	
	btnStand.config(state='disabled')

	# Update and configure the deal button by changing its state to normal
	btnDeal.config(state='normal')

	# Update and configure the canvas by changing the text of the message appearing at the bottom of the screen to "Click DEAL to begin!" - Default message
	canvas.itemconfig(message_output, text="Click DEAL to begin!")

	# Check if the player points and banker points are greater than 0 - Game has already started but the game components are still initialized
	if playerpoints > 0 or bankerpoints > 0:

		# Update and configure the betting entry widget by changing its state to normal
		entryBet.config(state='normal')

		# Delete all of the contents within the betting entry widget
		entryBet.delete(0, END)

		# Insert the number 0 into the entry Bet widget to signal to the user that new bets should be made for the new round
		entryBet.insert(0, "0")
		entryBet.select_range(0, END)

		# Update and configure the bet entry widget by changing its state to disabled
		entryBet.config(state='disabled')

	# Update and configure the canvas by changing the text of the player and banker hands and points to their most current values based on the current stance of the game
	canvas.itemconfig(playerhandtotal, text=str(playerhand))
	canvas.itemconfig(bankerhandtotal, text=str(bankerhand))
	canvas.itemconfig(playerscore, text=str(playerpoints))
	canvas.itemconfig(bankerscore, text=str(bankerpoints))
	
# Define a function that will handle the events that occur when the user clicks the deal button to deal cards
def dealingCards():

	# Declare the following variables as global variables 
	# They may now be accessed and manipulated within the function
	global listPlayingCards, playerhand, bankerhand, playerpoints, bankerpoints, suitRankings 
	global stage, playername, indexPlayingCards, readyForNextStage, listPlayerCards, listBankerCards, bottomRowIndex
	global highestCardPlayerS2, highestCardBankerS2, highestPlayerSuitS2, highestBankerSuitS2

	# Check if the stage is equivalent to 1 and the boolean variable storing whether or not the next stage may begin is equivalent to True
	# In stage 1, 1 card from the players cards and 1 from the banker's cards will be used and the highest card out of the two wins 1 point
	if stage == 1 and readyForNextStage == True:

		# Assign the variable determining whether or not the player wins the current stage to false as the player has not won yet
		playerWinStage = False

		# Re-initialize the current index of the playing cards 
		indexPlayingCards = 0
		
		# Update and configure the list of 2D player and banker card labels at the first indices by updating the images with the images of the corresponding card object images from the list of Cards from the Player and Banker lists 
		# The index 0 for the columns index suggests that the card should reveal its face-up card not its hidden back-card
		list2DCardsPlayer[0][0].config(image=listPlayerCards[indexPlayingCards][0].get_Image())
		list2DCardsBanker[0][0].config(image=listBankerCards[indexPlayingCards][0].get_Image())

		# Increment the player hand with the value of the most recently retrieved player card
		playerhand = playerhand + listPlayerCards[indexPlayingCards][0].get_Value()

		# Increment the banker hand with the value of the most recently retrieved banker card
		bankerhand = bankerhand + listBankerCards[indexPlayingCards][0].get_Value()

		# Console Test - Output hands and ranks
		print(playerhand, listPlayerCards[0][0].get_Rank(), bankerhand, listBankerCards[indexPlayingCards][0].get_Rank())

		# Check if the rank of the list of player cards at the face up card at the current index is higher than that of the banker's list of cards
		if listPlayerCards[indexPlayingCards][0].get_Rank() > listBankerCards[0][0].get_Rank():
			
			# Update the variable determining whether the player has won the stage to true - They have won since they have a higher card than the banker
			playerWinStage = True

		# If not, check if the rank of the current player card is less than the rank of the banker card
		elif listPlayerCards[indexPlayingCards][0].get_Rank() < listBankerCards[indexPlayingCards][0].get_Rank():
			
			# Do nothing - The value of the player win stage boolean will remain false as the banker has won
			pass

		# Otherwise, the ranks of both cards are equal in value and thereby the winner must be determined based on suit - Execute code below to find player with higher suit
		else:

			# Iterate throught the list of suits and keep track of the index as well using the enumerate function
			for index, suit in enumerate(suitRankings):

				# Check if the current suit within the list of suits is equivalent to the suit of the list of player cards at the current index
				if suit == listPlayerCards[indexPlayingCards][0].get_Suit():

					# Assign the variable containing the value of the suit of the player's card to the current index, the higher the index the higher the suit
					suitPersonRank = index

				# Perform the same algorithm above but with the banker's cards this time
				elif suit == listBankerCards[indexPlayingCards][0].get_Suit():
					suitBankerRank = index

			# Check if the suit rank of the highest player card is greater than the suit rank of the highest banker card 
			if suitPersonRank > suitBankerRank:

				# Make the player win stage boolean variable equal to true as the player has one by gaining the higher suit 
				playerWinStage = True	

			# Otherwise, check if the suit rank of the highest banker card is greater than the suit rank of the highest player card 	
			elif suitPersonRank < suitBankerRank:

				# Do nothing - The value of the player win stage boolean will remain false as the banker has won by attaining the higher suit
				pass

		# Check if the variable determining whether the player has won the stage is equivalent to true
		if playerWinStage == True:

			# Increment the number of player points by 1
			playerpoints = playerpoints + 1

			# Update and configure the canvas by changing the text of the message at the bottom of the screen to "{playername} wins 1 point!"
			canvas.itemconfig(message_output, text=str(playername) + " wins 1 point!")

		# If not, check if the variable determining whether the player has won the stage is equivalent to false
		elif playerWinStage == False:

			# Increment the number of banker points by 1
			bankerpoints = bankerpoints + 1

			# Update and configure the canvas by changing the text of the message at the bottom of the screen to "Banker wins 1 point!"
			canvas.itemconfig(message_output, text="Banker wins 1 point!")

		# Update and configure the canvas by changing the text of the player and banker hands and points to their most current values based on the current stance of the game
		canvas.itemconfig(playerhandtotal, text=str(playerhand))
		canvas.itemconfig(bankerhandtotal, text=str(bankerhand))
		canvas.itemconfig(playerscore, text=str(playerpoints))
		canvas.itemconfig(bankerscore, text=str(bankerpoints))
		
		# Update and configure the deal button by changing its state to disabled
		btnDeal.config(state='disabled')

		# Update and configure the betting entry widget by changing its state to normal
		entryBet.config(state='normal')

		# Update and configure the betting button by changing its state to normal
		btnBet.config(state='normal')

		# Increment the stage by 1 to move on to the next stage as the current stage has been completed
		stage = stage + 1

		# Set the boolean variable determining whether it is appropriate to start the next stage is equal to false
		readyForNextStage = False
		
	# Check if the stage is equivalent to 2 and the boolean variable storing whether or not the next stage may begin is equivalent to True
	# In stage 2, 2 cards from the players cards and 2 from the banker's cards will be used and the highest pair or card out of the two wins the number of wagered point	
	if stage == 2 and readyForNextStage == True:
		playerWinStage = False

		# Declare and initialize 4 empty lists that will store the player and banker stage two pair of cards values along with their suits 
		# Using the lists, the program may account for all possible senarios and fairly determine the winner of the stage
		listPairPlayerVals = []
		listPairBankerVals = []
		listPairPlayerSuits = []
		listPairBankerSuits = []

		# Set the index of the playing cards to 1 because the 1st card has already been played and we must start from the second to continue stage 2
		indexPlayingCards = 1

		# Using a for loop, iterate through every column within the second row of the card labels list (length of 2D list card labels at this row index)
		for column in range(len(list2DCardsPlayer[stage - 1])):

			# Update and configure the list of 2D player and banker card labels at the second row by updating the images with the images of the corresponding card object images from the list of Cards from the Player and Banker lists 
			# The index 0 for the columns index suggests that the card should reveal its face-up card not its hidden back-card - Flipping card over to deal
			list2DCardsPlayer[stage - 1][column].config(image=listPlayerCards[indexPlayingCards][0].get_Image())

			# Information regarding the card as seen below will be useful in the future when determining the winner based on the higher card or suit
			
			# Append the rank of the player's card being revealed currently
			listPairPlayerVals.append(listPlayerCards[indexPlayingCards][0].get_Rank())

			# Append the suit of the player's card being revealed currently
			listPairPlayerSuits.append(listPlayerCards[indexPlayingCards][0].get_Suit())

			# Increment the player hand value with the value of the player's card being revealed currently
			playerhand = playerhand + listPlayerCards[indexPlayingCards][0].get_Value()

			# Increment the index of playing cards by 1 to move on to displaying the next card within the row
			indexPlayingCards = indexPlayingCards + 1	

		# Perform the same algorithms seen above but for the banker's cards		
		indexPlayingCards = 1
		for column in range(len(list2DCardsBanker[stage - 1])):
			list2DCardsBanker[stage - 1][column].config(image=listBankerCards[indexPlayingCards][0].get_Image())
			listPairBankerVals.append(listBankerCards[indexPlayingCards][0].get_Rank())
			listPairBankerSuits.append(listBankerCards[indexPlayingCards][0].get_Suit())
			bankerhand = bankerhand + listBankerCards[indexPlayingCards][0].get_Value()
			indexPlayingCards = indexPlayingCards + 1	

		# Check if there are dublicates in the list of player values and no duplicates in the list of banker values
		if listPairPlayerVals.count(listPairPlayerVals[0]) > 1 and listPairBankerVals.count(listPairBankerVals[0]) <= 1:

			# Player win - Set the boolean variable storing whether the player won to true - Player's double beats Banker's single
			playerWinStage = True

			# Console Test - Case 1
			print("1")

		# If not, check if there ther are no duplicates in the list of player values and duplicates in the list of banker values
		elif listPairPlayerVals.count(listPairPlayerVals[0]) <= 1 and listPairBankerVals.count(listPairBankerVals[0]) > 1:

			# Console Test - Case 2
			print("2")

			# Do nothing since the banker will win and the player win stage variable is false by default - Banker double beats player single
			pass

		# If not, check if the highest value within the list of player values is greater than the highest value within the list of banker values 
		elif max(listPairPlayerVals) > max(listPairBankerVals):

			# Console Test - Case 3
			print("3")

			# Player win - Set the boolean variable storing whether the player won to true - Both cards have same number of high cards but the player has a higher high card
			playerWinStage = True

		# If not, check if the highest value within the list of Banker values is greater than the highest value within the list of player values
		elif max(listPairPlayerVals) < max(listPairBankerVals):

			# Console Test - Case 4
			print("4")

			# Do nothing since the banker will win and the player win stage variable is false by default - Both cards have same number of high cards but the banker has a higher high card
			pass

		# If not, check if the highest value within the list of player values is equivalent to the highest value within the list of banker values
		elif max(listPairPlayerVals) == max(listPairBankerVals):

			# Console Test - Case 5
			print("5")

			# Check if the value of the suit (Index) of the highest value player card is greater than the value of the suit (Index) of the highest value banker card
			if suitRankings.index(listPairPlayerSuits[listPairPlayerVals.index(max(listPairPlayerVals))]) > suitRankings.index(listPairBankerSuits[listPairBankerVals.index(max(listPairBankerVals))]):
				
				# Player win - Set the boolean variable storing whether the player won to true - Same high card but the player's high card has a higher suit than the banker
				playerWinStage == True

			# If not, check if the value of the suit (Index) of the highest value player card is less than the value of the suit (Index) of the highest value banker card
			elif suitRankings.index(listPairPlayerSuits[listPairPlayerVals.index(max(listPairPlayerVals))]) < suitRankings.index(listPairBankerSuits[listPairBankerVals.index(max(listPairBankerVals))]):
				
				# Do nothing since the banker will win and the player win stage variable is false by default - Same high card but the player's high card has a lower suit than the banker
				pass

		# Check if the boolean variable storing whether the player wins is equivalent to True (Player wins)
		if playerWinStage == True:

			# Increment the number of player points by the integer value of the bet wagered by the user in entry widget
			playerpoints = playerpoints + int(entryBet.get())

			# Update and configure the canvas by changing the message at the bottom of the screen to the player winning the points wagered
			canvas.itemconfig(message_output, text=str(playername) +  " wins " + entryBet.get() + " point(s)!")

		# If not, check if the boolean variable storing whether the player wins is equivalent to False (Banker wins)
		elif playerWinStage == False:

			# Increment the number of banker points by the integer value of the bet wagered by the user in entry widget
			bankerpoints = bankerpoints + int(entryBet.get())

			# Update and configure the canvas by changing the message at the bottom of the screen to the banker winning the points wagered
			canvas.itemconfig(message_output, text="Banker wins " + entryBet.get() + " point(s)!")

		
		# Update and configure the canvas by changing the text of the player and banker hands and points to their most current values based on the current stance of the game
		canvas.itemconfig(playerhandtotal, text=str(playerhand))
		canvas.itemconfig(bankerhandtotal, text=str(bankerhand))
		canvas.itemconfig(playerscore, text=str(playerpoints))
		canvas.itemconfig(bankerscore, text=str(bankerpoints))

		# Preparing components so that user can bet again for stage 3

		# Re-shuffle the deck of cards 
		deckOfCards.shuffleDeck()

		# Update and configure the deal button by changing its state to disabled
		btnDeal.config(state='disabled')
		
		# Update and configure the betting entry widget by changing its state to normal
		entryBet.config(state='normal')

		# Update and configure the betting button by changing its state to normal
		btnBet.config(state='normal')

		# Increment the stage variable by 1 to move on to the next stage
		stage = stage + 1

		# Make the variable storing whether it is appropriate to move on to the next to False (Stage 3 must not start yet before betting)
		readyForNextStage = False

		# Set the variables storing whether the banker or the player win a tie in the number of hand points to False so they may be initialized
		playerWinsTie = False
		bankerWinsTie = False

		# Check if both the player hand and the banker hand are equivalent to 31 before stage 3 even begins
		# 2 way win must not occur and winner should be determined based on high card or if not, suit rank
		if playerhand == 31 and bankerhand == 31:

			# Check if the highest card within player's revealed deck so far is greater than the highest card within the banker's revealed deck so far
			if highestCardPlayerS2 > highestCardBankerS2:

				# Player wins the tie - Set booleans of player wins tie to true but banker wins tie to false
				playerWinsTie = True
				bankerWinsTie = False

			# If not, check if the highest card within player's revealed deck so far is less than the highest card within the banker's revealed deck so far
			elif highestCardPlayerS2 < highestCardBankerS2:

				# Banker wins the tie - Set booleans of banker wins tie to true but player wins tie to false
				bankerWinsTie = True
				playerWinsTie = False

			# Otherwise, they both have the same ranking high card in which case, suit must come into play and the code below will be executed
			else:

				# Check if the highest card suit within player's revealed deck so far is greater than the highest card suit within the banker's revealed deck so far
				if highestPlayerSuitS2 > highestBankerSuitS2:

					# Player wins the tie - Set booleans of player wins tie to true but banker wins tie to false
					playerWinsTie = True
					bankerWinsTie = False

				# Otherwise, the highest card suit within player's revealed deck so far is less than the highest card suit within the banker's revealed deck so far so execute the code below
				else:

					# Banker wins the tie - Set booleans of banker wins tie to true but player wins tie to false
					bankerWinsTie = True
					playerWinsTie = False

		# Check if the player hand and the banker hand have gone over 31 before stage 3
		if playerhand > 31 and bankerhand > 31:

			# Update and configure the canvas by changing the text of the message at the bottom to inform the player that no one gets any points
			canvas.itemconfig(message_output, text="No one wins any points!")

			# Display a message box informing the user once again that no one wins or gets any points because both the player and the banker went over 31 points in stage 2
			messagebox.showinfo("No one wins",
			"No one wins because both the player and the banker went over 31 points in stage 2!")

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

		# If not, check if the player's hand is greater than 31 or the boolean variable determining whether the banker wins the tie is equivalent to True
		elif playerhand > 31 or bankerWinsTie == True:

			# Update and configure the canvas by changing the text of the message at the bottom to inform the player that the banker has won 2 points
			canvas.itemconfig(message_output, text="Banker wins 2 point(s)!")

			# Check if the player hand is greater than 31
			if playerhand > 31:

				# Display a message box that informs the player that they lose and the banker wins 2 points because they have gone over 31
				messagebox.showinfo("You lose",
				"Banker wins two (2) points because you have gone over 31!")

			# If not, check if the boolean variable determining whether the banker wins the tie is equivalent to True
			elif bankerWinsTie == True:

				# Display a message box that informs the player that they lose and the banker wins 2 points because they lost the tie breaker
				messagebox.showinfo("You lose",
					"Banker wins two (2) points because you lost the tie breaker!")

			# Increment the banker points by 2 since the banker wins two points in these cases
			bankerpoints = bankerpoints + 2

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

		# If not, check if the banker's hand is greater than 31 or the boolean variable determining whether the player wins the tie is equivalent to True
		elif bankerhand > 31 or playerWinsTie == True:

			# Update and configure the canvas by changing the text of the message at the bottom to inform the player that they have won 2 points
			canvas.itemconfig(message_output, text=str(playername) +  " wins 2 point(s)!")

			# Check if the banker hand is greater than 31
			if bankerhand > 31:

				# Display a message box that informs the player that they won 2 points because the banker has gone over 31
				messagebox.showinfo("You win",
					playername + " wins two (2) points because the banker has gone over 31!")

			# If not, check if the boolean variable determining whether the player wins the tie is equivalent to True
			elif playerWinsTie == True:

				# Display a message box that informs the player that they won 2 points because the banker lost the tie breaker
				messagebox.showinfo("You win",
					playername + " wins two (2) points because the banker has lost the tie breaker!")

			# Increment the player points by 2 since the player wins two points in these cases
			playerpoints = playerpoints + 2

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()	

		# If not, check if only the playerhand is equivalent to 31
		elif playerhand == 31:

			# Update and configure the canvas by changing the text of the message at the bottom to inform the player that they have won 2 points
			canvas.itemconfig(message_output, text=str(playername) +  " wins 2 point(s)!")

			# Display a message box that informs the player that they have won the hand
			messagebox.showinfo("Best-Pair-31", playername + " wins the hand!")

			# Increment the player points by 2 since the player wins in this case
			playerpoints = playerpoints + 2

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

		# If not, check if only the bankerhand is equivalent to 31
		elif bankerhand == 31:

			# Update and configure the canvas by changing the text of the message at the bottom to inform the player that the banker has won 2 points
			canvas.itemconfig(message_output, text="Banker wins 2 point(s)!")

			# Display a message box that informs the player that the banker has won the hand
			messagebox.showinfo("Best-Pair-31", "Banker wins the hand!")

			# Increment the banker points by 2 since the banker wins in this case
			bankerpoints = bankerpoints + 2

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

		# Set the bottom row index to -1 --> To be used in stage 3 to keep track of which of the three columns in the bottom row are being looked at
		bottomRowIndex = -1

	# Check if the stage is equivalent to 4 and the boolean variable storing whether or not the next stage may begin is equivalent to True
	# In stage 3, 3 cards from the players cards and 3 from the banker's cards will be used and the objective is to have a hand equivalent to 31 or closer than the banker's hand to 31
	if stage == 3 and readyForNextStage == True:

		# Increment the bottom Row index by 1 to move onto the next card label every time the user deals or to access the first card at the 0th index since the initial value is -1
		bottomRowIndex = bottomRowIndex + 1

		# Each time the user selects deal, each column within the last row of the player's deck will be revealled
		# Update and configure each column of the list of 2D card labels at the last row based on the current bottom row index by changing its image to reveal its face up card (column 0) but in accordance to the appropriate index	
		list2DCardsPlayer[2][bottomRowIndex].config(image=listPlayerCards[indexPlayingCards][0].get_Image())

		# Increment the player hand by the value of the of the list of player cards at the current index - Adding the card to the hand
		playerhand = playerhand + listPlayerCards[indexPlayingCards][0].get_Value()

		# Update and configure the canvas by changing the text containing the player hand value to the updated player hand value
		canvas.itemconfig(playerhandtotal, text=str(playerhand))

		# Increment the index playing cards integer variable by 1 to move onto the next card object
		indexPlayingCards = indexPlayingCards + 1

		# Check if the bottom row index is equivalent to 2 (The last column of the last row has been revealed)
		if bottomRowIndex == 2:

			# Update and configure the deal button by changing its state to disabled since the player has drawn all of their cards already and it is impossible to draw more
			btnDeal.config(state='disabled')

		# Check if the player hand is equivalent to 31
		if playerhand == 31:

			# Update and configure the canvas by changing the text of the message at the bottom to the player winning the number of wagered points
			canvas.itemconfig(message_output, text=str(playername) +  " wins " + entryBet.get() + " point(s)!")

			# Display a message box that informs the user that they have won the hand
			messagebox.showinfo("Best-Pair-31", playername + " wins the hand!")

			# Increment the number of player points by the integer value of the amount wagered in the betting entry widget
			playerpoints = playerpoints + int(entryBet.get())

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

		elif playerhand > 31:

			# Update and configure the canvas by changing the text of the message at the bottom to the banker winning the number of wagered points
			canvas.itemconfig(message_output, text="Banker wins " + entryBet.get() + " point(s)!")

			# Display a message box that informs the player that the benker has won the hand
			messagebox.showinfo("Best-Pair-31", "Banker wins the hand!")

			# Increment the number of banker points by the integer value of the amount wagered in the betting entry widget
			bankerpoints = bankerpoints + int(entryBet.get())

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

	# Check if after the completion of the most recent stage, either the number player points or banker points is greater than or equal to 11 (Win condition for the overall game)
	if playerpoints >= 11 or bankerpoints >= 11:

		# Check if the number of player points is greater than or equal to 11 (Player wins)
		if playerpoints >= 11:
			
			# Create a variable that stores the yes or no boolean answer determining whether the user would like to play again 
			# Display that the game is over and that the player has won along with the score
			playagain = messagebox.askyesno("Best-Pair-31", 
				message="GAME OVER!\n" + playername + " wins " + str(playerpoints) + "-" + str(bankerpoints) + "!\nWould you like to play again?")
		
		# If not, check if the number of banker points is greater than or equal to 11 (Banker wins)
		elif bankerpoints >= 11:

			# Create a variable that stores the yes or no boolean answer determining whether the user would like to play again 
			# Display that the game is over and that the banker has won along with the score
			playagain = messagebox.askyesno("Best-Pair-31", 
				message="GAME OVER!\nBanker wins " + str(bankerpoints) + "-" + str(playerpoints) + "!\nWould you like to play again?")	

		# Check if the boolean variable storing whether or not the user would like to play again is equivalent to True
		if playagain == True:

			# Reset the number of player and banker points to 0 to start a fresh new game
			playerpoints = 0
			bankerpoints = 0

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the betting entry widget by changing its state to normal
			entryBet.config(state='normal')

			# Delete all of the contents within the betting entry widget
			entryBet.delete(0, END)

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

		# If not, check if the boolean variable storing whether or not the user would like to play again is equivalent to False
		elif playagain == False:

			# Terminate the program
			exit()

# Define a function that will handle the events when the bet button is clicked - Handling validition of the entry and processing the bet
def userBetting():

	# Declare the following variables as global variables 
	# They may now be accessed and manipulated within the function
	global stage, playerpoints, readyForNextStage, bankerpoints
	
	# Check if the stage is equivalent to 2 or 3 (When betting is permitted)
	if stage == 2 or stage == 3:

		# Entry-Widget Error Handlers

		# Check if the contents of the betting entry widget are not digits
		if entryBet.get().isdigit() == False:

			# Display a message box error that warns the user that they must enter an integer
			messagebox.showerror("Error", "You must enter an integer!")

			# Return focus to the betting entry widget
			entryBet.focus()

			# Select and highlight all of the contents within the betting entry widget
			entryBet.select_range(0, END)

			# Update and configure the betting entry widget by changing the background colour to red (Dislay warning and incorrect input)
			entryBet.config(background='Red')

		# If not, check if the integer converted betting entry widget contents is less than 1 - Check if user entered a wager less than 1
		elif int(entryBet.get()) < 1:

			# Display a message box error that warns the user that they must enter a bet that is at least 1 point
			messagebox.showerror("Error", "You must bet at least (1) point!")

			# Return focus to the betting entry widget
			entryBet.focus()

			# Select and highlight all of the contents within the betting entry widget
			entryBet.select_range(0, END)

			# Update and configure the betting entry widget by changing the background colour to red (Dislay warning and incorrect input)
			entryBet.config(background='Red')

		# If not, check if the integer converted betting entry widget in addition to the player points is greater than 11 points (User cannot enter a bet that would result in their points greater than 11 if they win)
		elif int(entryBet.get()) + playerpoints > 11:

			# Display a message box error that warns the user that their bet must not exceed 11 points minus their play points
			messagebox.showerror("Error", "Your bet cannot exceed " + str(11 - playerpoints) + " point(s)!")

			# Return focus to the betting entry widget
			entryBet.focus()

			# Select and highlight all of the contents within the betting entry widget
			entryBet.select_range(0, END)

			# Update and configure the betting entry widget by changing the background colour to red (Dislay warning and incorrect input)
			entryBet.config(background='Red')
	
		# Otherwise, execute the code below
		else:

			# Update and configure the betting entry widget by changing the background colour to white 
			entryBet.config(background='White')

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the dealing button by changing its state to normal
			btnDeal.config(state='normal')

			# Update and configure the canvas by changing the text of the message at the bottom to a prompt telling the user to click deal
			canvas.itemconfig(message_output, text="Click DEAL!")

		# Check if the stage is equivalent to 3
		if stage == 3:

			# Update and configure the canvas by changing the text of the message at the bottom to a prompt telling the user to click deal or stand
			canvas.itemconfig(message_output, text="Click DEAL or STAND!")

			# Update and configure the stand button by changing its state to normal
			btnStand.config(state='normal')

		# Update the boolean variable storing whether the program is ready for the next stage to True
		readyForNextStage = True
	
def stand():

	# Declare the following variables as global variables 
	# They may now be accessed and manipulated within the function
	global indexPlayingCards, bottomRowIndex, list2DCardsBanker, bankerhand, playerhand, playerpoints, bankerpoints
	
	# Re-initialize and set the bottom row index to -1 --> To be used in stage 3 to keep track of which of the three columns in the bottom row are being looked at within the banker's deck
	bottomRowIndex = -1

	# Set the index of playing cards to 3 since cards 4th to 6th cards must be accessed since they are the bottom row cards
	indexPlayingCards = 3

	# Keep dealing the banker's cards while the banker's hand is less than or equal to the player's hand and the banker's hand is less than 31 and the bottom row index is less than 2 so it is not out of index
	while bankerhand <= playerhand and bankerhand < 31 and bottomRowIndex < 2:

		# Increment the bottom row index by 1 to move onto the next card label
		bottomRowIndex = bottomRowIndex + 1

		# Update and configure each column of the list of 2D card labels at the last row based on the current bottom row index by changing its image to reveal its face up card (column 0) but in accordance to the appropriate index
		list2DCardsBanker[2][bottomRowIndex].config(image=listBankerCards[indexPlayingCards][0].get_Image())

		# Increment the banker hand by the value of the of the list of banker cards at the current index - Adding the card to the hand
		bankerhand = bankerhand + listBankerCards[indexPlayingCards][0].get_Value()

		# Update and configure the canvas by changing the text of the banker hand to the updated banker hand value
		canvas.itemconfig(bankerhandtotal, text=str(bankerhand))

		# Increment the index playing cards by 1 to move onto the next card object in the list
		indexPlayingCards = indexPlayingCards + 1

	# Check if the bottom row index is equivalent to 2 and the banker hand is equivalent to the player hand and the banker hand is less than 31 (Player wins)
	if bottomRowIndex == 2 and bankerhand == playerhand and bankerhand < 31:

		# Update and configure the canvas by changing the text of the message at the bottom to the player winning the number of wagered points
		canvas.itemconfig(message_output, text=str(playername) +  " wins " + entryBet.get() + " point(s)!")

		# Display a message box that informs the user that they have won the hand
		messagebox.showinfo("Best-Pair-31", playername + " wins the hand!")

		# Increment the number of player points by the integer value of the amount wagered in the betting entry widget
		playerpoints = playerpoints + int(entryBet.get())

		# Make a call to the function responsible for declaring initializing basic game componenets and objects
		initializeObjects()
	
	# Check if either the banker hand is greater than the player hand and less than or equal to 31 or the banker hand is equivalent to 31 (Banker wins)
	if (bankerhand > playerhand and bankerhand <= 31) or bankerhand == 31:

		# Update and configure the canvas by changing the text of the message at the bottom to the banker winning the number of wagered points
		canvas.itemconfig(message_output, text="Banker wins " + entryBet.get() + " point(s)!")

		# Display a message box that informs the user that the banker has won the hand
		messagebox.showinfo("Best-Pair-31", "Banker wins the hand!")

		# Increment the number of banker points by the integer value of the amount wagered in the betting entry widget
		bankerpoints = bankerpoints + int(entryBet.get())

		# Update and configure the betting button by changing its state to disabled
		btnBet.config(state='disabled')

		# Update and configure the betting entry widget by changing its state to disabled
		entryBet.config(state='disabled')

		# Make a call to the function responsible for declaring initializing basic game componenets and objects
		initializeObjects()

	# Otherwise, execute the code below
	else:

		# Update and configure the canvas by changing the text of the message at the bottom to the player winning the points wagered
		canvas.itemconfig(message_output, text=str(playername) +  " wins " + entryBet.get() + " point(s)!")

		# Display a message box that informs the user that they have won the hand
		messagebox.showinfo("Best-Pair-31", playername + " wins the hand!")

		# Increment the number of player points by the integer value of the amount wagered in the betting entry widget
		playerpoints = playerpoints + int(entryBet.get())

		# Update and configure the betting button by changing its state to disabled
		btnBet.config(state='disabled')

		# Update and configure the betting entry widget by changing its state to disabled
		entryBet.config(state='disabled')

		# Make a call to the function responsible for declaring initializing basic game componenets and objects
		initializeObjects()
	
	# Check if after the completion of the most recent stage, either the number player points or banker points is greater than or equal to 11 (Win condition for the overall game)
	if playerpoints >= 11 or bankerpoints >= 11:

		# Check if the number of player points is greater than or equal to 11 (Player wins)
		if playerpoints >= 11:
			
			# Create a variable that stores the yes or no boolean answer determining whether the user would like to play again 
			# Display that the game is over and that the player has won along with the score
			playagain = messagebox.askyesno("Best-Pair-31", 
				message="GAME OVER!\n" + playername + " wins " + str(playerpoints) + "-" + str(bankerpoints) + "!\nWould you like to play again?")
		
		# If not, check if the number of banker points is greater than or equal to 11 (Banker wins)
		elif bankerpoints >= 11:

			# Create a variable that stores the yes or no boolean answer determining whether the user would like to play again 
			# Display that the game is over and that the banker has won along with the score
			playagain = messagebox.askyesno("Best-Pair-31", 
				message="GAME OVER!\nBanker wins " + str(bankerpoints) + "-" + str(playerpoints) + "!\nWould you like to play again?")	

		# Check if the boolean variable storing whether or not the user would like to play again is equivalent to True
		if playagain == True:

			# Reset the number of player and banker points to 0 to start a fresh new game
			playerpoints = 0
			bankerpoints = 0

			# Update and configure the betting button by changing its state to disabled
			btnBet.config(state='disabled')

			# Update and configure the betting entry widget by changing its state to normal
			entryBet.config(state='normal')

			# Delete all of the contents within the betting entry widget
			entryBet.delete(0, END)

			# Update and configure the betting entry widget by changing its state to disabled
			entryBet.config(state='disabled')

			# Make a call to the function responsible for declaring initializing basic game componenets and objects
			initializeObjects()

		# If not, check if the boolean variable storing whether or not the user would like to play again is equivalent to False
		elif playagain == False:

			# Terminate the program
			exit()


# Define a function that will close the program when the user clicks the close button at the top right of the screen or the exit button
def terminate_program():

    # Prompt the user through a messagebox verifying whether they would like to exit for sure
    # Store the yes or no answer in the following variable
    user_response = messagebox.askyesno("Best-Pair-31", 
        "Are you sure you want to exit?")

    # If the user's response is "yes", this indicates that the variable is equal to the boolean value of True in which case the code below will execute
    if user_response == True:

        # Terminate the program
        exit()

# Declare two constants resembling the width and the height of the Tk surface window (1000x677)
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 667

# Declare and intialize 5 integer variables storing the player and banker hands and points along with the current stage number
playerpoints, stage, bankerhand, playerhand,  bankerpoints = 0, 1, 0, 0, 0

# Declare and initialize an intger variable with the value -1 storing the current column of the last row of 3 cards of each deck
bottomRowIndex = -1

# Declare a list of suit ranking strings that display the first letter of each of the 4 card suits in order from least valuable to most valuable
suitRankings = ["S", "C", "H", "D"]

# Declare and initialize an empty string variable that will store the name of the user or player
playername = ""

# Declare and initialize a boolean variable whose current value is True determining whether the program is ready and it is appropriate to move onto the next stage
# This way the next stage does not begin right-away when the stage variable is incremented by 1 during the completion of the prior stage
readyForNextStage = True

# Create a Tk window that will display all objects for the graphical user interface
root = Tk()

# Set the name of the title of the Tk Window on the top left corner to "Best-Pair-31" (Name of the program)
root.title('Best-Pair-31')

# Set the size and location of the window using the contants declared above and formatting techniques
# The following properties ensure that the window is centered based on the properties of itself and the user's screen
root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, root.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2, 
	root.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2))

# Ensure that the user is unable to resize the Tk window in the x and the y directions
root.resizable(False, False)

# Call the function that terminates the program when the top right x button is clicked
root.protocol("WM_DELETE_WINDOW", terminate_program)

# Create a canvas object that will enable the programmer to add components on to the interface and draw other objects - Replicate the dimensions of the TK window
canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
# Output the canvas
canvas.pack()

# Create a PhotoImage object that contains the image file of the green logo png background image
imgTitle = PhotoImage(file='images/logo_green.png')

# Create a PhotoImage object that contains the image file of the card table png image
imgBackground = PhotoImage(file='images/card_table.png')

# Draw the background card table image on the canvas starting at the top left 
canvas.create_image(0, 0, image=imgBackground, anchor='nw')

# Draw the title image on the canvas near the top left of the screen
canvas.create_image(WINDOW_WIDTH // 2 - imgTitle.width() // 2, 10, image=imgTitle, anchor='nw')

# Hide and withdraw the main surface window so that only the simple dialogue box below could be seen
root.withdraw()

# Using a while conditional loop, repeat the code below while the playername is equivalent to None (Keys such as cancel or X have been clicked instead of ok) or player name is equivalent to "" (User has not entered a name in the dialogue box)
while playername == None or playername == "":

	# Create a simple dialogue box that takes a string, welcomes the user and prompts the user for their name to begin the game
	playername = simpledialog.askstring("Best-Pair-31", 
		"Welcome to Best-Pair-31!\nPlease enter your name:")

	# Check if the player name is equivalent to None (Keys such as cancel or X have been clicked instead of ok) or player name is equivalent to "" (User has not entered a name in the dialogue box)
	if playername == None or playername == "":

		# Display a message box error that warns the user that they must enter their name to proceed before iterating through the loop again
		messagebox.showerror("Error", "Please enter a name!")

# Return the main surface window and start the game
root.deiconify()

# Store in a variable the canvas drawn text for the subtitle for the player's hand and set its properties
playerhandoutput = canvas.create_text(320, 160, text=playername + '\'s hand:', 
	font=('Century Gothic', 16, 'bold'), fill='white', anchor='c')

# Store in a variable the canvas drawn text for the subtitle for the player's score and set its properties
playerscoreoutput = canvas.create_text(780, 240, text=playername + '\'s Score:', 
	font=('Century Gothic', 14, 'bold'), fill='white', anchor='w')

# Store in a variable the canvas drawn text for the actual player's score and set its properties
playerscore = canvas.create_text(960, 240, text='0', font=('Century Gothic', 14, 'bold'), 
	fill='white', anchor='c')

# Store in a variable the canvas drawn text for the actual player's hand and set its properties
playerhandtotal = canvas.create_text(320, 200, text='0', font=('Century Gothic', 16, 'bold'), 
	fill='white', anchor='c')

# Draw text on the canvas depicting the subtitle for the banker's hand and set the properties
canvas.create_text(670, 160, text='Banker\'s hand:', font=('Century Gothic', 16, 'bold'), 
	fill='white', anchor='c')

# Draw text on the canvas depicting the subtitle for the banker's score and set the properties
canvas.create_text(780, 275, text='Banker\'s Score:', font=('Century Gothic', 14, 'bold'), 
	fill='white', anchor='w')

# Store in a variable the canvas drawn text for the actual banker's score and set its properties
bankerscore = canvas.create_text(960, 275, text='0', font=('Century Gothic', 14, 'bold'), 
	fill='white', anchor='c')

# Store in a variable the canvas drawn text for the actual banker's hand and set its properties
bankerhandtotal = canvas.create_text(670, 200, text='0', font=('Century Gothic', 16, 'bold'), 
	fill='white', anchor='c')

# Create an entry widget that takes the bet of the user - Disabled since there is no betting on stage 1
entryBet = Entry(canvas, font=('Century Gothic', 12, 'bold'), justify='center', width=10, relief='sunken', state='disabled')
# Place the entry widget near the center of the interface below the main title and above main function buttons
entryBet.place(x=WINDOW_WIDTH // 2 - entryBet.winfo_reqwidth() // 2, y=190)

# Create a button object that will handle the events that occur when the user wants to place their bet --> Handles validation of user bet entries and processes bets - Starts disabled since no betting is done stage 1
btnBet = Button(canvas, text='BET', width=11, pady=4, font=('Century Gothic', 10), state='disabled', command=userBetting)
# Place the bet button object near the center of the interface above the deal button and under the betting entery widget
btnBet.place(x=WINDOW_WIDTH // 2 - btnBet.winfo_reqwidth() // 2, y=235)

# Create a button object that will handle the events that occur when the user wants to deal their cards and turn them face up
btnDeal = Button(canvas, text='DEAL', width=11, pady=4, font=('Century Gothic', 10), command=dealingCards)
# Place the deal button object near the center of interface under the bet button and above the stand button
btnDeal.place(x=WINDOW_WIDTH // 2 - btnDeal.winfo_reqwidth() // 2, y=280)

# Create a button object that will handle the events that occur when the user wants to stop dealing cards in the 3rd stage and the banker must deal their last 3 cards - Starts disabled since this only applies for stage 3
btnStand = Button(canvas, text='STAND', width=11, pady=4, font=('Century Gothic', 10), state='disabled', command=stand)
# Place the stand button object near the center of interface under the deal button and above the message output at the bottom
btnStand.place(x=WINDOW_WIDTH // 2 - btnStand.winfo_reqwidth() // 2, y=325)	

# Store in a variable the canvas drawn text for the informative messages for the user at the bottom of the screen 
message_output = canvas.create_text(WINDOW_WIDTH // 2, 600, text='Click DEAL to begin!', font=('Century Gothic', 16, 'bold'), fill='white', anchor='c')

# Make a call to the function responsible for declaring initializing basic game componenets and objects
initializeObjects()

# Main loop will listen for events triggered by the user and keep the program running
root.mainloop()