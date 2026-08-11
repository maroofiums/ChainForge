from chainforge.core import Runnable
from abc import abstractmethod

import json

class BaseLLM(Runnable):

    @property
    @abstractmethod
    def model_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def invoke(self, prompt: str) -> str:
        raise NotImplementedError


class FakeLLM(BaseLLM):

    def __init__(self, model_name="fake-model"):
        self._model_name = model_name

    @property
    def model_name(self) -> str:
        return self._model_name

    def invoke(self, prompt: str) -> str:
        return f"[{self.model_name}] Response to: {prompt}"


class ReverseLLM(BaseLLM):

    def __init__(self, model_name="reverse-model"):
        self._model_name = model_name

    @property
    def model_name(self) -> str:
        return self._model_name

    def invoke(self, prompt: str) -> str:
        return prompt[::-1]

class JsonFakeLLM(BaseLLM):

    def __init__(
        self,
        response: dict,
        model_name="json-fake-model",
    ):
        self._model_name = model_name
        self.response = response

    @property
    def model_name(self) -> str:
        return self._model_name

    def invoke(self, prompt: str) -> str:
        return json.dumps(self.response)