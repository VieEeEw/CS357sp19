import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -x ** 3 / 3 + 4 * x ** 2 / 2 + 2 * x + 2


a = -10
b = 10

brackets = []
gs = (np.sqrt(5) - 1) / 2
m1 = a + (1 - gs) * (b - a)
m2 = a + gs * (b - a)

# Begin your modifications below here
t = 0.618
count = 0

while abs(b - a) > 1e-5:
    if count == 0:
        brackets.append([a, m1, m2, b])
        h0 = b - a
        x1 = a + (1 - t) * h0
        x2 = a + t * h0
        f1 = f(x1)
        f2 = f(x2)
        go_right = False
        go_left = False
    else:
        brackets.append([a, m1, m2, b])
        h0 = b - a
        x1 = a + (1 - t) * h0
        x2 = a + t * h0
        if go_right:
            f1 = f2
            f2 = f(x2)
        elif go_left:
            f2 = f1
            f1 = f(x1)
        go_right = False
        go_left = False

    if f1 > f2:
        h1 = b - x1
        a = x1
        x1 = x2
        h1 = b - a
        x2 = a + t * h1
        go_right = True
        # f2 = f(x2)

    if f1 < f2:
        h1 = x2 - a
        b = x2
        x2 = x1
        x1 = a + (1 - t) * h1
        go_left = True
        # f1 = f(x1)
    count += 1

# End your modifications above here
print(brackets)
print(a, b)
# Plotting code below, no need to modify
x = np.linspace(-10, 10)
plt.plot(x, f(x))

brackets = np.array(brackets)
for i in range(4):
    plt.plot(brackets[:, i], 3 * np.arange(len(brackets)), 'o-')
plt.show()
