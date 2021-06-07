# Memory Systems inspired by Harry Lorayne's teachings
In his book *How To Develop a Super Power Memory*, Harry Lorayne teaches about multiple systems of memory, such as the Peg system. To help me learn these systems and test myself on them easily every day, I made these small desktop applications using Python.  

![*How to Develop a Super Power Memory* by Harry Lorayne](https://github.com/BrosephB/Memory-Systems/blob/main/Readme/icon.jpg?raw=true)

Our brain is an association machine, and our memory works by associating one unknown thing to a previously known thing.

In the Number to Peg words system, each number from 1-100 is associated with a certain word based on how the number sounds. By associating numbers to a word, you can associate this word to anything you want to attach to the respective number. For example, if you are trying to remember your grocery list in order, you'd attach each chronological peg word to whatever you want to buy and all you have to do is count numbers in your head to recall those items later through association.

In the card peg system, each card in a standard 52-card deck is associated with a certain word based on the suit and value of the card. This is a further application of the peg word system but requires different words because the number system does not deal with details such as suits and face cards. This system is best used for trying to remember the order of a shuffled deck of cards. Harry lorayne is also a world-renowned magician, hence his teaching on this subject.


## Requirements
> Based on a pre-determined list of peg words, prompt the user to provide the correct peg word for each number or card. Then, provide feedback to the user on whether or not they were correct. Keep prompting the user until they get every answer correct and then tell the user that the program is complete

## What the Program does
1. Introduce the Program and start by asking for the peg word for any number (determined at random). Below are screenshots for the Peg word system where numbers from 1-100 are prompted from the user. The Card peg system prompts the user for cards a standard 52-card deck. Both programs use the same base source code, but modified to determine the needs for cards vs. numbers 1-100.

	![When the program first starts](https://github.com/BrosephB/Memory-Systems/blob/main/Readme/Intro.png?raw=true)

2. Determine if the user provided the correct peg word, and give feedback. If the user was correct, that number or card will no longer be asked for the duration of the program. If the user is incorrect, the program will ask about that same number or card at random at some other point of the duration of the program
	
	![First peg word is correct and provides positive feedback](https://github.com/BrosephB/Memory-Systems/blob/main/Readme/feedback.png?raw=true)

	![Second peg word is incorrect and provides negative feedback](https://github.com/BrosephB/Memory-Systems/blob/main/Readme/feedback-wrong.png?raw=true)

3. Program continues until all numbers/cards have received a correct answer. Notice how the peg for lily has shown up again and will continue to do so until it is answered correctly.
	
	![the peg for Lily is shown again and will keep repeating until the user answers it correctly](https://github.com/BrosephB/Memory-Systems/blob/main/Readme/leech-twice.png?raw=true)

4. After the last number/card is answered correctly, the program will end

	![The program runs over and over for every number 1-100](https://github.com/BrosephB/Memory-Systems/blob/main/Readme/middle.png?raw=true)

	![The program ends and gives congratulations when you complete the list](https://github.com/BrosephB/Memory-Systems/blob/main/Readme/end.png?raw=true)











