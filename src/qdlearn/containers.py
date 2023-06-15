from abc import ABC, abstractmethod

from numpy import ndarray

from .base import Item

class Stack(ABC):
    
    @abstractmethod
    def push(self, item:Item) -> None:
        pass 
    
    @abstractmethod
    def top(self) -> Item:
        pass
    
    @abstractmethod
    def pop(self) -> None:
        pass

class Cell(Stack):
    
    def __init__(self) -> None:
        self.id = id(self)
        self.cell = []
    
    def push(self, item:Item) -> None:
        if self.cell == []:
            self.cell.append(item)
        elif item > self.top():
            self.cell.append(item)
        else:
            top = self.pop()
            self.cell.append(item)
            self.cell.append(top)
        
    
    def top(self) -> Item:
        return self.cell[-1]
    
    def pop(self) -> Item:
        try:
            return self.cell.pop()
        except:
            raise ValueError(f"Cell {self.id} is empty")
        
    def __str__(self):
        return f"{self.cell}"

    
class Grid: 
     
    def __init__(self, bounds:ndarray, mesh:ndarray) -> None:
        """_summary_

        Args:
            bounds (ndarray): (n,2) array with lower and upper bounds
            mesh (ndarray): (n,) array with number of points per feature
        """
        self.bounds = bounds
        self.mesh = mesh
        
    def inputs_health_check(self):
        grid_shape = self.bounds.shape[0] == 2
        grid_mesh = self.bounds.shape[1] == self.mesh.shape[0]
        return grid_shape & grid_mesh
    
    @property
    def shape(self):
        return f"({[self.mesh[i] for i in range(len(self.mesh))]})"
    
    @property
    def size(self):
        return self.mesh.prod()
    
        
    