import numpy as np
import matplotlib.pyplot as plt


n=25 #ESTO TIENE Q SER 25


def read_files(filename1, filename2):
    with open(filename1, 'r') as file1, open(filename2, 'r') as file2 :
        num_lines = 9482 #VER
        lines1 = file1.read().splitlines()[:num_lines]
        lines2 = file2.read().splitlines()[:num_lines]
        current_time = None
        current_particle = 0
        aux = []
        phi = []
        times= []
        
        for line1, line2 in zip(lines1, lines2):
        
            if line1.startswith("Time") and line1.startswith("Time"):
                if current_time:
                    phi.append(sum(aux))
                    aux = []
                current_time = float(line1.split()[-1])
                print("time:", current_time)
                times.append(current_time)
                current_particle = 0  
            elif line1 and line2:
                x1, v1 = map(float, line1.split())
                x2, v2 = map(float, line2.split())

                if current_particle < n:
                    aux.append(np.abs(x2-x1))
                    current_particle += 1
    
    return phi

deltaT = [0.1, 0.01, 0.001, 0.0001]

#phi1 = read_files(f'outputs/particle_train_{n}_{deltaT[0]}.txt',f'outputs/particle_train_{n}_{deltaT[1]}.txt')
phi2 = read_files(f'outputs/l_particle_train_{n}_{deltaT[1]}.txt',f'outputs/l_particle_train_{n}_{deltaT[2]}.txt')
phi3 = read_files(f'outputs/l_particle_train_{n}_{deltaT[2]}.txt',f'outputs/l_particle_train_{n}_{deltaT[3]}.txt')

#tiene q ser: t = np.linspace(0, 180, 1801)
t = np.linspace(0, 43, 429)

print("t", len(t))
print("phi2", len(phi2))
print("phi3", len(phi3))


#Graphics
plt.figure(figsize=(8, 6))
#plt.plot(t, phi1, label='k=1', color='blue', linestyle='-')
plt.plot(t, phi2, label='k=2', color='cyan', marker='o', linestyle='None')
plt.plot(t, phi3, label='k=3', color='magenta', marker='o' , linestyle='None')
plt.xlabel('Tiempo (s)')
plt.ylabel('Phi(UNIDAD)')
plt.grid(True)
plt.show()