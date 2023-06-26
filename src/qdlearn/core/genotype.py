from collections.abc import Sequence
from ..types import Genotype, Generator

import numpy as np
    
class Population(Sequence[Sequence]):
    
    def __init__(self, population: Sequence[Genotype]):
        self.capacity = len(population)
        self.population = population
        self.idx = len(self.values)
        
    def __getitem__(self, id:int) -> Genotype:
        if id >= self.idx:
            raise ValueError(f"Index {id} is not in the population")
        return self.values[id]
    
    def __len__(self) -> int:
        return self.idx
    
    @property
    def values(self):
        return self.population[~np.all(self.population == 0, axis=1)]
    
    def append(self, new_genotype: Genotype) -> None:
        if self.idx >= self.capacity:
            self._resize(self.capacity * 2)
        self.population[self.idx] = new_genotype
        self.idx += 1
    
    def _resize(self, new_capacity:int) -> None:
        population = np.zeros((new_capacity, self.population.shape[1]))
        population[:len(self.population)] = self.population
        self.population = population.astype(float)
    