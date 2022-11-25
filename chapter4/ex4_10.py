# Exercise 4.10: Linear Interpolation
import numpy as np

# a)
# assuming time starts at 0


def interpolate(measurements, delta, time):
    # check if time is in range of measurements
    # if time > measurements.size() * delta:
    #     return -1

    # finding i such that t_i <= time <= t_i+1
    i = 0
    while i * delta < time:
        i += 1
    print(f"i: {i}")

    # getting y values of surrounding t_i-1 and t_i
    # and making line passing through (t_i-1, y1) and (t_i, y2)
    x = [delta * (i - 1), delta * 1]
    y = [measurements[i - 1], measurements[i]]
    coefficients = np.polyfit(x, y, 1)

    return coefficients[0] * time + coefficients[1]


b = int(input("interval from 0 to ...?"))
N = int(input("How many steps of measurements?"))
time = float(input("Enter time for interpolation"))

print(f"interval: [0, {b}]\nsteps: {N}\ntime: {time}")

interval = np.linspace(0, b, N)
delta = interval[1]

print(f"interval from {interval[0]} to {interval[N - 1]}\ndelta: {delta}")


def f(x):
    return x**2


y_values = [f(x) for x in interval]

y_time = interpolate(y_values, delta, time)
print(y_time)
