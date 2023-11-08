import random
print('\tWelcome to Guess My Number!\n')
print('I am thinking of a number between 1 and 100.\n Try to guess it few attnepts as possible.')

value = random.randrange(1,100)
count = 0

while True:
    count +=1
    number = int(input('Take a guess: '))
    if number > value:
        print('lower...')
    elif number < value:
        print('higher!!!')

    else:
        print('You guess it! The number was', value,'\nAnd it only took',count,'tries!')
        break

