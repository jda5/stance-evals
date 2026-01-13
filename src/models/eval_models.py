from datetime import datetime
from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel, Field

from models.message_models import Message
from models.response_models import ResponseFormatT


class Provider(StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class EvalInput(BaseModel):
    messages: list[Message]
    response_model: type[ResponseFormatT]


class EvalResult(BaseModel):
    input_messages: list[Message]
    response: type[ResponseFormatT] | None
    refusal: bool = False


class EvalRun(BaseModel):
    run_id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.now())
    model: str
    provider: Provider
    result: EvalResult
