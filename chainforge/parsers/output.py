from typing import Any
from chainforge.core import Runnable

class StrOutputParser(Runnable):
    """
    A simple output parser that converts the output of a chain into a string.
    """
    def invoke(self, input: Any) -> str:
        return str(input).split()