from typing import Any
from chainforge.core import Runnable

import json

class StrOutputParser(Runnable):
    """
    A simple output parser that converts the output of a chain into a string.
    """
    def invoke(self, input: Any) -> str:
        return str(input).strip()

class JsonOutputParser(Runnable):
    """
    A simple output parser that converts the output of a chain into a JSON object.
    """
    def invoke(self, input: Any) -> dict:
        if isinstance(input, dict):
            return input
        
        if not isinstance(input, str):
            raise ValueError("Input must be a string or a dictionary.")

        try:
            return json.loads(input)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Failed to parse JSON: {input}"
            ) from exc
        