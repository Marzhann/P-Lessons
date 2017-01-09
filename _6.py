# Practice 6

while True:
    ent_str = input('Enter word to check: ')
    rev_str = ent_str[::-1]
    if ent_str == rev_str:
        print('This word is polindrom!')
    else:
        print('Oops! NON POLINDROM WORD')



