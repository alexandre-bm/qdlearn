from abc import ABC, abstractmethod
from ..core.genotype import Population, Genotype

class Repertoire(ABC):
    
    @abstractmethod
    def add_genotype(self, genotype:Genotype) -> None:
        pass
    
    @abstractmethod
    def get_genotype_by_id(self, id:int) -> Genotype:
        pass
    
    @abstractmethod
    def set_genotype_by_id(self, id:int, new_genotype:Genotype) -> None:
        pass
    
    @abstractmethod
    def del_genotype_by_id(self, id:int) -> None:
        pass 