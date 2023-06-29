from src.qdlearn.core.genotype import Genotype, Population
from src.qdlearn.core.generator import Generator 
from src.qdlearn.containers.map_elites import MAPEliteRepertoire
from src.qdlearn.utils.logger import LOGGER
from src.qdlearn.algorithms.map_elites import MAPElite

from src.qdlearn.functions.function import ScoringFunction, FitnessScore

import numpy as np


def f(x):
    return (x + np.sin(x) * x - 2).sum(axis=1)

def fitness(y):
    return (y.argmax(), y.max())



def main(): 

    scoring_function = ScoringFunction(f)
    fitness_function = FitnessScore(fitness)

    pop = Population(np.array([[1,2,3,5], [1,3,4,123], [1,4,5,0]]))
    mer = MAPEliteRepertoire(pop)
    g = np.array([1,2,3,4])
    mer.add_genotype(g)
    mer.add_genotype(g)
    mer.add_genotype(np.array([2,4,0,9]), np.array([3,0]))
    print(mer.population.values)
    mer.add_population(pop)
    
    mer.evaluate_population(scoring_function)

   
    me = MAPElite(mer, scoring_function, fitness_function)

    print(fitness_function(mer.phenotype))

    

    
if __name__ == '__main__':
    main()