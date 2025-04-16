import numpy as np
import matplotlib.pyplot as plt



n = 1000
m = 100

integral = np.zeros(m)

a = 0
b = np.pi / 2

def f(theta):
    return 1 / np.sqrt(1 - 0.5**2 * np.sin(theta)**2)

rand = np.random.uniform(0,1,n*m) * b


for i in range(m):
    j = 0
    theta = rand[i*n:n*(i+1)]
    for t in range(n):
        j += f(theta[t])
    integral[i] = (b - a) * j / n
    std_values = np.zeros(m)
for i in range(1, m + 1):
    std_values[i - 1] = np.std(integral[:i])

plt.plot(range(1, m + 1), std_values, marker='o')
plt.xlabel('параметр i')
plt.ylabel('Стандартное отклонение')
plt.title('Зависимость стандартного отклонения интеграла от значения i')
plt.show()

print("Значение эллиптического интеграла первого рода для k = 0.5 равно:", f"{np.average(integral)} +- {np.std(integral)}")