import numpy as np
import matplotlib.pyplot as plt

l = 7.0 #м
t_mean = 30 #нс
t_std = 0.150 #нс
m_n = 939.56563 #МэВ/с^2
c = 0.299792 #м/нс
# переведу значения длины:
l = l / c
    
n_s = 100000
t_s = np.random.normal(t_mean, t_std, n_s)


# вычисление скорости в м
v = l/t_s


gamma = 1.0 / np.sqrt(1 - v**2)

E_k = m_n * (gamma - 1)

plt.figure(figsize = (10, 8))
plt.hist(E_k, bins= 200, density= True,alpha= 0.7, color= 'blue', edgecolor= 'black', label = "нормальное распределение кинетической энергии нейтрона")


plt.xlabel("Кинетическая энергия, МэВ", fontsize= 12)
plt.ylabel('Плотность вероятности', fontsize= 12)

plt.legend()
plt.grid(True)

plt.text(0.05, 0.95, f'Eср = {np.mean(E_k)}, минимум = {np.min(E_k)}, максимум = {np.max(E_k)}')

plt.show()