import sys
from random import randint
 
ans = ['tie','noah','ma','rye','law','shoe','cow','ivy','bee','toes', 
       'tot','tin','tomb','tire','towel','dish','tack','dove','tub',
       'nose','net','nun','name','noir','nail','notch','neck','knife',
       'knob','mice','mat','moon','mummy','mower','mule','match','mug',
       'movie','mop','rose','rod','rain','ram','rower','roll','roach',
       'rock','roof','rope','lace','lot','lion','llama','lure','lily',
       'leech','lock','lava','lip','cheese','sheet','chain','chum','cherry',
       'jail','choo choo','chalk','chef','ship','case','cot','coin','comb',
       'car','coal', 'cage','coke','cave','cob','fez','fit','phone','foam',
       'fur','file','fish','fog','fife','fob','bus','bat','bone','bum','bear',
       'bell','beach','book','puff','pipe','disease']

# holds index's already referenced
used = []

print("Welcome to the Peg Memory aid. This program is specifically" 
          + " for practicing with Harry Lorayne's peg method with a "
          + "couple modiifcations made by Sepehr Borji")
print("\nAt any point if you wish to exit the program, type 'q' and press enter")

start = input("Press any key to continue or press 'q' to exit... ")
if start == 'q' or start == 'Q':
    sys.exit()

while len(used) < 100:
    
    # choose a random number to ask about (Peg system should not be ordered)
    index = randint(0,len(ans)-1)
    while index in used:
        index = randint(0,len(ans)-1)
    else:
        question = input(str(index+1) + ': ')
        question = question.strip()
        if question.lower() == ans[index]:
            print("Good job! The answer was " + ans[index].title())
            print()
            used.append(index)
        else:
            print("Sorry! The answer was " + ans[index].title())
            print()

print("Congratulations! You made it through your list for today!")
print("Please restart the program if you wish to begin again")
input("Press any key to exit...")