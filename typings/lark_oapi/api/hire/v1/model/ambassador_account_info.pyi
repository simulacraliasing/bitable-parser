from lark_oapi.core.construct import init as init

class AmbassadorAccountInfo:
    id: str | None
    name: str | None
    mobile_code: str | None
    mobile_number: str | None
    email_address: str | None
    remark: str | None
    related_school: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AmbassadorAccountInfoBuilder: ...

class AmbassadorAccountInfoBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> AmbassadorAccountInfoBuilder: ...
    def name(self, name: str) -> AmbassadorAccountInfoBuilder: ...
    def mobile_code(self, mobile_code: str) -> AmbassadorAccountInfoBuilder: ...
    def mobile_number(self, mobile_number: str) -> AmbassadorAccountInfoBuilder: ...
    def email_address(self, email_address: str) -> AmbassadorAccountInfoBuilder: ...
    def remark(self, remark: str) -> AmbassadorAccountInfoBuilder: ...
    def related_school(self, related_school: str) -> AmbassadorAccountInfoBuilder: ...
    def build(self) -> AmbassadorAccountInfo: ...
