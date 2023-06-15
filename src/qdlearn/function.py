from abc import ABC, abstractmethod
from typing import Callable

from .phenotype import Phenotype

class ScoreFunction(ABC):
    
    @abstractmethod
    def __call__(self, phenotype:Phenotype) -> None:
        pass
    
    
class FitnessScore(ScoreFunction):
    
    def __init__(self, function:Callable) -> None:
        self.function = function
    
    def __call__(self, phenotype:Phenotype) -> None:
        return self.function(phenotype.value)
    
    
class NoveltyScore(ScoreFunction):
    
    def __init__(self) -> None:
        pass 
    
    def __call__(self) -> None:
        pass
    
    
class CuriosityScore(ScoreFunction):
    
    def __init__(self) -> None:
        pass 
    
    def __call__(self) -> None:
        pass