#Practice 1
username = input('Enter your name please : ')
age = int(input('Enter your age please : '))
curr_year = 2016
birth_year = curr_year - age
out_year = birth_year + 100
out_str = 'Your name is ' + username + ', and you  will turn 100 years old in ' + str(out_year)
print(out_str)

rep_num = int(input('Give me an another number : '))
print(rep_num * (' '+out_str))
print(rep_num * (out_str+'\n'))
