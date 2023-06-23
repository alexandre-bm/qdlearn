from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence

from ..core.genotype import Population, Genotype

class Repertoire(ABC):
    
    @abstractmethod
    def add(self, genotype:Sequence[Genotype]) -> Repertoire:
        pass
    
    @abstractmethod
    def sample(self) -> Sequence[Genotype]:
        pass
    