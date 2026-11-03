import numpy as np
import matplotlib.pyplot as plt


angles_deg = np.array([20.8, 25.5, 29.1, 35.2, 40.0, 50.8])

# ускорения для каждого угла 3 раза
a_vals = np.array([
    [0.73, 0.611, 1.918, 2.857, 3.602, 5.411],
    [0.636, 0.765, 1.777, 2.433, 3.686, 5.45],
    [0.611, 0.915, 1.863, 2.794, 3.549, 5.34]
])

# Среднее и стандартное отклонение
a_mean = a_vals.mean(axis=0)
a_std = a_vals.std(axis=0, ddof=0)  # STDEV.P

# угол в радианах
phi = np.radians(angles_deg)

#  для графика
tau = np.tan(phi)
a_prime = a_mean / np.cos(phi)

# Линейная аппроксимация a' 
coeff = np.polyfit(tau, a_prime, 1)
g = coeff[0]
intercept = coeff[1]
mu = -intercept / g

# Построение графика
plt.figure(figsize=(8, 6))
plt.errorbar(
    tau, a_prime,
    yerr=a_std / np.cos(phi),
    fmt='o', capsize=5, label='Экспериментальные точки'
)

x_fit = np.linspace(0, tau.max() * 1.1, 100)
plt.plot(
    x_fit, g * x_fit + intercept, 'r-',
    label=f"Аппроксимация: a' = {g:.2f}τ − {g*mu:.2f}"
)

plt.xlabel(r'$\tau = \mathrm{tg}\,\phi$')
plt.ylabel(r"$a' = a / \cos\phi$, м/с²")
plt.title('Зависимость приведённого ускорения от tg φ')
plt.grid(True)
plt.legend()
plt.text(
    0.05, 0.85,
    f'g = {g:.2f} м/с²\nμ = {mu:.3f}',
    transform=plt.gca().transAxes,
    bbox=dict(facecolor='white', alpha=0.8)
)

plt.tight_layout()
plt.show()

print(f"g = {g:.3f} м/с²")
print(f"μ = {mu:.3f}")