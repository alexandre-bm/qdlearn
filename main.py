from src.qdlearn.core.genotype import Genotype, Population
from src.qdlearn.core.generator import Generator 
from src.qdlearn.containers.map_elites import MAPEliteRepertoire
from src.qdlearn.utils.logger import LOGGER

import numpy as np

def main(): 
    mer = MAPEliteRepertoire()
    g = np.array([1,2,3,4])
    pop = Population(np.array([[1,2,3,5], [1,3,4,123], [1,4,5,0]]))
    mer.add_genotype(g)
    mer.add_genotype(g)
    mer.add_genotype(np.array([2,4,0,9]), np.array([3,0]))
    mer.add_population(pop)
    print(mer.generators.values)

    

    
if __name__ == '__main__':
    main()