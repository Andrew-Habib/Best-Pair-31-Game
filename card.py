'''
Andrew Habib
16 October 2021
Best Pair 31 Program
Card Class Module
'''

# From the tkinter library import the following modules to aid in creating a Graphical User Interface
# These modules enable one to create objects that may be used to formulate enhanced and essential features to create a functioning interface
# Only Import PhotoImage to aid in creating image objects that may be manipulated for visual aid for the user
from tkinter import PhotoImage

# From the PIL library, import Image and ImageTk for more options related to manipulating imagery
# Contains greater facilities that are not included in PhotoImage to help adjust image dimensions
from PIL import Image, ImageTk

# Formulate a class to be used to create a card object for a programmer
class Card:

    # Declare an initializing no-argument constructor - Creating of the Card object and initializing components
    def __init__(self):
        
        # Declare all private class level variables
        # Declare a private class variable that stores the processed or opened image of the back of a card (blue)
        self.__img = Image.open('images/back_blue.png')

        # Declare a private class variable that uses the processed image to create a PhotoImage object that could be displayed to the user when needed
        self.__imgCard = ImageTk.PhotoImage(self.__img)

        # Declare a private class variable that stores the width of the image retrieved above (card image)
        self.__width = self.__img.size[0]

        # Declare a private class variable that stores the height of the image retrieved above (card image)
        self.__height = self.__img.size[1]

        # Declare and initialize a private class integer variable that stores the rank of the card object (e.g. 2 is 2, jack is 11)
        self.__rank = 0

        # Declare and initialize a private class integer variable that stores the value of the card object 
        self.__cardValue = 0

        # Declare and initialize a private class string variable that stores the suit of the card object (diamonds, spades, etc.)
        self.__cardSuit = ""

        # Declare and initialize a private class string variable that stores the name of the card object (e.g. King)
        self.__cardName = ""

    # Mutator/Setter Method --> Returns Void --> Takes Image as parameter
    # Define a class level function that will set the image of the card object  
    def set_Image(self, image):

        # Set the private class image variable to the image passed by the programmer
        self.__img = image

        # Set the private class card object image variable to the image retrieved above
        self.__imgCard = ImageTk.PhotoImage(self.__img)

    # Accessor/Getter Method --> Returns Image --> Takes no parameters
    # Define a function that will return the image of the card object
    def get_Image(self):

        # Return the image of the card Object
        return self.__imgCard

    # Accessor/Getter Method --> Returns Floating Point Value --> Takes no parameters
    # Define a function that will return the width of the card object image
    def get_Width(self):

        # Return the width of the card object image
        return self.__width

    # Accessor/Getter Method --> Returns Floating Point Value --> Takes no parameters
    # Define a function that will return the height of the card object image
    def get_Height(self):

        # Return the height of the card Object image
        return self.__height

    # Mutator/Setter Method --> Returns Void --> Takes floating point as parameter
    # Define a class level function that will set the width of the card object  
    def set_Width(self, width):

        # Set the private class floating point width variable to the value of the parameter passed
        self.__width = width

        # Update the private class image processing variable to the resized image of the card object set based on the attained width
        self.__img = self.__img.resize((self.__width, self.__height), Image.ANTIALIAS)

        # Update the private class image variable to the newly resized image of the card object
        self.__imgCard = ImageTk.PhotoImage(self.__img)

    # Mutator/Setter Method --> Returns Void --> Takes floating point as parameter
    # Define a class level function that will set the height of the card object 
    def set_Height(self, height):

        # Set the private class floating point height variable to the value of the parameter passed
        self.__height = height

        # Update the private class image processing variable to the resized image of the card object set based on the attained height
        self.__img = self.__img.resize((self.__width, self.__height), Image.ANTIALIAS)

        # Update the private class image variable to the newly resized image of the card object
        self.__imgCard = ImageTk.PhotoImage(self.__img)

    # Mutator/Setter Method --> Returns Void --> Takes integer as parameter
    # Define a class level function that will set the card value of the card object  
    def set_Value(self, value):

        # Set the private class card value integer variable to the value passed in the parameter
        self.__cardValue = value

    # Accessor/Getter Method --> Returns Integer Value --> Takes no parameters
    # Define a function that will return the card value of the card object image
    def get_Value(self):

        # Return the private class card value integer variable
        return self.__cardValue

    # Mutator/Setter Method --> Returns Void --> Takes integer as parameter
    # Define a class level function that will set the suit of the card object 
    def set_Suit(self, suit):

        # Update the private class suit string variable to the value passed in the parameter
        self.__cardSuit = suit

    # Accessor/Getter Method --> Returns String Value --> Takes no parameters
    # Define a function that will return the card suit of the card object image
    def get_Suit(self):

        # Return the private class card suit string variable
        return self.__cardSuit

    # Mutator/Setter Method --> Returns Void --> Takes integer as parameter
    # Define a class level function that will set the rank of the card object 
    def set_Rank(self, rank):

        # Update the private class rank integer variable to the value passed in the parameter
        self.__rank = rank

    # Accessor/Getter Method --> Returns Integer Value --> Takes no parameters
    # Define a function that will return the card rank of the card object image
    def get_Rank(self):

        # Return the private class card rank integer variable
        return self.__rank

    # Mutator/Setter Method --> Returns Void --> Takes string as parameter
    # Define a class level function that will set the name of the card object 
    def set_Name(self, name):

        # Update the private class card name string variable to the value passed in the parameter
        self.__cardName = name

    # Accessor/Getter Method --> Returns String Value --> Takes no parameters
    # Define a function that will return the name of the card object image
    def get_Name(self):

        # Return the private class card name string variable
        return self.__cardName












    # Extra Unused Code
    # def get_Name(self):
    #     if self.__cardName == "":
    #         outputCardValue = ""
    #         if self.__cardValue >= 2 and self.__cardName <= 10:
    #             outputCardValue = str(self.__cardValue)
    #         elif self.__cardValue == 11:
    #             outputCardValue = "Jack"
    #         elif self.__cardValue == 12:
    #             outputCardValue = "Queen"
    #         elif self.__cardValue == 13:
    #             outputCardValue = "King"
    #         elif self.__cardValue == 14:
    #             outputCardValue = "Ace"
    #         self.__cardName = (outputCardValue + " OF " + self.__cardSuit).upper()
    #     return self.__cardName

# from tkinter import PhotoImage

# class Card:

#     # Declare class-level variables
#     __width, __height = 0.0, 0.0
#     __cardValue = 0
#     __cardSuit, __cardName = "", ""
#     __imgCard = None

#     # Declare a no-arg constructor
#     def __init__(self, image=None, value=0, suit=None, name=None):
#         if image == None:
#             self.__imgCard = PhotoImage(file='images/back_blue.png')
#         else:
#             self.__imgCard = image

#         self.__width = self.__imgCard.width()
#         self.__height = self.__imgCard.height()

#         self.__cardValue = value

#         if suit == None:
#             self.__cardSuit = ""
#         else: 
#             self.__cardSuit = suit

#         if name == None:
#             self.__cardName = ""
#         else:
#             self.__cardName = name

#     def set_Image(self, image):
#         self.__imgCard = image

#     def get_Image(self):
#         return self.__imgCard

#     def get_Width(self):
#         return self.__width

#     def get_Height(self):
#         return self.__height

#     def set_Size(self, largerSmaller="Larger", size=1):
#         if largerSmaller == "Larger":
#             self.__imgCard = self.__imgCard.zoom(size)
#         else:
#             self.__imgCard = self.__imgCard.subsample(size)

#     def set_Value(self, value):
#         self.__cardValue = value

#     def get_Value(self):
#         return self.__cardValue

#     def set_Suit(self, suit):
#         self.__cardSuit = suit

#     def get_Suit(self):
#         return self.__cardSuit

#     def set_Name(self, name):
#         self.__cardName = name

#     def get_Name(self):
#         if self.__cardName == "":
#             outputCardValue = ""
#             if self.__cardValue >= 2 and self.__cardName <= 10:
#                 outputCardValue = str(self.__cardValue)
#             elif self.__cardValue == 11:
#                 outputCardValue = "Jack"
#             elif self.__cardValue == 12:
#                 outputCardValue = "Queen"
#             elif self.__cardValue == 13:
#                 outputCardValue = "King"
#             elif self.__cardValue == 14:
#                 outputCardValue = "Ace"
#             self.__cardName = (outputCardValue + " OF " + self.__cardSuit).upper()
#         return self.__cardName
