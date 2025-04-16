import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры
L = 16.98  # длина L
D = 0.51947  # коэффициент D
a = 1
x = np.linspace(0, 5 * L, 500)  # значения x от 0 до 5L

# Расчёт функций
phi_inf = (L / (2 * D)) * np.exp(-x / L)  # для a/L -> infinity
phi_1 = (L / (2 * D)*(1-np.exp(-2))) * (np.exp(-x / L) - np.exp(-2)*np.exp( x / L ))  # для a/L = 1

# Построение графиков
plt.figure(figsize=(10, 6))
plt.ylim(-10,20)
plt.plot(x, phi_inf, label=r"$a/L \rightarrow \infty$", color='blue')
plt.plot(x, phi_1, label=r"$a/L = 1$", color='orange')
plt.xlabel("x")
plt.ylabel(r"$\Phi(x)$")
plt.title("Зависимость потока $\Phi$ от $x$")
plt.legend()
plt.grid(True)
plt.show()
