# Lesson 4
while True:
    try:
        num = int(input('Please enter a number: '))
        num_list = range(2, num + 1)

        # div_list = []

        # for i in num_list:
        #    if num % i == 0:
        #       div_list.append(i)

        div_list = [i for i in num_list
                    if num % i == 0 and num != i]  # this is how you can write conditions more compact

        if not div_list:
            print(num, 'is prime number!')
        else:
            print('this is a list of divisors for your number: ', div_list)
    except ValueError:
        print('Sorry, this is not a number!')

