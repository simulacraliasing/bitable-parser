from .list_app_data_asset_tag_response_body import ListAppDataAssetTagResponseBody as ListAppDataAssetTagResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppDataAssetTagResponse(BaseResponse):
    data: ListAppDataAssetTagResponseBody | None
    def __init__(self, d=None) -> None: ...
