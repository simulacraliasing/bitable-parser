from .space_cover_info import SpaceCoverInfo as SpaceCoverInfo
from .space_home_page import SpaceHomePage as SpaceHomePage
from lark_oapi.core.construct import init as init

class Space:
    space_id: str | None
    name: str | None
    description: str | None
    avatar_url: str | None
    tenant_id: str | None
    domain: str | None
    is_cross_tenant: bool | None
    default_attr: int | None
    home_page: SpaceHomePage | None
    cover_info: SpaceCoverInfo | None
    version: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SpaceBuilder: ...

class SpaceBuilder:
    def __init__(self) -> None: ...
    def space_id(self, space_id: str) -> SpaceBuilder: ...
    def name(self, name: str) -> SpaceBuilder: ...
    def description(self, description: str) -> SpaceBuilder: ...
    def avatar_url(self, avatar_url: str) -> SpaceBuilder: ...
    def tenant_id(self, tenant_id: str) -> SpaceBuilder: ...
    def domain(self, domain: str) -> SpaceBuilder: ...
    def is_cross_tenant(self, is_cross_tenant: bool) -> SpaceBuilder: ...
    def default_attr(self, default_attr: int) -> SpaceBuilder: ...
    def home_page(self, home_page: SpaceHomePage) -> SpaceBuilder: ...
    def cover_info(self, cover_info: SpaceCoverInfo) -> SpaceBuilder: ...
    def version(self, version: int) -> SpaceBuilder: ...
    def build(self) -> Space: ...
