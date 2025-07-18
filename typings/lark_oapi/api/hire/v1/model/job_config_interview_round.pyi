from .id_name_object import IdNameObject as IdNameObject
from lark_oapi.core.construct import init as init

class JobConfigInterviewRound:
    interviewer_list: list[IdNameObject] | None
    round: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> JobConfigInterviewRoundBuilder: ...

class JobConfigInterviewRoundBuilder:
    def __init__(self) -> None: ...
    def interviewer_list(self, interviewer_list: list[IdNameObject]) -> JobConfigInterviewRoundBuilder: ...
    def round(self, round: int) -> JobConfigInterviewRoundBuilder: ...
    def build(self) -> JobConfigInterviewRound: ...
