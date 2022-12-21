"Best-Pair-31-Game" 

This game was made through Tkinter Module in Python using object-oriented programming priniciples in python
It is a card game similar to Black Jack.

Process:
1) User enters their name to load the interface with their unrevealed cards along with the Banker's unrevealed cards (Computer).
2) They then must deal one card which comes from top row (Only contains one card) where either the banker or the player would win 1 point if their card is of higher value
 - Regardless of who recieves the point, both the user and computer's hand increment by the cards value (1-11) Jack, Queen and King are 10 Ace is 11
* Note: Card Values are as follows (lowest to highest) --> 1, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K, A
3) The user could then bet an amount of points for the second row (Two cards) of cards and if they win by having a greater value of cards in the second row, the user recieves that amount. Otherwise, the banker (Computer) recieves those points.
* Note: the user is never able to bet an amount that allows them to exceed 11 points
4) The user then has to ensure that they don't get their hand above a total value of 31 by choosing to deal and stand. If the user goes over 31 they lose. If the user is closer to 31 than the banker is, then they win the hand and the bet amount of points.
5) This process repeats until a player reaches 11 points where they win the whole game
