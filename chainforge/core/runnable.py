from abc import ABC, abstractmethod
from typing import Any

class Runnable(ABC):

    @abstractmethod
    def invoke(self, input: Any) -> Any:
        """Execute the runnable."""
        raise NotImplementedError

    
    
