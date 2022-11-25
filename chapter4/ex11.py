# Exercise 4.11: Test Straight Line Requirement
import random


def f(x):
    return 4 * x + 1


# draw 100 random values between 0 and 10
random_x_values = [random.uniform(0, 10) for x in range(100)]
print(f"drawn {len(random_x_values)} values\n")
# print(random_x_values)

c = 2
calculated_slopes = []

for x in random_x_values:
    slope = (f(x) - f(c)) / (x - c)
    calculated_slopes.append(slope)

print(calculated_slopes)
