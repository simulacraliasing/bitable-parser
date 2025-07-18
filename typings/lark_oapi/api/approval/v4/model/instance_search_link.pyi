from lark_oapi.core.construct import init as init

class InstanceSearchLink:
    pc_link: str | None
    mobile_link: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InstanceSearchLinkBuilder: ...

class InstanceSearchLinkBuilder:
    def __init__(self) -> None: ...
    def pc_link(self, pc_link: str) -> InstanceSearchLinkBuilder: ...
    def mobile_link(self, mobile_link: str) -> InstanceSearchLinkBuilder: ...
    def build(self) -> InstanceSearchLink: ...
