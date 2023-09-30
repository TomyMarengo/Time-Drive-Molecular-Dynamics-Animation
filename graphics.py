import matplotlib.pyplot as plt
import numpy as np

tf = 180


def phi(num_particles, delta_ts):
    lines = [] * len(delta_ts)
    phi_t = []
    for index, delta_t in enumerate(delta_ts):
        formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
        file_suffix = str(num_particles) + '_' + formatted_delta_t
        with open('outputs/particle_train_' + file_suffix + '.txt', 'r') as file:
            lines.append(file.readlines())

    for index, delta_t in enumerate(delta_ts):
        phi_t.append([])
        if index == 0:
            continue
        for step in range(tf + 1):
            first_line = step * (num_particles + 2) + 1
            phi_t_k = 0
            for i in range(num_particles):
                phi_t_k += abs(
                    float(lines[index][first_line + i].split()[0]) - float(lines[index - 1][first_line + i].split()[0]))

            phi_t[index].append(phi_t_k)

        plt.semilogy(np.arange(0, tf + 1, 1), phi_t[index], label="k = " + str(index + 1))

    plt.xlabel('Tiempo (s)')
    plt.ylabel('$\phi$')
    plt.legend(loc='upper right')
    plt.savefig("images/phi_" + str(num_particles) + ".png")
    print("Saved phi_" + str(num_particles) + ".png")
    plt.close()


def graph_velocity_vs_time(nums_particles, delta_t):
    lines = [] * len(nums_particles)
    avg_velocities = []

    for index, num_particles in enumerate(nums_particles):
        formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
        file_suffix = str(num_particles) + '_' + formatted_delta_t
        with open('outputs/particle_train_' + file_suffix + '.txt', 'r') as file:
            lines.append(file.readlines())

    for index, num_particles in enumerate(nums_particles):
        avg_velocities.append([])

        for step in range(tf + 1):
            first_line = step * (num_particles + 2) + 1
            avg_velocity = 0
            for i in range(num_particles):
                avg_velocity += float(lines[index][first_line + i].split()[1])

            avg_velocities[index].append(avg_velocity / num_particles)

        plt.plot(np.arange(0, tf + 1, 1), avg_velocities[index], label="N = " + str(num_particles))

    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad promedio (m/s)')
    plt.legend(loc='upper right')
    plt.savefig("images/velocity_vs_time_" + str(delta_t) + ".png")
    print("Saved velocity_vs_time_" + str(delta_t) + ".png")
    plt.close()


