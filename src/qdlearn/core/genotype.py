from __future__ import annotations

from collections.abc import Sequence, MutableSequence

import numpy as np

class Genotype:
    
    def __init__(self, genotype: Sequence) -> None:
        super().__init__()
        self.genotype = genotype
        
    @property
    def values(self):
        return self.genotype
    
    
class Population(MutableSequence):
    
    def __init__(self, population: Sequence[Genotype]):
        self.population = population
        
    def __delitem__(self, genotype:Genotype) -> None:
        return super().__delitem__()
        
    def __getitem__(self, genotype:Genotype) -> None:
        return super().__getitem__()
        
    def __setitem__(self, genotype:Genotype, new_genotype:Genotype) -> None:
        return super().__setitem__()
        
    def __len__(self) -> int:
        return len(self.population)
    
    @property
    def values(self):
            return np.array([self.population[k].values for k in range(len(self))])
    
    def append(self, new_genotype: Genotype) -> Population:
        self.population.append(new_genotype)
        return self
        
    def insert(self, new_genotype: Genotype) -> None:
        pass
        
    def sample(self, idx: int) -> Genotype:
        return self.population[idx]
    
    