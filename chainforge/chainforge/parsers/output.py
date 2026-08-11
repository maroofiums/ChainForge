import json
from typing import Any, Type, TypeVar

from pydantic import BaseModel, ValidationError

from chainforge.core import Runnable


T = TypeVar("T", bound=BaseModel)


class StrOutputParser(Runnable):

    """Parses string output."""

    def invoke(self, input: Any) -> str:
        return str(input).strip()


class JsonOutputParser(Runnable):

    """Parses JSON output."""

    def invoke(self, input: Any) -> dict:
        if isinstance(input, dict):
            return input

        if not isinstance(input, str):
            raise TypeError(
                "JsonOutputParser expects a string or dict"
            )

        text = input.strip()

        try:
            result = json.loads(text)

        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON output.\n"
                f"Raw output: {text}"
            ) from exc

        if not isinstance(result, dict):
            raise ValueError(
                "Expected JSON object, "
                f"got {type(result).__name__}"
            )

        return result

class PydanticOutputParser(Runnable):

    def __init__(self, model: Type[T]):
        if not issubclass(model, BaseModel):
            raise TypeError(
                "model must inherit from pydantic.BaseModel"
            )

        self.model = model

    def get_format_instructions(self) -> str:
        schema = self.model.model_json_schema()

        return (
            "Return ONLY valid JSON.\n\n"
            "The JSON must follow this schema:\n"
            f"{json.dumps(schema, indent=2)}"
        )

    def invoke(self, input: Any) -> T:

        if isinstance(input, self.model):
            return input

        if isinstance(input, str):
            try:
                data = json.loads(input)

            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON output:\n{input}"
                ) from exc

        elif isinstance(input, dict):
            data = input

        else:
            raise TypeError(
                "PydanticOutputParser expects "
                "a string, dict, or Pydantic model"
            )

        try:
            return self.model.model_validate(data)

        except ValidationError as exc:
            raise ValueError(
                f"Output validation failed:\n{exc}"
            ) from exc
    """
    Parses output into a Pydantic model.
    """
    def __init__(self, model: Type[T]):
        if not issubclass(model, BaseModel):
            raise TypeError(
                "model must inherit from pydantic.BaseModel"
            )

        self.model = model

    def get_format_instructions(self) -> str:
        schema = self.model.model_json_schema()

        return (
            "Return ONLY valid JSON.\n\n"
            "The JSON must follow this schema:\n"
            f"{json.dumps(schema, indent=2)}"
        )

    def invoke(self, input: Any) -> T:

        if isinstance(input, self.model):
            return input

        if isinstance(input, str):
            try:
                data = json.loads(input)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON output:\n{input}"
                ) from exc

        elif isinstance(input, dict):
            data = input

        else:
            raise TypeError(
                "PydanticOutputParser expects "
                "a string, dict, or Pydantic model"
            )

        try:
            return self.model.model_validate(data)

        except ValidationError as exc:
            raise ValueError(
                f"Output validation failed:\n{exc}"
            ) from exc