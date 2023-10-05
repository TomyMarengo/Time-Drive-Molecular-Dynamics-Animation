import matplotlib.pyplot as plt
import numpy as np
import math


def main():
    n = 10
    stationary = 120
    filename = f'outputs/particle_train_{n}_0.001.txt'

    with open(filename, 'r') as archive:
        velocities = []
        dt = archive.readline()
        # While doesn't encounter a line with 'Time x.xxxx' where x is a number greater than stationary
        while dt.split() and (dt.split()[0] != 'Time' or float(dt.split()[1]) < stationary):
            for i in range(n):
                archive.readline()
            dt = archive.readline()

        for line in archive:
            cols = line.split()
            if len(cols) > 0 and cols[0] != 'Time':
                velocities.append(float(cols[1]))

    archive.close()

    num_particles = int(len(velocities))
    bins = int(math.log2(num_particles)) + 1
    p, x = np.histogram(velocities, bins)
    x = x[:-1] + (x[1] - x[0]) / 2
    plt.plot(x, [a / ((x[1] - x[0]) * num_particles) for a in p], linestyle='-', label=f'N={n}', color='blue')
    plt.legend()
    plt.ylabel('Densidad de probabilidad ($\\frac{{\mathrm{1}}}{{\mathrm{cm/s}}})$')
    plt.xlabel('Velocidad ($\\frac{{\mathrm{cm}}}{{\mathrm{s}}})$')

    plt.savefig(f'./graphs/pdf_{n}.png')


if __name__ == "__main__":
    main()