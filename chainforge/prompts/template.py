from string import Formatter
from typing import Any, Dict, List

from chainforge.core import Runnable


class PromptTemplate(Runnable):

    def __init__(self, template: str):
        self.template = template
        self.input_variables = self._extract_variables()

    def _extract_variables(self) -> List[str]:
        variables = []

        for _, field_name, _, _ in Formatter().parse(self.template):
            if field_name is not None:
                variables.append(field_name)

        return list(dict.fromkeys(variables))

    def format(self, **kwargs: Any) -> str:
        self._validate_inputs(kwargs)

        return self.template.format(**kwargs)

    def _validate_inputs(self, kwargs: Dict[str, Any]) -> None:
        missing = [
            variable
            for variable in self.input_variables
            if variable not in kwargs
        ]

        if missing:
            raise ValueError(
                f"Missing variables: {missing}"
            )

    def invoke(self, input: Dict[str, Any]) -> str:
        return self.format(**input)