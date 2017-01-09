#Practice 2
num_1 = int(input('Give me some number: '))

if (num_1 % 2) == 0 and (num_1 % 4) != 0:
    print('You gave me an even number!')
elif (num_1 % 2) != 0:
    print('You gave me an odd number!')
else:
    print('You gave me an even number and it is multiple of 4!')

num_2 = int(input('Ask you to first number: '))
check = int(input('Ask you to second number: '))
rem = num_2 % check
if rem == 0:
    print('Your first number evenly divides into second number!')
else:
    print('Ooop! here is a remainder! Your first number divides not evenly into second!')

