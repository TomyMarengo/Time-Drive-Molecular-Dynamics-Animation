import numpy as np
import matplotlib.pyplot as plt


def read_file(filename, n):
    with open(filename, 'r') as file:
        num_lines = 9482 #VER
        lines = file.read().splitlines()[:num_lines]
        current_time = None
        current_particle = 0
        aux = []
        first_aux = 0
        data = []
        times= []
        
        for line in lines:
            if line.startswith("Time"):
                if current_time:
                    for i in range(n):
                        x, v = aux[i]
                        x_prev, v_prev = aux[(i - 1) % n]  
                        x_next, v_next = aux[(i + 1) % n]  
                        d_prev = abs(x - x_prev)
                        d_next = abs(x - x_next)
                        result = 1/(d_prev + d_next)
                        data.append((v, result)) #con esto alcanza?
                    aux = []
                current_time = float(line.split()[-1])
                times.append(current_time)
                current_particle = 0  
            elif line:
                x, v = map(float, line.split())
                if current_particle < n:
                    aux.append((x,v))
                    current_particle += 1
    
    return data

#ns = [5, 10, 15, 20, 25, 30]

ns =[10]
deltaT = 0.001 #ACA TIENE QUE SER EL QUE DIO EN EL OTRO EJ
data_dict = {} 

#for n in ns:
 #   velocities, times = read_file(f'outputs/particle_train_{n}_{deltaT}.txt', n)
  #  data_dict[n] = {'velocities': velocities, 'times': times}
    
data = read_file(f'outputs/particle_train_{10}_{deltaT}.txt', 10)
    

plt.figure(figsize=(8, 6))

v, d= zip(*data)
plt.plot(v, d, marker='o', linestyle='None' )

#for n, data in data_dict.items():
#    plt.plot(data['times'], data['velocities'], label=f'n = {n}')
plt.xlabel('Velocidad (UNIDAD)')
plt.ylabel('Densidad (UNIDAD)')
plt.legend()
plt.grid(True)
plt.show()