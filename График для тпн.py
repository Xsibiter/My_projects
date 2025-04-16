import numpy as np
import matplotlib.pyplot as plt

# Определяем диапазон значений theta от 0.1 до 100 для плавного отображения графика
theta_values = np.linspace(0.1, 100, 1000)

# Формулы для объемов
def volume_cube(theta):
    return ((np.pi * np.sqrt(3)) / np.sqrt(4.758 - (0.167 / theta)))**3

def volume_cylinder(theta):
    return 2 * np.pi * (2.873 / np.sqrt(4.758 - (0.167 / theta)))**3

def volume_sphere(theta):
    return (4 / 3) * np.pi * (np.pi / np.sqrt(4.758 - (0.167 / theta)))**3

# Вычисляем объемы для каждого значения theta
volumes_cube = volume_cube(theta_values)
volumes_cylinder = volume_cylinder(theta_values)
volumes_sphere = volume_sphere(theta_values)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(theta_values, volumes_cube, label="Куб", color="blue")
plt.plot(theta_values, volumes_cylinder, label="Цилиндр", color="green")
plt.plot(theta_values, volumes_sphere, label="Шар", color="red")

# Настройки графика
plt.xlabel("Theta")
plt.ylabel("Объем")
plt.title("Зависимость объема от Theta для куба, цилиндра и шара")
plt.legend()
plt.grid(True)

# Устанавливаем границы оси Y для лучшего отображения результатов
plt.ylim(0, 40)  # Предел по оси Y для удобного отображения
plt.xlim(0, 100)  # Ограничиваем диапазон по X
plt.show()
