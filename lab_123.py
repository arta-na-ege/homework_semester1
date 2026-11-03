import matplotlib.pyplot as plt
import numpy as np

# 1. Исходные экспериментальные данные
h_mm = np.array([0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70])  # Расстояние h в мм
T = np.array([3.136, 3.213, 3.160, 3.185, 3.219, 3.261, 3.378, 3.479, 3.943, 4.021, 4.145])  # Период T в с

# 2. Константы
k = 4e-4       # Коэффициент установки (м^2 / с^2)
m = 1.3373     # Суммарная масса двух полудисков (кг)

# 3. Расчёт величин для осей СИ
x = (h_mm / 1000.0) ** 2  # Аргумент h^2 (м^2)
y = k * m * (T ** 2)       # Момент инерции I (кг*м^2)

# 4. Линейная аппроксимация по МНК
A, B = np.polyfit(x, y, 1)

# Настройка графика
fig, ax = plt.subplots(figsize=(8, 6))

# 1. Линия тренда (черная сплошная)
x_fit = np.linspace(0, x.max() * 1.1, 100)
ax.plot(
    x_fit, A * x_fit + B, color='black', linestyle='-', linewidth=1.5,
    label=f'Аппроксимация: I = {A:.3f}·h² + {B:.5f}'
)

# 2. Точка пересечения с осью ординат (черный контурный квадрат)
ax.plot(
    0, B,
    marker='s', color='black', markerfacecolor='white', markeredgewidth=2, markersize=8,
    linestyle='None',
    label=f'Пересечение с осью I: I₀ = {B:.5f} кг·м²',
    zorder=5
)
# Горизонтальная линия, показывающая уровень I₀
ax.axhline(B, color='black', linewidth=1.2, linestyle=':', alpha=0.8)

# 3. Экспериментальные точки (черные контурные кружки)
ax.plot(
    x, y,
    marker='o', color='black', markerfacecolor='none', markeredgewidth=1.2, markersize=6,
    linestyle='None',
    label='Экспериментальные точки',
    zorder=4
)

# Оформление осей (как в самом первом коде)
ax.set_xlabel('$h^2$, м$^2$', fontsize=12)
ax.set_ylabel('$I$, кг$\\cdot$м\(^2\)', fontsize=12)
ax.set_title('Проверка теоремы Гюйгенса-Штейнера')
ax.grid(True, linestyle='-', alpha=0.4)

# Легенда
ax.legend(loc='upper left', framealpha=1, edgecolor='black')

# Ограничения осей
ax.set_xlim(0, x.max() * 1.1)
ax.set_ylim(min(y) * 0.85, max(y) * 1.05)

# Формат оси X (три знака после запятой)
ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.3f'))

plt.tight_layout()
plt.show()

print(f"I₀ = {B:.5f} кг·м²")
print(f"A  = {A:.3f} кг·м²/м²")