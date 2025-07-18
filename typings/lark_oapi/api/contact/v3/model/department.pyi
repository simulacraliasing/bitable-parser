from .department_i18n_name import DepartmentI18nName as DepartmentI18nName
from .department_leader import DepartmentLeader as DepartmentLeader
from .department_status import DepartmentStatus as DepartmentStatus
from lark_oapi.core.construct import init as init

class Department:
    name: str | None
    i18n_name: DepartmentI18nName | None
    parent_department_id: str | None
    department_id: str | None
    open_department_id: str | None
    leader_user_id: str | None
    chat_id: str | None
    order: int | None
    unit_ids: list[str] | None
    member_count: int | None
    status: DepartmentStatus | None
    create_group_chat: bool | None
    leaders: list[DepartmentLeader] | None
    group_chat_employee_types: list[int] | None
    department_hrbps: list[str] | None
    primary_member_count: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DepartmentBuilder: ...

class DepartmentBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> DepartmentBuilder: ...
    def i18n_name(self, i18n_name: DepartmentI18nName) -> DepartmentBuilder: ...
    def parent_department_id(self, parent_department_id: str) -> DepartmentBuilder: ...
    def department_id(self, department_id: str) -> DepartmentBuilder: ...
    def open_department_id(self, open_department_id: str) -> DepartmentBuilder: ...
    def leader_user_id(self, leader_user_id: str) -> DepartmentBuilder: ...
    def chat_id(self, chat_id: str) -> DepartmentBuilder: ...
    def order(self, order: int) -> DepartmentBuilder: ...
    def unit_ids(self, unit_ids: list[str]) -> DepartmentBuilder: ...
    def member_count(self, member_count: int) -> DepartmentBuilder: ...
    def status(self, status: DepartmentStatus) -> DepartmentBuilder: ...
    def create_group_chat(self, create_group_chat: bool) -> DepartmentBuilder: ...
    def leaders(self, leaders: list[DepartmentLeader]) -> DepartmentBuilder: ...
    def group_chat_employee_types(self, group_chat_employee_types: list[int]) -> DepartmentBuilder: ...
    def department_hrbps(self, department_hrbps: list[str]) -> DepartmentBuilder: ...
    def primary_member_count(self, primary_member_count: int) -> DepartmentBuilder: ...
    def build(self) -> Department: ...
