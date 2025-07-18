from .get_biz_entity_tag_relation_response_body import GetBizEntityTagRelationResponseBody as GetBizEntityTagRelationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetBizEntityTagRelationResponse(BaseResponse):
    data: GetBizEntityTagRelationResponseBody | None
    def __init__(self, d=None) -> None: ...
