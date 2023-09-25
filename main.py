from animation import animate

num_particles = [10, 15, 20, 25]
delta_ts = [0.1, 0.01, 0.001, 0.0001]


for n in num_particles:
    for t in delta_ts:
        animate(n, t)
