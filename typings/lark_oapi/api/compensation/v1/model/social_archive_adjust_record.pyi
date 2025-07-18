from .social_archive_detail import SocialArchiveDetail as SocialArchiveDetail
from lark_oapi.core.construct import init as init

class SocialArchiveAdjustRecord:
    user_id: str | None
    record_type: str | None
    details: list[SocialArchiveDetail] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SocialArchiveAdjustRecordBuilder: ...

class SocialArchiveAdjustRecordBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: str) -> SocialArchiveAdjustRecordBuilder: ...
    def record_type(self, record_type: str) -> SocialArchiveAdjustRecordBuilder: ...
    def details(self, details: list[SocialArchiveDetail]) -> SocialArchiveAdjustRecordBuilder: ...
    def build(self) -> SocialArchiveAdjustRecord: ...
