from abc import ABC, abstractmethod
from typing import Callable, Tuple
from collections.abc import Sequence

from ..core.genotype import Population
from ..types import Genotype, Phenotype

class Function(ABC):
    
    @abstractmethod
    def __call__(self, phenotype:Phenotype) -> None:
        pass

class ScoringFunction(Function):

    def __init__(self, function:Callable[Population, Phenotype]) -> None:
        self.function = function
        super().__init__()

    def __call__(self, genotype: Population) -> Phenotype:
        return self.function(genotype)
    
    
class FitnessScore(Function):
    
    def __init__(self, function:Callable) -> None:
        self.function = function
    
    def __call__(self, phenotypes:Sequence[Phenotype]) -> Tuple[int, Phenotype]:
        return self.function(phenotypes)
    
    
class NoveltyScore(Function):
    
    def __init__(self) -> None:
        pass 
    
    def __call__(self) -> None:
        pass
    
    
class CuriosityScore(Function):
    
    def __init__(self) -> None:
        pass 
    
    def __call__(self) -> None:
        pass