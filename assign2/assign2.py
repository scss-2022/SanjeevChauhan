# assingment 2
#This take only one number randomly for finding probability 
import random

# event of rolling a dice
sample_space = [1, 2, 3, 4, 5, 6]


def choice_of_outcome():
    return random.choice(sample_space)


def permutation_question():
    print(f'outcome of event: {choice_of_outcome()}')


def trial(n):
    trials = []
    for x in range(n):
        trials.append(choice_of_outcome())
        #print(trials[x])
    return sum(trials) / n


if __name__ == '__main__':
    permutation_question()
    number_of_time_dice_rolled = 10000
    print(
        f'probability interpretation for rolling a dice {number_of_time_dice_rolled} '
        f'time is : {trial(number_of_time_dice_rolled)}')


'''
Output
This is Output. It may varie everytime as per outcome.
>>
outcome of event: 6
probability interpretation for rolling a dice 10000 time is : 3.4887
'''