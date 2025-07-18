from lark_oapi.core.construct import init as init

class Gadget:
    enable_pc_mode: int | None
    schema_urls: list[str] | None
    pc_use_mobile_pkg: bool | None
    pc_version: str | None
    mobile_version: str | None
    mobile_min_lark_version: str | None
    pc_min_lark_version: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GadgetBuilder: ...

class GadgetBuilder:
    def __init__(self) -> None: ...
    def enable_pc_mode(self, enable_pc_mode: int) -> GadgetBuilder: ...
    def schema_urls(self, schema_urls: list[str]) -> GadgetBuilder: ...
    def pc_use_mobile_pkg(self, pc_use_mobile_pkg: bool) -> GadgetBuilder: ...
    def pc_version(self, pc_version: str) -> GadgetBuilder: ...
    def mobile_version(self, mobile_version: str) -> GadgetBuilder: ...
    def mobile_min_lark_version(self, mobile_min_lark_version: str) -> GadgetBuilder: ...
    def pc_min_lark_version(self, pc_min_lark_version: str) -> GadgetBuilder: ...
    def build(self) -> Gadget: ...
