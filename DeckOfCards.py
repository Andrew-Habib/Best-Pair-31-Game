'''
Andrew Habib
16 October 2021
Best Pair 31 Program
Deck of Cards Module
'''

# From the tkinter library import the following modules to aid in creating a Graphical User Interface
# These modules enable one to create objects that may be used to formulate enhanced and essential features to create a functioning interface
# Only Import PhotoImage to aid in creating image objects that may be manipulated for visual aid for the user
from tkinter import PhotoImage

# Andrew's Card Game Module that contains options to create and manipulate a card from a deck of cards
from card import Card

# Import a module that adds more options for creating randomizing objects not included in python
import random

# From the PIL library, import Image and ImageTk for more options related to manipulating imagery
# Contains greater facilities that are not included in PhotoImage to help adjust image dimensions
from PIL import Image, ImageTk

# Formulate a class to be used to create a deck of cards using the cards class already created
class Deck:

    # Declare an initializing no-argument constructor - Creating the deck of cards object and initializing components
    def __init__(self):

        # Declare and initialize a private class list of 52 None values that will hold each card in the deck of cards
        self.__backOfCards = [None] * 52

        # Declare and initialize a private class variable containing None that will hold the current card dealt
        self.__dealtCard = None

        # Declare and initialize a private class list of 52 None values that will hold each card's backside in the deck
        self.__deck = [None] * 52

        # Declare and initialize a private class integer variable that will the number of cards that have already been dealt 
        self.__numCardsDealt = 0

        # Declare a private class integer variable that will contain the number of cards remaining in the deck after dealing
        self.__cardsRemaining = 52
        
    # Define a class level function that will generate the deck of cards
    # Replace the intialized none value lists with their correspondent card Image, Value, Suit, and Rank
    def _generateDeck(self):

        # Declare an integer variable that will contain an index value for when iterating through a list
        indexDeck = 0

        # Declare a 2 dimensional list containing 13 rows of the 4 different card suits
        list2DCardAbbrevs = [["C", "D", "H", "S"] for row in range(13)]
        
        # Will iterate through each item on the 2 dimensional list to ensure every card value of every suit is generated
        # Using a counted for loop, iterate based on the number of rows within the 2 dimensional list (length of 2D list)
        for row in range(len(list2DCardAbbrevs)):

            # Using a for loop, iterate based on the number of columns within each row of the 2 dimensional list (length of 2D list at each row index)
            for column in range(len(list2DCardAbbrevs[row])):

                # Create a card object at within the list of the deck of cards at the current deck index
                self.__deck[indexDeck] = Card()

                # Set the Image of the current card in the deck of cards to the image file of the current card value and suit according to the current position on the 2D list
                self.__deck[indexDeck].set_Image(Image.open("images/" + str(row + 2) + list2DCardAbbrevs[row][column] + ".png"))
                
                # Set the card value of the current card object in the deck of cards to the row number + 2 (Since the deck starts at the minimum number of 2 until ace)
                self.__deck[indexDeck].set_Value(row + 2)

                # Set the suit of the current card object in the deck of cards to the current index of the 2D list (Either "C"lubs, "D"iamonds, "H"earts, "S"pades) based on the current item on the 2D list
                self.__deck[indexDeck].set_Suit(list2DCardAbbrevs[row][column])
                
                # Set the rank of the current card object in the deck of cards to the current row + 2 (Same as with the default pre-set value)
                self.__deck[indexDeck].set_Rank(row + 2)
                
                # The back of the card object attributes should correspond with the values of the face up card as they are technically the same card
                # Create another card object within the list of the back of cards deck at the current deck index
                self.__backOfCards[indexDeck] = Card()

                # Set the Image of the current card in the deck of back-side cards to the image file of the blue colour back-side of card image png file
                self.__backOfCards[indexDeck].set_Image(Image.open("images/back_blue.png"))
                
                # Set the card value of the current card object in the back-side deck of cards to the row number + 2 (Since the deck starts at the minimum number of 2 until ace)
                self.__backOfCards[indexDeck].set_Value(row + 2)

                # Set the suit of the current card object in the back-side deck of cards to the current index of the 2D list (Either "C"lubs, "D"iamonds, "H"earts, "S"pades) based on the current item on the 2D list
                self.__backOfCards[indexDeck].set_Suit(list2DCardAbbrevs[row][column])

                # Set the rank of the current card object in the back-side deck of cards to the current row + 2 (Same as with the default pre-set value)
                self.__backOfCards[indexDeck].set_Rank(row + 2)

                # Increment the current index of the deck by 1 to move on to creating and setting the attributes of the next card in the order
                indexDeck = indexDeck + 1

    # Define a class function that will be responsible dealing or returning the card at the current index represented by the number of cards dealt class private variable and then incrementing this index by 1 incase the programmer wants to deal a new card later
    def dealCard(self):

        # Update the private class variable storing a card object to the card at the current index (based on number of cards dealt) of the private deck of cards list containing the full deck of cards
        self.__dealtCard = self.__deck[self.__numCardsDealt]

        # Increment the private class integer variable storing the number of cards dealt by 1 so that the next time the user deals a card, the next card within the deck will be returned
        self.__numCardsDealt = self.__numCardsDealt + 1

        # Return the private class variable storing the dealt card retrieved from the algorithm above
        return self.__dealtCard
    
    # Define a class function that returns the back of the previously dealt card
    def getBackOfCard(self):

        # Return the private class list of back-side cards at the index of the private class number of cards dealt - 1 to account for the incrementing that occurred in the deal card function
        # We are returning the back side of the very last card that was dealt
        return self.__backOfCards[self.__numCardsDealt - 1]

    # Mutator/Setter Method --> Returns Void --> Takes integer as parameter
    # Define a class level function that will set the number of cards remaining within the deck
    def setCardsRemaining(self, num):

        # Update the value of the private class integer variable for the number of cards remaining
        self.__cardsRemaining = num

    # Accessor/Getter Method --> Returns Integer --> Takes no parameters
    # Define a function that will return the private class integer variable for the number of cards remaining within the deck of cards
    def getCardsRemaining(self):

        # Return the private class integer variable containing the number of cards remaining within the deck of cards
        return self.__cardsRemaining

    # Mutator/Setter Method --> Returns Void --> Takes integer as parameter
    # Define a class level function that will set the number of cards dealt so far
    def setTotalCardsDealt(self, num):

        # Update the value of the private class integer containing the number of cards dealt so far
        self.__numCardsDealt = num

    # Accessor/Getter Method --> Returns Integer --> Takes no parameters
    # Define a function that will return the number of cards dealt so far
    def getTotalCardsDealt(self):

        # Return the private class integer variable containing the number of cards dealt so far
        return self.__numCardsDealt

    # Define a function that returns void but shuffles the deck of cards using the random.shuffle function
    def shuffleDeck(self):

        # Shuffle the deck of cards by randomizing the order of the list containing the deck of card objects
        random.shuffle(self.__deck)

# from tkinter import PhotoImage
# from card import Card
# import random

# class Deck:
#     __backOfCard, __dealtCard = None, None
#     __deck = []
#     __numCardsDealt, __cardsRemaining = 0, 0

#     def __init__(self):
#         self.__backOfCard = None
#         self.__dealtCard = None
#         self.__deck = [None] * 52
#         self.__numCardsDealt = 0
#         self.__cardsRemaining = 52
        
#     def _generateDeck(self):
#         indexDeck = 0
#         list2DCardAbbrevs = ["C", "D", "H", "S"]
#         for row in range(len(list2DCardAbbrevs)):
#             for column in range(len(list2DCardAbbrevs[row])):
#                 self.__deck[indexDeck] = Card()
#                 self.__deck[indexDeck].set_Image(PhotoImage(file="images/" + str(row + 2) + list2DCardAbbrevs[column] + ".png"))
#                 self.__deck[indexDeck].set_Value(row + 2)
#                 self.__deck[indexDeck].set_Suit(list2DCardAbbrevs[column])
#                 indexDeck = indexDeck + 1

#     def dealCard(self):
#         self.__dealtCard = self.__deck[self.__numCardsDealt]
#         self.__numCardsDealt = self.__numCardsDealt + 1
#         return self.__dealtCard
        
#     def getBackOfCard(self):
#         self.__backOfCard = self.__dealtCard
#         self.__backOfCard.set_Image(PhotoImage(file="images/back_blue.png"))
#         return self.__backOfCard

#     def setCardsRemaining(self, num):
#         self.__cardsRemaining = num

#     def getCardsRemaining(self):
#         return self.__cardsRemaining

#     def setTotalCardsDealt(self, num):
#         self.__numCardsDealt = num

#     def getTotalCardsDealt(self):
#         return self.__numCardsDealt

#     def shuffleDeck(self):
#         random.shuffle(self.__deck)