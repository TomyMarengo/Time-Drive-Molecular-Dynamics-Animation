import numpy as np

avg_velocities = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

avg_velocities = np.array(avg_velocities)

stationary_states = int(avg_velocities.shape[1] * 0.5)
avg_velocities_stationary = avg_velocities[:, stationary_states:]

print(avg_velocities.shape[0])
print(avg_velocities.shape[1])
print(stationary_states)
print(avg_velocities_stationary)