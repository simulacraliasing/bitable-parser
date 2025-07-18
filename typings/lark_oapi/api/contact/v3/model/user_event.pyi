from .avatar_info import AvatarInfo as AvatarInfo
from .user_custom_attr import UserCustomAttr as UserCustomAttr
from .user_order import UserOrder as UserOrder
from .user_position import UserPosition as UserPosition
from .user_status import UserStatus as UserStatus
from lark_oapi.core.construct import init as init

class UserEvent:
    open_id: str | None
    union_id: str | None
    user_id: str | None
    name: str | None
    en_name: str | None
    nickname: str | None
    email: str | None
    enterprise_email: str | None
    job_title: str | None
    mobile: str | None
    mobile_visible: bool | None
    gender: int | None
    avatar: AvatarInfo | None
    status: UserStatus | None
    department_ids: list[str] | None
    leader_user_id: str | None
    city: str | None
    country: str | None
    work_station: str | None
    join_time: int | None
    is_tenant_manager: bool | None
    employee_no: str | None
    employee_type: int | None
    positions: list[UserPosition] | None
    orders: list[UserOrder] | None
    time_zone: str | None
    custom_attrs: list[UserCustomAttr] | None
    job_level_id: str | None
    job_family_id: str | None
    dotted_line_leader_user_ids: list[int] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> UserEventBuilder: ...

class UserEventBuilder:
    def __init__(self) -> None: ...
    def open_id(self, open_id: str) -> UserEventBuilder: ...
    def union_id(self, union_id: str) -> UserEventBuilder: ...
    def user_id(self, user_id: str) -> UserEventBuilder: ...
    def name(self, name: str) -> UserEventBuilder: ...
    def en_name(self, en_name: str) -> UserEventBuilder: ...
    def nickname(self, nickname: str) -> UserEventBuilder: ...
    def email(self, email: str) -> UserEventBuilder: ...
    def enterprise_email(self, enterprise_email: str) -> UserEventBuilder: ...
    def job_title(self, job_title: str) -> UserEventBuilder: ...
    def mobile(self, mobile: str) -> UserEventBuilder: ...
    def mobile_visible(self, mobile_visible: bool) -> UserEventBuilder: ...
    def gender(self, gender: int) -> UserEventBuilder: ...
    def avatar(self, avatar: AvatarInfo) -> UserEventBuilder: ...
    def status(self, status: UserStatus) -> UserEventBuilder: ...
    def department_ids(self, department_ids: list[str]) -> UserEventBuilder: ...
    def leader_user_id(self, leader_user_id: str) -> UserEventBuilder: ...
    def city(self, city: str) -> UserEventBuilder: ...
    def country(self, country: str) -> UserEventBuilder: ...
    def work_station(self, work_station: str) -> UserEventBuilder: ...
    def join_time(self, join_time: int) -> UserEventBuilder: ...
    def is_tenant_manager(self, is_tenant_manager: bool) -> UserEventBuilder: ...
    def employee_no(self, employee_no: str) -> UserEventBuilder: ...
    def employee_type(self, employee_type: int) -> UserEventBuilder: ...
    def positions(self, positions: list[UserPosition]) -> UserEventBuilder: ...
    def orders(self, orders: list[UserOrder]) -> UserEventBuilder: ...
    def time_zone(self, time_zone: str) -> UserEventBuilder: ...
    def custom_attrs(self, custom_attrs: list[UserCustomAttr]) -> UserEventBuilder: ...
    def job_level_id(self, job_level_id: str) -> UserEventBuilder: ...
    def job_family_id(self, job_family_id: str) -> UserEventBuilder: ...
    def dotted_line_leader_user_ids(self, dotted_line_leader_user_ids: list[int]) -> UserEventBuilder: ...
    def build(self) -> UserEvent: ...
