# Exercise 4.10: Linear Interpolation
import numpy as np

# a)
# assuming time starts at 0


def interpolate(measurements, delta, time):
    # check if time is in range of measurements
    if time > measurements.size() * delta:
        return -1

    # finding i such that t_i <= time <= t_i+1
    i = 0
    while (i * delta < time):
        i += 1

    # getting y values of surrounding t_i and t_i+1
    y1 = measurements[i]
    y2 = measurements[i + 1]

    # calculating line passing through (t_i, y1) and (t_i+1, y2)
    slope = y2 - y1
    def f(x): return slope + (y1 - i * slope)

    return f(time)


b = int(input("interval from 0 to ...?"))
N = int(input("How many steps of measurements?"))
time = float(input("Enter time for interpolation"))

interval = np.linspace(0, b, N)
delta = interval[1]


def f(x): return x ** 2


y_values = np.array([f(x) for x in interval])

y_time = interpolate(y_values, delta, time)
print(y_time)
