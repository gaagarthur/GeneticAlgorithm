import random
#import array
def initpopulation(size):
    population = []
    
    for i in range(0,size,1):
        x1 = round(random.uniform(-5.12, 5.12),8)
        x2 = round(random.uniform(-5.12, 5.12),8)
        population.append([x1,x2])
    return population

def weightscalc(pop):
    
    total = 0
    weights = []
    v =[]
    for i in range(0,len(pop)):
        v.append(round((1/pop[i][2]),8))
        total +=v[i]
    for i in v:
        aux = round(i/total,8)
        weights.append(aux)
    return weights

def championwarfare(pop, elitism=10.0):
    
    selected = []
    elit_pop = int(len(pop)*(elitism/100))
    champ_len = len(pop) - elit_pop
    for i in range(0,champ_len):
        champion_1 = random.randint(0,(len(pop)-1))
        champion_2 = random.randint(0,(len(pop)-1))

        if(pop[champion_1][2]<=pop[champion_2][2]):
            selected.append(pop[champion_1])
        else:
            selected.append(pop[champion_2])
    for i in range(0,elit_pop):
        selected.append(pop[i])
    return selected

def crossover(pop,chance=75, mutation_chance=5):

    new_pop =[]
    length = len(pop)
    ind = length -1
    plusminus = [-1, 1]
    chance_cross = [random.randint(0, 100) for _ in range(int(length/2))]
    chance_mutation = [random.randint(0, 100) for _ in range(2*length)]

    if(length%2.0!=0):
        ind -= 1

    for i in range(0,ind,2):
        
        if(chance_cross[int(i/2)]<chance):
            # (crossover parents i and i+1)            
            offspring = [0,0,0,0]
            #creates child 1
            offspring[0] = 0.7*pop[i][0] + 0.3*pop[i+1][0]
            offspring[1] = 0.7*pop[i][1] + 0.3*pop[i+1][1]
            #creates child 2
            offspring[2] = 0.3*pop[i][0] + 0.7*pop[i+1][0]
            offspring[3] = 0.3*pop[i][1] + 0.7*pop[i+1][1]

            aux_mutation = [random.randint(0, 1) for _ in range(4)]

            for j in range(0,4,1):
                index = (2*i)+j
                if(chance_mutation[index]<mutation_chance):
                    mutation = plusminus[aux_mutation[j]]*(random.uniform(0.01, 0.9))
                    offspring[j] = offspring[j] + (mutation)

            new_pop.append([round(offspring[0],8),round(offspring[1],8)])
            new_pop.append([round(offspring[2],8),round(offspring[3],8)])
        else:
            # append parents as childs (no crossover)
            x1_1 = pop[i][0]
            x2_1 = pop[i][1]           
            x1_2 = pop[i+1][0]
            x2_2 = pop[i+1][1]
            new_pop.append([x1_1,x2_1])
            new_pop.append([x1_2,x2_2])

    if(length%2.0!=0):
        x1 = pop[length-1][0]
        x2 = pop[length-1][1]
        new_pop.append([x1,x2])
        
    return new_pop
def averagefitness(pop):
    length = len(pop)
    sum = 0
    for i in range(length):
        sum += pop[i][2]
    return sum/length
   
