import random 

number = random.randint(1,10)
player_name = input("hello, what is your name?")

number_of_guess = 0 

print('okay' + player_name + 'i am guessing number b/w 1 and 10: ' )


while number_of_guess < 5:
    guess = int(input())
    number_of_guess +=1
    if guess < number:
        print('your guess is too low')
    if guess > number:
        print('your guess is too high')
    if guess == number:
        break
if guess == number:
    print ('you guessed the number in ' + str(number_of_guess) + 'tries')
else
    print('you did not guess the number, the number was ' + str(number))