from src.qdlearn.core.genotype import Genotype, Population
from src.qdlearn.containers.map_elites import MAPEliteRepertoire

import numpy as np

def main():
    gen = Genotype(np.array([1,2,3]))
    pop = Population([gen, gen, gen])
    pop.append(gen)
    print(pop.values)
    
    mer = MAPEliteRepertoire(pop)
    mer.add(gen)
    print(mer.sample())
    
if __name__ == '__main__':
    main()