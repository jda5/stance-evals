from pydantic import BaseModel

from enum import StrEnum



class MessageRole(StrEnum):
    user = "user"
    assistant = "assistant"
    system = "system"



class Message(BaseModel):
    role: MessageRole
    content: str