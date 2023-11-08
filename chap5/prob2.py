import random

WORDS = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
word = random.choice(WORDS)
correct = word
tries = 1

jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(" Welcome to Word Jumble!\nUnscramble the letters to make a word.")
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not correct.")
    guess = input("Your guess: ")
    
if guess == correct:
    print("\nGood! You guessed it!\n")

