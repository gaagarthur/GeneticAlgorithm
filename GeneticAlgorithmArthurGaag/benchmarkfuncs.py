import numpy as np

def rastringinfunc(pop):
    
    length = len(pop)
    for i in range(length):
        x1 = pop[i][0]
        x2 = pop[i][1]
        temp1 = x1**2 - (10*np.cos(2*np.pi*x1))
        temp2 = x2**2 - (10*np.cos(2*np.pi*x2))
        y = temp1 + temp2 + 20
        y = round(float(y),8)
        pop[i].append(y)
    
    pop.sort(key=lambda x: x[2])
    min = pop[0][2]

    return min, pop
