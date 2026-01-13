from typing import Any, Type

from openai import AsyncOpenAI
from openai import AuthenticationError as OpenAIAuthenticationError

from clients.base_llm_client import BaseLLMClient
from config import OPENAI_KEY
from errors import AuthenticationError, RefusalError
from models.eval_models import Provider
from models.message_models import Message
from models.response_models import ResponseFormatT


class OpenAIClient(BaseLLMClient):
    def __init__(self, model: str):
        super().__init__(Provider.OPENAI, model)
        self._client = AsyncOpenAI(api_key=OPENAI_KEY)

    @staticmethod
    def _convert_messages(messages: list[Message]) -> list[dict[str, Any]]:
        return [message.model_dump(mode="json") for message in messages]

    async def generate_structured_output(
        self, messages: list[Message], response_model: Type[ResponseFormatT]
    ) -> ResponseFormatT:
        try:
            completion = await self._client.beta.chat.completions.parse(
                model=self.model,
                messages=self._convert_messages(messages),
                response_format=response_model,
            )
        except OpenAIAuthenticationError as e:
            raise AuthenticationError(str(e))

        response = completion.choices[0].message
        if response.refusal:
            raise RefusalError(
                f"model refused to generate response: {response.refusal}"
            )

        if not response.parsed:
            raise RuntimeError(
                f"model did not generate a response in the expected format: {response.model_dump_json()}"
            )

        return response.parsed
