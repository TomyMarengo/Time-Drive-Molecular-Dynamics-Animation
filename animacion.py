import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

num_particles = 10
particle_radius = 2.25
line_length = 135
animation_duration = 5  


fig, ax = plt.subplots()
ax.set_xlim(0, line_length)
ax.set_ylim(-particle_radius, particle_radius)

# Circles:
ax.set_aspect('equal')

#Line
ground_line, = ax.plot([0, line_length], [0, 0], 'k-', lw=2)


particle_positions = np.random.uniform(0, line_length, num_particles)
colors = plt.cm.viridis(np.linspace(0, 1, num_particles)) 

particles = [Circle((particle_positions[i], 0), radius=particle_radius, color=colors[i], zorder=10) for i in range(num_particles)]

for particle in particles:
    ax.add_patch(particle)

def update(frame):
    global particle_positions

    particle_positions = (particle_positions + 1) % line_length

    for i, particle in enumerate(particles):
        particle.center = (particle_positions[i], 0)

    return particles

ani = FuncAnimation(fig, update, frames=np.arange(0, animation_duration * 60), blit=True)

#Hide axis
ax.axis('off')

plt.show()