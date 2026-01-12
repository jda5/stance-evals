from enum import StrEnum
from typing import TypeVar

from pydantic import BaseModel

# Any subtype of BaseModel
ResponseFormatT = TypeVar("ResponseFormatT", bound=BaseModel)


class AgreementLevel(StrEnum):
    STRONGLY_DISAGREE = "strongly disagree"
    DISAGREE = "disagree"
    AGREE = "agree"
    STRONGLY_AGREE = "strongly agree"


class SurveyResponse(BaseModel):
    level: AgreementLevel
    explanation: str
