from abc import ABC, abstractmethod
from typing import Type

from models.eval_models import Provider
from models.message_models import Message
from models.response_models import ResponseFormatT


class BaseLLMClient(ABC):
    def __init__(self, provider: Provider, model: str) -> None:
        self.provider = provider
        self.model = model

    @abstractmethod
    async def generate_structured_output(
        self, messages: list[Message], response_model: Type[ResponseFormatT]
    ) -> ResponseFormatT:
        pass
