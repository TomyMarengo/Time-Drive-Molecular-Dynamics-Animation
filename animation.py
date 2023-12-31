import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

particles = []
lines = []
particle_positions = []
num_particles = 0


def update(frame):
    global particle_positions, particles, lines, num_particles

    first_line = frame * (num_particles + 1) + 1
    for i in range(num_particles):
        particle_positions[i] = float(lines[i + first_line].split()[1]) % 135

    for i, particle in enumerate(particles):
        particle.center = (particle_positions[i], 0)

    # Change title with time in seconds in each frame
    return particles


def animate(n, delta_t):
    global particle_positions, particles, lines, num_particles

    tf = 180
    particle_radius = 2.25
    line_length = 135
    num_particles = n

    fig, ax = plt.subplots()
    ax.set_xlim(0, line_length)
    ax.set_ylim(-particle_radius, particle_radius)

    # Circles:
    ax.set_aspect('equal')
    # Line
    ground_line, = ax.plot([0, line_length], [0, 0], 'k-', lw=2)

    particle_positions = np.array([0.0] * num_particles)

    formated_delta_t = "{:.6f}".format(delta_t).rstrip('0').rstrip('.')
    file_suffix = str(num_particles) + '_' + formated_delta_t
    with open('outputs/output_ex2_' + file_suffix + '_no_periodic_position.txt', 'r') as file:
        lines = file.readlines()

    first_line = 1
    for i in range(num_particles):
        particle_positions[i] = float(lines[i + first_line].split()[1]) % 135

    colors = plt.cm.viridis(np.linspace(0, 1, num_particles))

    particles = [Circle((particle_positions[i], 0), radius=particle_radius, color=colors[i % num_particles], zorder=10)
                 for i in range(num_particles)]

    for particle in particles:
        ax.add_patch(particle)

    max_frames = int(len(lines) / (num_particles + 1))

    ani = FuncAnimation(fig, update, frames=max_frames, blit=True, interval=100)

    # Hide axis
    ax.axis('off')
    ani.save('gifs/particle_train_' + file_suffix + '.gif')
    print('Gif creado')

    plt.show()
