from typing import Any, Type

from anthropic import Anthropic
from anthropic import AuthenticationError as AnthropicAuthenticationError

from clients.base_llm_client import BaseLLMClient
from config import ANTHROPIC_KEY
from errors import AuthenticationError, RefusalError
from models.message_models import Message
from models.response_models import ResponseFormatT


class AnthropicClient(BaseLLMClient):
    def __init__(self, model: str, betas: list[str] | None = None):
        self._client = Anthropic(api_key=ANTHROPIC_KEY)
        self.model = model
        self.betas = betas or ["structured-outputs-2025-11-13"]

    @staticmethod
    def _convert_messages(messages: list[Message]) -> list[dict[str, Any]]:
        return [message.model_dump(mode="json") for message in messages]

    async def generate_structured_output(
        self, messages: list[Message], response_model: Type[ResponseFormatT]
    ) -> ResponseFormatT:
        try:
            response = self._client.beta.messages.parse(
                model=self.model,
                betas=self.betas,
                max_tokens=1024,
                messages=self._convert_messages(messages),
                output_format=response_model,
            )
        except AnthropicAuthenticationError as e:
            raise AuthenticationError(str(e))

        if response.stop_reason == "refusal":
            raise RefusalError(
                f"model refused to generate response: {response.model_dump_json()}"
            )

        if response.parsed_output:
            return response.parsed_output

        raise RuntimeError(
            f"model did not generate a response in the expected format: {response.model_dump_json()}"
        )
