import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def genroom(n):
    return np.random.randint(1, 366, n)


def duplicate_birthdays(n):
    # Generate 1000 simulations of room of size n
    # Determine if the room has duplicate birthdays
    # Returns the number of rooms with duplicate birthdays
    simulation = 1000
    duplicate = 0
    for i in range(simulation):
        room = genroom(n)
        birth_dict = {}
        for people in room:
            birth_dict[people] = birth_dict.get(people, 0) + 1

        for k in birth_dict:
            if birth_dict[k] > 1:
                duplicate += 1
                break

    return duplicate


# Part 1
prob_n = []
for n in range(2, 101):
    prob_n.append(duplicate_birthdays(n) / 1000)
    # call function duplicate_birthdays(n)
    # update the array prob_n

prob_n = np.array(prob_n)
# print(prob_n)


# Part 2
# Estimate perc_50

for index, p in enumerate(sorted(prob_n),2):
    if p > 0.5:
        perc_50 = index
        break
print(prob_n)
print(sorted(prob_n))
# Part 3
# Plot prob_n
sample_size = [n for n in range(2, 101)]
plt.plot(sample_size,prob_n)
plt.xlabel('n')
plt.ylabel('probability')
plt.grid(True)
plt.title('n-probability')
plt.show()