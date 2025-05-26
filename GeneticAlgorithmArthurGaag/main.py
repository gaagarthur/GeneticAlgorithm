
import auxfuncsGA as ag
import plotting as pt
from benchmarkfuncs import rastringinfunc

population_size = 20,
max_iter = 100,
crossover_chance = 80,
mutation_chance = 6,
elitism=20

iter = 0
delta_min =0.0054
average = 9999999 #high number just to start

#====================initialize population==================
pop = ag.initpopulation(population_size)

    #pt.plotpop(pop,iter) #plot initial population

#===================calculate the fitness========================
min, pop = rastringinfunc(pop)

#==========Difference between best and average fitness ==============
delta = abs(ag.averagefitness(pop)-min)

#=== Iterates generations until it either converges
#=== or reaches max number of iterations
while((iter<max_iter) and (delta_min<delta)):

    #chooses which individuals will pass on their genes
    pop = ag.championwarfare(pop, elitism)

    #creates a new generation with mutations
    pop = ag.crossover(pop,crossover_chance, mutation_chance)

    #calculate the fitness of new gen
    min, pop = rastringinfunc(pop)

    iter+=1
    #Difference between best and average fitness
    delta = abs(ag.averagefitness(pop)-min)

        #pt.plotpop(pop,iter)

print(f"\nAfter {iter} iterations the minimun found was = {min}, at x1:{pop[0][0]}, x2:{pop[0][1]}\n\n")







