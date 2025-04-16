import matplotlib.pyplot as plt


tau = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270,
       300, 330, 360, 390, 420, 450, 480, 510, 540, 570]


theta = [32.5, 31, 30, 28.5, 27, 26, 25, 23.5, 22.5, 21,
         20, 19, 18, 17, 16, 15, 14, 13.5, 12.5, 12]




plt.figure(figsize=(10, 6))
plt.plot(tau, theta, marker='o', label='Цилиндр', color='red')
plt.xlabel('Время τ (с)')
plt.ylabel('θ, °C')
plt.title('График зависимости θ от времени')
plt.grid(True)
plt.legend()
plt.show()

