import matplotlib.pyplot as plt
import numpy as np

def plotpop(pop, frame = 0):
    x1=[]
    x2=[]
    for i in range(len(pop)):
        x1.append(pop[i][0])
        x2.append(pop[i][1])

    axismin=-5.4
    axismax=5.4
    ax = plt.gca()
    plt.grid(True,color='#e3e3e3')
    ax.set_xlim([axismin, axismax])
    ax.set_ylim([axismin, axismax])
    plt.xticks(np.arange(axismin, axismax, 0.7))
    plt.yticks(np.arange(axismin, axismax, 0.7))

    plt.scatter(x1,x2,s=50)
    plt.savefig(f"./images/frame{frame}.png")
    plt.clf()

    