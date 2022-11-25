# Exercise 4.9: Find Crossing Points of Two Graphs
import numpy as np


def f(x):
    return x


def g(x):
    return x**2


N = int(input("How many steps on interval [-4, 4]?\n"))
epsilon = float(input("Give an epsilon:\n"))

interval = np.linspace(-4, 4, N)
crossing_points = []

for x in interval:
    difference = abs(f(x) - g(x))
    if difference < epsilon:
        crossing_points.append(x)

print("crossing points are:")
print(crossing_points)
