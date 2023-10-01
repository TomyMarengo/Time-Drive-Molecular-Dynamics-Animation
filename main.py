from animation import animate
from graphics import *

# Put the txt files in the outputs folder before running the program

# Ej1
# delta_ts = [0.01, 0.001, 0.0001, 0.00001, 0.000001]
# phi(25, delta_ts)  # N = 25

# Ej2.1
nums_particles = [5, 10, 15, 20, 25, 30]
graph_velocity(nums_particles, 0.001)  # delta_t = 0.001

# Ej2.2
nums_particles = [10, 20, 30]
probability_velocity(nums_particles, 0.001)  # delta_t = 0.001

# Animation
nums_particles = [5, 10, 15, 20, 25, 30]
delta_ts = [0.001]
for n in nums_particles:
    for t in delta_ts:
        animate(n, t)

