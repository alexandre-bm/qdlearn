from __future__ import annotations

from collections.abc import Sequence

from .repertoire import Repertoire
from ..core.genotype import Genotype, Population

import numpy as np

class MAPEliteRepertoire(Repertoire):
    
    def __init__(self, population: Population = None) -> None:
        self.population = population
    
    def add(self, new_genotype: Sequence[Genotype]) -> MAPEliteRepertoire:
        self.population.append(new_genotype)
        
    def sample(self, strategy: str = 'random') -> Sequence[Genotype]:
        if strategy == "random":
            idx = np.random.randint(0,len(self.population))
        else:
            idx = 1
        return self.population.sample(idx)
        