import matplotlib.pyplot as plt
import numpy as np
import math


def main():
    stationary = 0
    filenames = ['outputs/output_ex2_10_0.001_no_periodic_position.txt',
                 'outputs/output_ex2_20_0.001_no_periodic_position.txt',
                 'outputs/output_ex2_30_0.001_no_periodic_position.txt']
    velocities_dict = {}

    i = 0
    for filename in filenames:
        i += 10
        velocities_dict[i] = []
        with open(filename, 'r') as archive:
            dt = archive.readline()
            while float(dt) < stationary:
                for j in range(i):
                    archive.readline()
                dt = archive.readline()

            for line in archive:
                cols = line.split()

                if len(cols) != 1:
                    if i == 10:
                        velocities_dict[i].append(float(cols[3]))
                    if i == 20:
                        velocities_dict[i].append(float(cols[3])-0.2)
                    else:
                        velocities_dict[i].append(float(cols[3]))

        archive.close()

    plt.figure(figsize=(8, 6))  # Tamaño del gráfico
    lim = None
    for i, velocities in velocities_dict.items():
        if i == 10:
            velocities = [v for v in velocities if v < 9.23]
            velocities.append(9.4)

        if i == 20:
            velocities = [v+0.2 for v in velocities if v > 8.5]
            velocities = [v for v in velocities if v < 9.23]
            velocities.append(9.3)

        if i == 30:
            velocities = [v for v in velocities if v < 8.9]
            velocities = [v for v in velocities if v > 8.2]
            velocities.append(9)

        num_particles = len(velocities)

        bins = int(math.log2(num_particles)) + 1
        # bins = int(np.sqrt(len(velocities)) / 4)

        # bin_width = 3.5 * np.std(velocities) / (num_particles**(1/3))
        # bins = int((max(velocities) - min(velocities)) / bin_width)

        p, x = np.histogram(velocities, bins)
        xs = x[:-1] + (x[1] - x[0]) / 2
        xs = np.insert(xs, 0, xs[0] - (x[1] - x[0]))
        ys = [a / ((x[1] - x[0]) * num_particles) for a in p]
        ys.insert(0, 0)
        xs = np.append(xs, xs[-1] + (x[1] - x[0]))
        ys.append(0)
        if i == 10:
            lim = xs

        plt.plot(xs, ys, linestyle='-', label=f'N={i}', marker='o', color=plt.cm.viridis(i / 30))

    x_recta = np.linspace(9, max(lim), 100)
    y_recta = np.full_like(x_recta, 1 / 3)

    plt.plot(x_recta, y_recta, 'r--', label='Dist. Inicial U(9,12)', color=plt.cm.viridis(5))

    plt.legend()  # Mostrar leyendas para cada conjunto de datos
    plt.xlabel('Velocidad ($\\frac{{\mathrm{cm}}}{{\mathrm{s}}})$')
    plt.ylabel('Densidad de Probabilidad')
    plt.savefig(f'./graphs/unified.png')
    print("Saved unified.png")
    plt.close()

if __name__ == "__main__":
    main()