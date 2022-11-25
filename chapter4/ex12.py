# Exercise 4.12: Fit Straight Line to Data
import matplotlib.pyplot as plt


# gives back square distance between linear function and actual measurements
def error_function(x, y, a, b):
    error = 0
    for i in range(len(x)):
        error += (a * x[i] + b - y[i]) ** 2
    return error


x_values = [1, 2, 3, 4, 5]
y_values = [0.5, 2.0, 1.0, 1.5, 7.5]


a = 1
b = 0


def f(x):
    return a * x + b


while True:
    a = float(input("Please enter the slope of f: "))
    b = float(input("Please enter the value of b: "))
    if a < 0:
        break

    f_values = [f(x) for x in range(0, 7)]
    error = error_function(x_values, y_values, a, b)

    plt.plot(f_values, color="red")
    plt.plot(x_values, y_values, "*", color="green")
    plt.grid("on")
    plt.axis([-1, 6, -1, 8])
    plt.text(-0.9, -0.9, f"Error: {error}")
    plt.show()
