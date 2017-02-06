def primer_or_not(num):
    #num = get_number()
    num_list = range(2, num + 1)
    div_list = [i for i in num_list
                if num % i == 0 and num != i]  # this is how you can write conditions more compact
    if not div_list:
        return True
    else:
        return False

if primer_or_not(6):
    print('Good! it is works')

