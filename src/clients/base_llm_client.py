from abc import ABC, abstractmethod
from typing import Type

from models.message_models import Message
from models.response_models import ResponseFormatT


class BaseLLMClient(ABC):
    @abstractmethod
    async def generate_structured_output(
        self, messages: list[Message], response_model: Type[ResponseFormatT]
    ) -> ResponseFormatT:
        pass
