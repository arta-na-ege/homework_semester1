
# исправленный дипсиком код:
import numpy as np
import matplotlib.pyplot as plt

# Константы
L = 7.0          # м
c = 0.299792     # м/нс
m_n = 939.56563  # МэВ (энергия покоя нейтрона)

def recon_energy(E_avg, scale, num=10000):
    # Генерируем кинетическую энергию
    E_k = np.random.normal(E_avg, scale, num)
    E_k = E_k[E_k > 0]  # фильтруем отрицательные и нулевые значения

    if E_k.size == 0:
        raise ValueError("Все сгенерированные значения E_k <= 0")

    gamma = E_k / m_n + 1.0
    beta2 = 1.0 - (1.0 / gamma) ** 2
    beta = np.sqrt(beta2)

    if np.any(beta >= 1.0):
        raise ValueError("скорость не может превышать скорость света")

    t_s = L / (c * beta)  # время пролёта, нс
    t_mean_rec = np.mean(t_s)
    t_std_rec = np.std(t_s)

    print(f"t_mean реконструированное = {t_mean_rec:.6f} нс")
    print(f"t_std  (реконструированное) = {t_std_rec:.6f} нс")

    t_min = L / c
    t_rec = np.random.normal(t_mean_rec, t_std_rec, num)
    t_rec = t_rec[t_rec > t_min]

    beta_r = L / (c * t_rec)
    gamma_r = 1.0 / np.sqrt(1.0 - beta_r ** 2)
    E_rec = m_n * (gamma_r - 1.0)

    print(f"<E> вход  = {E_avg:.3f} МэВ,  sigma_E вход  = {scale:.3f} МэВ")
    print(f"<E> выход = {np.mean(E_rec):.3f} МэВ,  "
          f"sigma_E выход = {np.std(E_rec):.3f} МэВ")

    plt.figure(figsize=(10, 8))
    plt.hist(E_rec, bins=200, density=True, alpha=0.7,
             color='steelblue', edgecolor='black',
             label="восстановленное распределение энергии")

    plt.axvline(E_avg, color='red', linestyle='--',
                label=f'цель $E$ = {E_avg:.1f} МэВ')
    plt.axvline(np.mean(E_rec), color='green', linestyle=':',
                label=f'$\\langle E \\rangle$ = {np.mean(E_rec):.1f} МэВ')

    plt.xlabel("Кинетическая энергия, МэВ", fontsize=12)
    plt.ylabel("Плотность вероятности", fontsize=12)
    plt.legend()
    plt.grid(True)

    plt.text(0.05, 0.95,
             f'$t_{{mean}}$ = {t_mean_rec:.4f} нс\n'
             f'$t_{{std}}$  = {t_std_rec:.4f} нс\n'
             f'$\\sigma_E$ (выход) = {np.std(E_rec):.2f} МэВ',
             transform=plt.gca().transAxes, va='top')

    plt.show()

    return {
        'E_sim': E_k,
        't_sim': t_s,
        't_mean_rec': t_mean_rec,
        'E_rec': E_rec,
    }


if __name__ == "__main__":
    E_avg = float(input("Введите среднюю кинетическую энергию, МэВ: "))
    scale = float(input("Введите sigma_E, МэВ: "))
    recon_energy(E_avg, scale)


# код руками
'''import numpy as np
import matplotlib.pyplot as plt

E_avg = float(input())
# введу константы:

l = 7.0 #м
c = 0.299792 #м/нс
m_n = 939.56563 #МэВ/с^2
t_s = np.zeros(num)
t_min = l/c

l = l / c
def recon_energy(E_avg, scale, num = 10000):
    E_k = np.random.normal(E_avg, scale, num)
    E_k[E_k > 0]

    # E_k = m_n * (gamma - 1)
    # gamma = 1.0 / np.sqrt(1 - v**2)
    gamma = E_k // m_n + 1.0
    v2 = 1 - (1/ gamma)**2
    v = np.sqrt(v2)
    if np.any(v >= 1.0):
        raise ValueError("скорость не может превышать скорость света")

    t_s = l / (c * v)
    t_mean_rec = np.mean(t_s)
    t_std_rec = np.std(t_s)

    print(f"t_mean реконструированное = {t_mean_rec:.6f} нс")
    print(f"t_std  реконструированное = {t_std_rec:.6f} нс")

    t_rec = np.random.normal(t_mean_rec, t_std_rec, num)
    t_rec = t_rec[t_rec > t_min]
    
    beta_r  = l / (c * t_rec)
    gamma_r = 1.0 / np.sqrt(1.0 - beta_r**2)
    E_rec   = m_n * (gamma_r - 1.0)

    print(f"<E> вход  = {E_avg:.3f} МэВ,  sigma_E вход  = {scale:.3f} МэВ")
    print(f"<E> выход = {np.mean(E_rec):.3f} МэВ,  "
        f"sigma_E выход = {np.std(E_rec):.3f} МэВ")

    
    plt.figure(figsize=(10, 8))
    plt.hist(E_rec, bins=200, density=True, alpha=0.7,
            color='steelblue', edgecolor='black',
            label="восстановленное распределение энергии")

    plt.axvline(E_avg, color='red', linestyle='--',
                label=f'цель $E$ = {E_avg:.1f} МэВ')
    plt.axvline(np.mean(E_rec), color='green', linestyle=':',
                label=f'$\\langle E \\rangle$ = {np.mean(E_rec):.1f} МэВ')

    plt.xlabel("Кинетическая энергия, МэВ", fontsize=12)
    plt.ylabel("вероятность", fontsize=12)
    plt.legend()
    plt.grid(True)

    plt.text(0.05, 0.95,
            f'$t_{{mean}}$ = {t_mean_rec:.4f} нс\n'
            f'$t_{{std}}$  = {t_std_rec:.4f} нс\n'
            f'$\\sigma_E$ (выход) = {np.std(E_rec):.2f} МэВ',
            transform=plt.gca().transAxes, va='top')

    plt.show()
    return {'E_sim': E_k,
            't_sim': t_s,
            't_mean_rec': t_std_rec,
            'E_rec': E_rec,
            }'''