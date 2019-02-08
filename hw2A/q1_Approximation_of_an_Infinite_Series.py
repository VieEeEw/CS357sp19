import math
x = 0.7
t1 = x
t3 = x - x**3/6

err_0_1 = abs(t1 - math.sin(x)) / math.sin(x)
err_0_3 = abs(t3 - math.sin(x)) / math.sin(x)

x = 0.7
tpi4 = 1/2**0.5 + (x-math.pi/4)/2**0.5 - (x-math.pi/4)**2/(2*2**0.5) - (x-math.pi/4)**3/(6*2**0.5)
err_pi4_3 = abs(tpi4 - math.sin(x)) / math.sin(x)

print(err_0_1)
print(err_0_3)
print(err_pi4_3)