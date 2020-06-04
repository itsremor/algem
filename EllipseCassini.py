import matplotlib.pyplot as plt
import numpy as np


def ellipse(x_param, a_param, c_param):
    return np.sqrt(np.sqrt(a_param ** 4 + 4 * x_param ** 2 * c_param ** 2) - x_param ** 2 - c_param ** 2)


print('Ellipse of Cassini: ')
print('sqrt(sqrt(a^4 + 4 * c^2 * x^2) - x^2 - c^2) ')

a = float(input('Enter parameter a: '))
c = float(input('Enter parameter c: '))

x = np.linspace(-4*c, 4*c, 666666)
y = []

for x_value in x:
    y_result = ellipse(x_value, a, c)
    y.append([y_result, -1 * y_result])

plt.plot(x, y)
plt.show()
