import sys
from random import randint
 
words = ["cat",'can','comb','core','coal','cash','cook','cuff','cap','case','club','cream','king',
         'hat','hone','hem','hare','hail','hash','hog','hoof','hub','hose','heart','queen','hinge',
         'suit','sun','sum','sore','sail','sash','sock','safe','soap','suds','spade','steam','sing',
         'date','dune','dam','door','doll','dash','duck','dive','dope','dose','diamond','dream','drink']

cardId = ["Ace of Clubs", "2 of Clubs", "3 of Clubs","4 of Clubs", "5 of Clubs", 
      "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", 
      "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Hearts", 
      "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts",
      "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts",
      "Queen of Hearts", "King of Hearts", "Ace of Spades", "2 of Spades", 
      "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades",
      "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades",
      "King of Spades", "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", 
      "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", 
      "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds",
      "Queen of Diamonds", "King of Diamonds"]

# holds index's already referenced
used = []

print("Welcome to the Peg Memory aid. This program is specifically" 
          + " for practicing with Harry Lorayne's Card peg method with a "
          + "couple modiifcations made by Sepehr Borji")
print("\nAt any point if you wish to exit the program, type 'q' and press enter")

start = input("Press any key to continue or press 'q' to exit... ")
if start == 'q' or start == 'Q':
    sys.exit()

while len(used) < 52:
    
    # choose a random number to ask about (Peg system should not be ordered)
    index = randint(0,len(words)-1)
    while index in used:
        index = randint(0,len(words)-1)
    else:
        question = input(cardId[index] + ': ')
        question = question.strip()
        if question.lower() == words[index]:
            print("Good job! The answer was " + words[index].title())
            print()
            used.append(index)
        else:
            print("Sorry! The answer was " + words[index].title())
            print()

print("Congratulations! You made it through your list for today!")
print("Please restart the program if you wish to begin again")
input("Press any key to exit...")