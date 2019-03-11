import numpy as np

dice_list = [[1, 1, 1, 1, 7, 7], [4, 4, 4, 4, 4, 4], [2, 2, 2, 2, 6, 6], [3, 5, 3, 3, 5, 5]]


def winning_dice(dice_list):
    # add your code here
    # for i in range(len(dice_list)):
    # my_dice = dice_list[i]
    n = len(dice_list)
    winning_list = np.array([0 for i in range(n)])
    for j in range(5000):
        max_value = -1
        winner = 0
        for i in range(n):
            roll = np.random.randint(0, 6)
            if dice_list[i][roll] > max_value:
                winner = i
                max_value = dice_list[i][roll]
        winning_list[winner] += 1
    winning_list = winning_list / 5000
    selected_dice = 0
    prob = 0
    for i in range(n):
        if winning_list[i] > prob:
            selected_dice = i
            prob = winning_list[i]
    return selected_dice, prob


print(winning_dice(dice_list))
