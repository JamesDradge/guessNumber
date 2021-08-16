import sys, random
number = random.randint(1, 20)
print('Im thinking of a number between 1 and 20, can you guess it?')
for guessesTaken in range(1, 7):
    guess = input()
    if int(guess) > number:
        print('Your guess is too high.')
        print('Try again')
    elif int(guess) < number:
        print('Your guess is too low.')
        print('Try again')
    else:
        break
if int(guess) == number:
    print('You guess correct! You guessed my number in ' + str(guessesTaken) + ' tries')
else:
    print('Sorry, you didnt guess my number, it was ' + str(number))
sys.exit