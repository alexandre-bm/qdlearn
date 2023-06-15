from src.qdlearn.function import FitnessScore 
from src.qdlearn.phenotype import Phenotype
from src.qdlearn.containers import Grid, Cell

import numpy as np

def main():
    ph = Phenotype(5)
    f = lambda x : 4 + x
    fitness = FitnessScore(f)
    print(fitness(ph))    
    
    bounds = np.vstack((np.zeros(3), np.ones(3)))
    mesh = 10 * np.ones(3)
    grid = Grid(bounds, mesh)
    print(grid.shape)

    c = Cell()
    c.push(1)
    c.push(2)
    c.push(1)
    print(c)

if __name__ == '__main__':
    main()