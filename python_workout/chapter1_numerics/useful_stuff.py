# random
import random
from datetime import datetime

number = random.randint(1, 100)
print(number)

###################
# comparisons

first = random.randint(1, 100)
second = random.randint(1, 100)

print(first < second)

# f srings
message = f'It is currently {datetime.now()}'
print(message)

# for loops

for elem in range(10):
    print(elem * elem, end = ' ')

# input
name = input('Enter your name: ')
print(name)

# enumerate
for index, item in enumerate('abc'):
    print(f'{index}: {item}')

