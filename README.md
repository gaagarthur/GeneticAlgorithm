## ARTHUR GAAG - 20230087350


### OBJECTIVE




The objective of this assignment is to implement a metaheuristic and use it to solve a real-life or academic problem.


---


 
### THE METAHEURISTIC


The Metaheuristic chosen is the Genetic Algorithm or GA. GA is a population based, nature inspired algorithm that tries to replicate properties of evolution such as selecting partners based on fitness, having offspring or not, and mutations, so as to manipulate this artificial population into converging to an optimum solution. The pseudocode for the GA is as follows.


#### PSEUDOCODE
 
````
Choose an initial population of chromosomes;
while termination condition not satisfied do
    Repeat
        if crossover condition satisfied then
        {select parent chromosomes;
        choose crossover parameters;
        perform crossover};
        if mutation condition satisfied then
        {choose mutation points;
        perform mutation};
        evaluate fitness of offspring
    until sufficient offspring created;
select new population;
endwhile 
````
GENDREAU, M.; POTVIN, J.-Y. 2012
Some of the parameters used are population size, crossover chance, mutation chance, number max of iterations and elitism rate.


---


### THE PROBLEM


The problem selected to apply the genetic algorithm is the Rastrigins’s function with two dimensions (eq.1). This function is a well known benchmark function, used to test optimization methods, since it has multiple local minima distributed periodically throughout the search space, making it a tough but good assessment for the implementation made.


$R_{\text{astrigin}}(x_{1}, x_{2}) = 20 + \sum_{i=1}^{2} \left[ x_{i}^{2} - 10\cos(2\pi x_{i}) \right]$


---


### IMPLEMENTATION


For the implementation section, in order to keep the main as clean as possible, the code was spread into four files:
|File name|Description|
|----|----|
|main|Set some parameters and call functions based on GA|
|benchmarkfuncs|attributes fitness of individuals (Rastrigin’s func)|
|auxfuncsGA|functions used on GA: initpopulation(), crossover(), etc|
|potting|plotts different population on graph|


#### The main parts of the algorithm (main)
````python
- 1 Initialize population: parameters(size) # runs once
When initializing the population the best practice is to randomize the population  values. It returns a list of lists (pop). EX: pop = [[x1,x2],[x1,x2],[x1,x2],...]


while begins


- 2 Apply fitness function: parameters(pop)
Returns the minimum value and the pop with a third item in the inner list. EX: min_value, pop = [[x1,x2,v],[x1,x2,v],[x1,x2,v],...]


- 3 Select individuals for the chance to reproduce: parameters(pop, elitism)
Return a pop list with the same structure as before (2), with the chosen individuals.


- 4 Crossover/mutation: parameters(pop,crossover_chance, mutation_chance)
Returns a pop list, with the offspring with the mutations applied already.


while ends
- 5 show results: min_value at pop[0][0], pop[0][1]


````




–--


### HOW TO RUN
````
To run the algorithm: 
1 All file .py (other than plotting because it's commented) must be in the same directory.
2 Set the parameters on main.py
3 Run main.py
````


---


### RESULTS


For each set of parameters the program ran 10000 times.
The parameters in first column are: popsize, iterlimit , crossover, mutation, elitism)


|Parameters|best|worst|average|avg_value iterations|
|---|---|---|---|---|
|10, 1000, 75%, 2%, 10%|0.00002001|32.01010055|6.3335|12.3379|
|15, 1000, 75%, 2%, 10%|0.00000112|19.28972011|2.8217|15.8243|
|20, 1000, 75%, 2%, 10%|0.00000006|21.85844078|2.415|15.7424|
|25, 1000, 75%, 2%, 10%|0.00000002|13.29979748|1.8065|18.1437|
|30, 1000, 75%, 2%, 10%|0.00000000|11.81844551|1.498|18.3199|
|15, 1000, 65%, 2%, 10%|0.00000006|20.11202449|3.3595|14.3465|
|15, 1000, 70%, 2%, 10%|0.00000027|21.12426984|3.0595|14.9389|
|15, 1000, 75%, 2%, 10%|0.00000010|19.52447273|2.3921|15.6774|
|15, 1000, 80%, 2%, 10%|0.00000007|20.727604|2.622|16.6387|
|15, 1000, 85%, 2%, 10%|0.00000152|17.38864987|2.405|17.5852|
|15, 1000, 75%, 1%, 10%|0.00000477|20.42293935|3.0291|14.7323|
|15, 1000, 75%, 4%, 10%|0.00000002|17.34905964|1.8788|21.5781|
|15, 1000, 75%, 6%, 10%|0.00000000|17.08713949|1.7418|25.1558|
|15, 1000, 75%, 8%, 10%|0.00000033|16.08830616|1.8871|26.737|
|15, 1000, 75%, 10%, 10%|0.00000000|18.2403492|1.6417|34.3822|
|15, 1000, 75%, 2%, 5%|0.00006371|32.05226712|4.8057|18.7386|
|15, 1000, 75%, 2%, 15%|0.00000307|23.87483776|3.7005|14.002|
|15, 1000, 75%, 2%, 20%|0.00000028|18.17798413|2.6726|14.487|
|15, 1000, 75%, 2%, 25%|0.00000141|21.04741757|4.057|12.7929|
|15, 1000, 75%, 2%, 30%|0.00000591|22.2225075|4.349|12.9463|


---

### CONCLUSION

Overall all of the cenarios testes resulted in values close to the global minima, which would be equals
to 0 at (0,0). By going purely by these results a well ajusted set of parametes would be:
````python
population size = 20
max_iteration was never reached
crossover = 80
mutation = 6
elitism = 20 
````

---


### REFERENCES
GENDREAU, M.; POTVIN, J.-Y. Handbook of Metaheuristics. [s.l.] Springer, 2012. 




 

