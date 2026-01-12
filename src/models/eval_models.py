from pydantic import BaseModel

from models.message_models import Message
from models.response_models import ResponseFormatT


class Evaluation(BaseModel):
    messages: list[Message]
    response_model: type[ResponseFormatT]
