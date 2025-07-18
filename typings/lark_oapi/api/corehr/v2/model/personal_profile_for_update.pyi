from .file import File as File
from lark_oapi.core.construct import init as init

class PersonalProfileForUpdate:
    personal_profile_type: str | None
    files: list[File] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PersonalProfileForUpdateBuilder: ...

class PersonalProfileForUpdateBuilder:
    def __init__(self) -> None: ...
    def personal_profile_type(self, personal_profile_type: str) -> PersonalProfileForUpdateBuilder: ...
    def files(self, files: list[File]) -> PersonalProfileForUpdateBuilder: ...
    def build(self) -> PersonalProfileForUpdate: ...
