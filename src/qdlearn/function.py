from abc import ABC, abstractmethod

class BaseFunction(ABC):
    
    @abstractmethod
    def __call__(self) -> None:
        pass
    
    
class FitnessFunction(BaseFunction):
    
    def __init__(self):
        pass 
    
    def __call__(self) -> None:
        pass