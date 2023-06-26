from collections.abc import Sequence

class Generator(Sequence):
    
    def __init__(self, generators:Sequence) -> None:
        self.generators = generators
    
    def __getitem__(self, id:int) -> int:
        return self.generators[id]
    
    def __len__(self) -> int:
        return len(self.generators)
    

        
    
    def get_direct_child(self, id:int) -> int:
        return self.generators[id]
    
    def get_direct_parent(self, id:int) -> int:
        if self.generators[id] == 0:
            return None 
        else:
            return self.generators == id