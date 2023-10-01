import numpy as np
import matplotlib.pyplot as plt

# Parameters
tf = 5
m = 70
k = 10000
gamma = 100
A = 1
delta_ts = [0.01, 0.001, 0.0001, 0.00001, 0.000001]
oscillators = ['beeman', 'gear', 'verlet']
params = [('blue', '-'), ('cyan', '-.'), ('magenta', ':'), ('black', '--')]

def analytic_position(t):
    return A * np.exp(-(gamma / (2 * m)) * t) * np.cos(np.sqrt(k / m - ((gamma ** 2) / (4 * m ** 2))) * t)


def comparing():
    for i, delta_t in enumerate(delta_ts):
        lines = [] * len(oscillators)
        for j, oscillator in enumerate(oscillators):
            formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
            file_suffix = str(oscillator) + '_' + formatted_delta_t
            with open('outputs/oscillator_' + file_suffix + '.txt', 'r') as file:
                lines.append(file.readlines())

        # Get the anayltic position from 0 to tf, with delta_t as step
        t = np.linspace(0, tf, int(tf / delta_t) + 1)
        analytic_values = analytic_position(t)

        # Read the values from the files for all oscillator with the delta_t and compare MSD with the analytic values
        # Also graph the position for all oscillators and the anylitic one for the delta_t
        for j, oscillator in enumerate(oscillators):
            positions = []
            for line in lines[j]:
                positions.append(float(line))

            # Calculate the MSD
            MSD = np.mean((analytic_values - positions) ** 2)
            print("MSD for " + str(oscillator) + " with delta_t = " + str(delta_t) + ": " + str(MSD))

            # Graph the position
            plt.plot(t, positions, label=oscillator, color=params[j][0], linestyle=params[j][1])

        plt.plot(t, analytic_values, label="analítico", color=params[3][0], linestyle=params[3][1])
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Posición (m)')
        plt.legend(loc='upper right')
        plt.savefig("images/position_" + str(delta_t) + ".png")
        print("Saved position_" + str(delta_t) + ".png")
        plt.close()

    # Graph the MSD for all oscillators with the delta_ts
    for j, oscillator in enumerate(oscillators):
        MSDs = []
        for i, delta_t in enumerate(delta_ts):
            formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
            file_suffix = str(oscillator) + '_' + formatted_delta_t
            with open('outputs/oscillator_' + file_suffix + '.txt', 'r') as file:
                lines = file.readlines()

            positions = []
            for line in lines:
                positions.append(float(line))

            # Calculate the MSD
            t = np.linspace(0, tf, int(tf / delta_t) + 1)
            analytic_values = analytic_position(t)
            MSD = np.mean((analytic_values - positions) ** 2)
            MSDs.append(MSD)

        plt.loglog(delta_ts, MSDs, label=oscillator)

    plt.xlabel('$\Delta t (s)')
    plt.ylabel('MSD')
    plt.legend(loc='upper right')
    plt.savefig("images/MSD.png")
    print("Saved MSD.png")
    plt.close()


comparing()
