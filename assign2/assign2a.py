# Assignment 2 extra
# This got Probability for every value of die
import random
import operator

random.seed()

# yha Rolled naam ki dictionary bn rhi hai, dict comprehension use krke
# 1:0
# 2:0
# 3:0
# 4:0
# 5:0
# 6:0
ROLLED = {i: 0 for i in range(1, 7)}
#yha kitne bari chaiyeee ye ho jayega
ITERATIONS = int(input('How many times would you like to roll the dice? '))


def probability():
    print("Calculation of probability: ")
    for key, count in ROLLED.items():
        print("\t{}: {:.2f}".format(key, count * 100. / ITERATIONS * 1.))


for _ in range(ITERATIONS):
    ROLLED[random.randint(1, 6)] += 1

probability()

'''
#Output
This is Output. It may varie everytime as per outcome.
>>
How many times would you like to roll the dice? 100
Calculation of probability:
        1: 18.00
        2: 14.00
        3: 17.00
        4: 14.00
        5: 16.00
        6: 21.00
'''