from .enum import Enum as Enum
from .file import File as File
from lark_oapi.core.construct import init as init

class PersonalProfile:
    personal_profile_id: str | None
    personal_profile_type: Enum | None
    files: list[File] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PersonalProfileBuilder: ...

class PersonalProfileBuilder:
    def __init__(self) -> None: ...
    def personal_profile_id(self, personal_profile_id: str) -> PersonalProfileBuilder: ...
    def personal_profile_type(self, personal_profile_type: Enum) -> PersonalProfileBuilder: ...
    def files(self, files: list[File]) -> PersonalProfileBuilder: ...
    def build(self) -> PersonalProfile: ...
