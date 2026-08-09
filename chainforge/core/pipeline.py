from typing import Any

from .runnable import Runnable

class Pipeline(Runnable):
    def __init__(self, steps: list[Runnable]):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        result = input

        for step in self.steps:
            result = step.invoke(result)

        return result

        