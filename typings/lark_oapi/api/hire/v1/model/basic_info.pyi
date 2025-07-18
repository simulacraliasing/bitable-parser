from .identification import Identification as Identification
from lark_oapi.core.construct import init as init

class BasicInfo:
    name: str | None
    mobile: str | None
    mobile_country_code: str | None
    email: str | None
    birthday: int | None
    confidentiality: int | None
    creator_account_type: int | None
    creator_id: str | None
    current_city_code: str | None
    gender: int | None
    hometown_city_code: str | None
    identification: Identification | None
    init_source_id: str | None
    nationality_id: str | None
    resume_attachment_id: str | None
    self_evaluation: str | None
    start_work_time: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BasicInfoBuilder: ...

class BasicInfoBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> BasicInfoBuilder: ...
    def mobile(self, mobile: str) -> BasicInfoBuilder: ...
    def mobile_country_code(self, mobile_country_code: str) -> BasicInfoBuilder: ...
    def email(self, email: str) -> BasicInfoBuilder: ...
    def birthday(self, birthday: int) -> BasicInfoBuilder: ...
    def confidentiality(self, confidentiality: int) -> BasicInfoBuilder: ...
    def creator_account_type(self, creator_account_type: int) -> BasicInfoBuilder: ...
    def creator_id(self, creator_id: str) -> BasicInfoBuilder: ...
    def current_city_code(self, current_city_code: str) -> BasicInfoBuilder: ...
    def gender(self, gender: int) -> BasicInfoBuilder: ...
    def hometown_city_code(self, hometown_city_code: str) -> BasicInfoBuilder: ...
    def identification(self, identification: Identification) -> BasicInfoBuilder: ...
    def init_source_id(self, init_source_id: str) -> BasicInfoBuilder: ...
    def nationality_id(self, nationality_id: str) -> BasicInfoBuilder: ...
    def resume_attachment_id(self, resume_attachment_id: str) -> BasicInfoBuilder: ...
    def self_evaluation(self, self_evaluation: str) -> BasicInfoBuilder: ...
    def start_work_time(self, start_work_time: int) -> BasicInfoBuilder: ...
    def build(self) -> BasicInfo: ...
