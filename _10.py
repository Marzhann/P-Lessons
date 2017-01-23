# lesson 10
# Concepts of lesson: List comprehension; Random numbers
import random

a = [random.randint(1, 15) for n in range(0, 10)]
b = [random.randint(1, 15) for n in range(0, 30)]

print(a)
print(b)

overlap_list = [n for n in a if n in b]
print(overlap_list)

common_list = []

for elem in overlap_list:
    if not common_list.count(elem) == 1:
        common_list.append(elem)

print(common_list)
