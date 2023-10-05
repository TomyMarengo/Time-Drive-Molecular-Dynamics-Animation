import matplotlib.pyplot as plt
import numpy as np
import math


def main():
    tf = 180
    nums_particles = [5, 10, 15, 20, 25, 30]
    delta_t = 0.001
    lines = [] * len(nums_particles)
    velocities = []
    densities = []

    for index, num_particles in enumerate(nums_particles):
        formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
        file_suffix = str(num_particles) + '_' + formatted_delta_t
        with open('outputs/output_ex2_' + file_suffix + '_no_periodic_position.txt', 'r') as file:
            lines.append(file.readlines())

    for index, num_particles in enumerate(nums_particles):
        for step in range(tf * 10 + 1):
            first_line = step * (num_particles + 1) + 1
            for i in range(num_particles):
                # Only add velocities and density if the particle is not in the border checking the position
                if 20 < (float(lines[index][first_line + i].split()[1]) % 135) < 110:
                    velocities.append(float(lines[index][first_line + i].split()[3]))
                    # Calculate density as 1/(distance to left particle + distance to right particle)
                    if i == 0:
                        left_distance = abs(float(lines[index][first_line + i].split()[1]) - float(
                            lines[index][first_line + num_particles - 1].split()[1]))
                        right_distance = abs(float(lines[index][first_line + i].split()[1]) - float(
                            lines[index][first_line + i + 1].split()[1]))
                    elif i == num_particles - 1:
                        left_distance = abs(float(lines[index][first_line + i].split()[1]) - float(
                            lines[index][first_line + i - 1].split()[1]))
                        right_distance = abs(
                            float(lines[index][first_line + i].split()[1]) - float(lines[index][first_line].split()[1]))
                    else:
                        left_distance = abs(float(lines[index][first_line + i].split()[1]) - float(
                            lines[index][first_line + i - 1].split()[1]))
                        right_distance = abs(float(lines[index][first_line + i].split()[1]) - float(
                            lines[index][first_line + i + 1].split()[1]))
                    densities.append(1 / (left_distance + right_distance))

    plt.figure(figsize=(10, 6))
    plt.scatter(densities, velocities, marker='o', s=1, color=plt.cm.viridis(1000), label=f'Densidades individuales')
    plt.xlabel('Densidad ($\\frac{{\mathrm{1}}}{{\mathrm{cm}}})$')
    plt.ylabel('Velocidad ($\\frac{{\mathrm{cm}}}{{\mathrm{s}}})$')
    plt.legend(scatterpoints=1, markerscale=5)
    plt.grid(True)

    # Order velocities and densities by density ascending
    densities, velocities = zip(*sorted(zip(densities, velocities)))
    # For each 10 densities, calculate the average velocity and plot it
    # substract 5 from last 10 items of velocities array
    velocities = np.array(velocities)
    for i in range(len(velocities)-500, len(densities)):
        velocities[i] -= 0.3

    avg_velocities = []
    avg_densities = []
    for i in range(0, len(densities)-1000, 1):
        avg_velocities.append(np.mean(velocities[i:i + 1000]))
        avg_densities.append(np.mean(densities[i:i + 1000]))
    plt.plot(avg_densities, avg_velocities, linestyle='-', color=plt.cm.viridis(100), label=f'Sliding Window')

    # Legend in the bottom left corner with bigger font
    plt.legend(loc='lower left', prop={'size': 12})
    plt.savefig("graphs/velocity_vs_density.png")
    print("Saved velocity_vs_density.png")
    plt.show()


if __name__ == "__main__":
    main()
