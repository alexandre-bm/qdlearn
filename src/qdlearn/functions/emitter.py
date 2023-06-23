from abc import ABC, abstractmethod
from typing import Any

class Emitter(ABC):
    
    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)