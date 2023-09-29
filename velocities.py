import numpy as np
import matplotlib.pyplot as plt



def read_file(filename, n):
    with open(filename, 'r') as file:
        num_lines = 9482 #VER
        lines = file.read().splitlines()[:num_lines]
        current_time = None
        current_particle = 0
        aux = []
        velocities = []
        times= []
        
        for line in lines:
            if line.startswith("Time"):
                if current_time:
                    velocities.append(np.mean(aux))
                    aux = []
                current_time = float(line.split()[-1])
                print("time:", current_time)
                times.append(current_time)
                current_particle = 0  
            elif line:
                x, v = map(float, line.split())
            
                if current_particle < n:
                    aux.append(v)
                    current_particle += 1
    
    return velocities, times # EN REALIDAD EL TIEMPO DEBERIA SER FIJO??? 

ns = [ 10, 15, 20, 25]  #FALTA 5 Y 30

deltaT = 0.001 #ACA TIENE QUE SER EL QUE DIO EN EL OTRO EJ
data_dict = {} 

for n in ns:
    velocities, times = read_file(f'outputs/particle_train_{n}_{deltaT}.txt', n)
    data_dict[n] = {'velocities': velocities, 'times': times}
    
t = np.linspace(0, 43, 429)

plt.figure(figsize=(8, 6))
for n, data in data_dict.items():
    plt.plot(t, data['velocities'], label=f'n = {n}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad Promedio (UNIDAD)')
plt.legend()
plt.grid(True)
plt.show()