import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import seaborn as sns

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


def graph_velocity(nums_particles, delta_t):
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

                print(float(lines[index][first_line + i].split()[1]))
            print("avg_velocity: " + str(avg_velocity))
            avg_velocities[index].append(avg_velocity / num_particles)

        plt.plot(np.arange(0, tf + 1, 1), avg_velocities[index], label="N = " + str(num_particles))

    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad promedio (m/s)')
    plt.legend(loc='upper right')
    plt.savefig("images/velocity_vs_time_" + str(delta_t) + ".png")
    print("Saved velocity_vs_time_" + str(delta_t) + ".png")
    plt.close()

    # velocity vs particles
    stationary_state = int(avg_velocities.shape[1] * 0.5)  # TODO: Change this to stationary_state (current 50%)
    avg_velocities = np.array(avg_velocities)
    avg_velocities_stationary = avg_velocities[:, stationary_state:]
    avg_velocities = np.mean(avg_velocities_stationary, axis=1)
    std_devs = np.std(avg_velocities_stationary, axis=1)
    plt.errorbar(nums_particles, avg_velocities, yerr=std_devs, fmt='o')
    plt.xlabel('Cantidad de partículas')
    plt.ylabel('Velocidad promedio (m/s)')
    plt.savefig("images/velocity_vs_particles_" + str(delta_t) + ".png")
    print("Saved velocity_vs_particles_" + str(delta_t) + ".png")
    plt.close()


def probability_velocity(nums_particles, delta_t):
    # Get all velocities of all particles, for all times of the stationary state and graph the probability distribution
    # using a gaussian adjustment. Graph all simulation (depending on num_particles) in the same plot.

    # Get the velocities of the stationary state
    velocities = [] * len(nums_particles)
    for index, num_particles in enumerate(nums_particles):
        formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
        file_suffix = str(num_particles) + '_' + formatted_delta_t
        with open('outputs/particle_train_' + file_suffix + '.txt', 'r') as file:
            lines = file.readlines()
            velocities.append([])
            for step in range((tf + 1)//2, tf + 1):  # TODO: Change this to stationary_state (current 50%)
                first_line = step * (num_particles + 2) + 1
                for i in range(num_particles):
                    velocities[index].append(float(lines[first_line + i].split()[1]))

        # Adjust a gaussian distribution to the velocities, plot all simulations in the same plot
        mu, std = norm.fit(velocities[index])
        x = np.linspace(min(velocities[index]), max(velocities[index]), velocities[index] )
        pdf = norm.pdf(x, mu, std)
        pdf /= pdf.sum()

        plt.plot(x, pdf, label="N = " + str(num_particles))



    plt.xlabel('Velocidad (m/s)')
    plt.ylabel('Densidad de Probabilidad')
    plt.title('Curva de Distribución de Probabilidad de Velocidades')  # TODO: Delete this
    plt.legend()
    plt.savefig("images/probability_velocity_" + str(delta_t) + ".png")
    print("Saved probability_velocity_" + str(delta_t) + ".png")
    plt.show()
    plt.close()





