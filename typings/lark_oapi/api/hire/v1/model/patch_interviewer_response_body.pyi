from .interviewer import Interviewer as Interviewer
from lark_oapi.core.construct import init as init

class PatchInterviewerResponseBody:
    interviewer: Interviewer | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchInterviewerResponseBodyBuilder: ...

class PatchInterviewerResponseBodyBuilder:
    def __init__(self) -> None: ...
    def interviewer(self, interviewer: Interviewer) -> PatchInterviewerResponseBodyBuilder: ...
    def build(self) -> PatchInterviewerResponseBody: ...
