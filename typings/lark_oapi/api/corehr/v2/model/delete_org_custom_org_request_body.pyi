from lark_oapi.core.construct import init as init

class DeleteOrgCustomOrgRequestBody:
    org_id: str | None
    object_api_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DeleteOrgCustomOrgRequestBodyBuilder: ...

class DeleteOrgCustomOrgRequestBodyBuilder:
    def __init__(self) -> None: ...
    def org_id(self, org_id: str) -> DeleteOrgCustomOrgRequestBodyBuilder: ...
    def object_api_name(self, object_api_name: str) -> DeleteOrgCustomOrgRequestBodyBuilder: ...
    def build(self) -> DeleteOrgCustomOrgRequestBody: ...
