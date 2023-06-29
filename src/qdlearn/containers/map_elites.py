from collections.abc import Sequence

from ..types import Phenotype, Generator
from .repertoire import Repertoire
from ..functions.function import ScoringFunction
from ..core.genotype import Genotype, Population

import numpy as np

class MAPEliteRepertoire(Repertoire):
    
    def __init__(
        self, 
        population:Population = Population(np.zeros((10,4))),
        generators:Population = Population(np.zeros((10,2))),
        phenotypes:Sequence[Phenotype] = None
        ) -> None:
        self.population = population
        self.generators = generators
        self.phenotype = phenotypes
    
    def add_genotype(self, genotype:Genotype, generator:Generator = None) -> None:
        self.population.append(genotype)
        if not isinstance(generator, type(None)):
            self.generators.append(generator)
        else:
            self.generators.append(np.array([self.population.idx, -1]))
        
    def add_population(self, population:Population) -> None:
        for _, item in enumerate(population.values):
            self.add_genotype(item)

    def evaluate_population(self, scoring_function:ScoringFunction) -> None:
        if isinstance(self.phenotype, type(None)):
            self.phenotype = scoring_function(self.population.values)
    
    def get_genotype_by_id(self, id:int) -> Genotype:
        return self.population.__getitem__(id)
    
    def set_genotype_by_id(self, id:int, new_genotype:Genotype) -> None:
        pass
    
    def del_genotype_by_id(self, id:int) -> None:
        pass 
    
    
        