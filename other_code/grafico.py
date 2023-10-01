import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 70
k = 10000
gamma = 100
A = 1


# Time values
# t = np.linspace(0, 5, 501)

def read_file(filename, num_lines):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()[:num_lines]
        positions = [float(line) for line in lines]
        return positions


deltaT_values = [0.01, 0.001, 0.0001, 0.00001, 0.000001]

errors = []
std_devs = []

for deltaT in deltaT_values:
    n = int(5 / deltaT) + 1
    t = np.linspace(0, 5, n)
    r = A * np.exp(-(gamma / (2 * m)) * t) * np.cos(np.sqrt(k / m - ((gamma ** 2) / (4 * m ** 2))) * t)

    format_deltaT = '{0:.6f}'.format(deltaT).rstrip('00')
    print(format_deltaT)

    beeman = read_file(f'../outputs/oscillator_beeman_{format_deltaT}.txt', n)
    gear = read_file(f'../outputs/oscillator_gear_{format_deltaT}.txt', n)
    verlet = read_file(f'../outputs/oscillator_verlet_{format_deltaT}.txt', n)

    error_beeman = np.mean((r - beeman) ** 2)
    # error_gear = np.mean((r - gear) ** 2)
    error_verlet = np.mean((r - verlet) ** 2)

    r_aux = r[:len(r) - 1]
    aux_gear = gear[1:]

    # Calcular el error cuadrático medio entre Gear y los resultados analíticos defasados
    error_gear = np.mean((r_aux - aux_gear) ** 2)

    errors.append([error_beeman, error_gear, error_verlet])

# deltaT = 0.001
# n = int(5/deltaT) + 1
# t = np.linspace(0, 5, n)
# r = A * np.exp(-(gamma/ (2 * m)) * t) * np.cos(np.sqrt(k /m - ((gamma **2) / (4 * m**2))) * t)

# beeman = read_file(f'outputs/oscilator_beeman_{deltaT}.txt', n)
# gear = read_file(f'outputs/oscilator_gear_{deltaT}.txt', n)
# verlet = read_file(f'outputs/oscilator_verlet_{deltaT}.txt', n)


# Graphics
plt.figure(figsize=(8, 6))
plt.plot(t, r, label='Analítica', color='blue', linestyle='-')
plt.plot(t, beeman, label='Beeman', color='cyan', linestyle='-.')
plt.plot(t, gear, label='Gear', color='magenta', linestyle=':')
plt.plot(t, verlet, label='Verlet', color='black', linestyle='--')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.legend()
plt.grid(True)
plt.show()

nombres_metodos = ['Beeman', 'Gear', 'Verlet']

# Graficar errores para distintos deltaT
plt.figure(figsize=(8, 6))
plt.loglog(deltaT_values, [error[0] for error in errors], marker='o', linestyle='-', label='Error Beeman')
plt.loglog(deltaT_values, [error[1] for error in errors], marker='o', linestyle='-', label='Error Gear')
plt.loglog(deltaT_values, [error[2] for error in errors], marker='o', linestyle='-', label='Error Verlet')

plt.xlabel('Δt (s)')
plt.ylabel('Error Cuadrático Medio (MSE)')
plt.legend()
plt.grid(True)
plt.show()
