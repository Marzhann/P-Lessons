# Practice 3

list_1 = [1,1,2,3,5,8,13,21,34,55,89]

#for elem in list_1:
 #   if elem < 5:
  #      print(elem)

list_less_five = []
for elem in list_1:
    if elem < 5:
        list_less_five.append(elem)

print(list_less_five)

user_num = int(input('enter number : '))
for elem in list_1:
    if user_num > elem:
        list_3 = []
        list_3.append(elem)
        print(list_3)

