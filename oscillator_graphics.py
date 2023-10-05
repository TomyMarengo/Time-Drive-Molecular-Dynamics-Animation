import numpy as np
import matplotlib.pyplot as plt

# Parameters
tf = 5
m = 70
k = 10000
gamma = 100
A = 1
delta_ts = [0.01, 0.001, 0.0001, 0.00001, 0.000001]
max_steps = [500, 5000, 50000, 500000, 5000000]
oscillators = ['beeman', 'gear', 'verlet']
osc_graphic_params = [('blue', '-'), ('cyan', '-.'), ('magenta', ':'), ('black', '--')]
osc_labels = ['Beeman', 'Gear predictor-corrector 5', 'Verlet Original', 'Analítica']

def analytic_position(t):
    return A * np.exp(-(gamma / (2 * m)) * t) * np.cos(np.sqrt(k / m - ((gamma ** 2) / (4 * m ** 2))) * t)


def comparing():
    for i, delta_t in enumerate(delta_ts):
        print("Delta t: " + str(delta_t))
        lines = [] * len(oscillators)
        for j, oscillator in enumerate(oscillators):
            formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
            file_suffix = str(oscillator) + '_' + formatted_delta_t
            with open('outputs/oscillator_' + file_suffix + '.txt', 'r') as file:
                lines.append(file.readlines())

        # Get the anayltic position from 0 to tf, with delta_t as step
        t = np.linspace(0, tf, max_steps[i] + 1)
        analytic_values = analytic_position(t)

        # Read the values from the files for all oscillator with the delta_t and compare MSE with the analytic values
        # Also graph the position for all oscillators and the anylitic one for the delta_t
        for j, oscillator in enumerate(oscillators):
            positions = []
            for line in lines[j]:
                positions.append(float(line))
            # Print length of analytic values and positions
            print("Analytic values length: " + str(len(analytic_values)))
            print("Positions length: " + str(len(positions)))
            # Calculate the MSE
            MSE = np.mean((analytic_values - positions) ** 2)
            print("MSE for " + str(oscillator) + " with delta_t = " + str(delta_t) + ": " + str(MSE))

            # Graph the position
            plt.plot(t, positions, label=osc_labels[j], color=osc_graphic_params[j][0], linestyle=osc_graphic_params[j][1])

        plt.plot(t, analytic_values, label=osc_labels[3], color=osc_graphic_params[3][0], linestyle=osc_graphic_params[3][1])
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Posición (m)')
        plt.legend(loc='upper right')
        plt.savefig("images/position_" + str(delta_t) + ".png")
        print("Saved position_" + str(delta_t) + ".png")
        plt.close()

    # Graph the MSE for all oscillators with the delta_ts
    for j, oscillator in enumerate(oscillators):
        MSEs = []
        for i, delta_t in enumerate(delta_ts):
            formatted_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
            file_suffix = str(oscillator) + '_' + formatted_delta_t
            with open('outputs/oscillator_' + file_suffix + '.txt', 'r') as file:
                lines = file.readlines()

            positions = []
            for line in lines:
                positions.append(float(line))

            # Calculate the MSE
            t = np.linspace(0, tf, max_steps[i] + 1)
            analytic_values = analytic_position(t)
            MSE = np.mean((analytic_values - positions) ** 2)
            MSEs.append(MSE)

        plt.loglog(delta_ts, MSEs, label=osc_labels[j], color=osc_graphic_params[j][0], linestyle=osc_graphic_params[j][1],
                   marker='o')

    plt.xlabel('$\Delta$t (s)')
    plt.ylabel('MSE')
    # legend without overlapping (font size 10) upper left
    plt.legend(loc='upper left', fontsize=10)
    plt.savefig("images/MSE.png")
    print("Saved MSE.png")
    plt.close()


comparing()
