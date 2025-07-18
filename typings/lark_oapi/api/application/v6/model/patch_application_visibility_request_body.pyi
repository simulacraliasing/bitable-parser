from .app_visibility_id_list import AppVisibilityIdList as AppVisibilityIdList
from lark_oapi.core.construct import init as init

class PatchApplicationVisibilityRequestBody:
    add_visible_list: AppVisibilityIdList | None
    del_visible_list: AppVisibilityIdList | None
    add_invisible_list: AppVisibilityIdList | None
    del_invisible_list: AppVisibilityIdList | None
    is_visible_to_all: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PatchApplicationVisibilityRequestBodyBuilder: ...

class PatchApplicationVisibilityRequestBodyBuilder:
    def __init__(self) -> None: ...
    def add_visible_list(self, add_visible_list: AppVisibilityIdList) -> PatchApplicationVisibilityRequestBodyBuilder: ...
    def del_visible_list(self, del_visible_list: AppVisibilityIdList) -> PatchApplicationVisibilityRequestBodyBuilder: ...
    def add_invisible_list(self, add_invisible_list: AppVisibilityIdList) -> PatchApplicationVisibilityRequestBodyBuilder: ...
    def del_invisible_list(self, del_invisible_list: AppVisibilityIdList) -> PatchApplicationVisibilityRequestBodyBuilder: ...
    def is_visible_to_all(self, is_visible_to_all: bool) -> PatchApplicationVisibilityRequestBodyBuilder: ...
    def build(self) -> PatchApplicationVisibilityRequestBody: ...
