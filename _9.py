# Practice 9
# Guessing game. Let`s have fun
import random
try:
    ran_number = random.randint(1,9)
    n = 1
    in_1 = input('Hi there!Let`s play guessing game.I have number in my mind from 1 to 9.Try to guess! p.s. if you wanna quit type exit: ')
    while in_1 != 'exit':
        if int(in_1) == ran_number and n == 1:
            print('WOW! Do you really read my mind?! That is impressive')
            break
        elif int(in_1) == ran_number and n != 1:
            print('Congrats! You guessed with '+str(n)+' attempt')
            break
        else:
            print('Nope! Try again')
            n += 1
            in_1 = input('Ok. one more time. What number in my mind? : ')
except ValueError:
    print('Sorry that is not number')