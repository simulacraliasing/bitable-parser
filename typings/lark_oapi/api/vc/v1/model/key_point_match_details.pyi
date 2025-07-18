from .key_point_match_detail import KeyPointMatchDetail as KeyPointMatchDetail
from lark_oapi.core.construct import init as init

class KeyPointMatchDetails:
    key_point_match_details: list[KeyPointMatchDetail] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> KeyPointMatchDetailsBuilder: ...

class KeyPointMatchDetailsBuilder:
    def __init__(self) -> None: ...
    def key_point_match_details(self, key_point_match_details: list[KeyPointMatchDetail]) -> KeyPointMatchDetailsBuilder: ...
    def build(self) -> KeyPointMatchDetails: ...
