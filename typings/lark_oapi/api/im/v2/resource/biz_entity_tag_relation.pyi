from ..model.create_biz_entity_tag_relation_request import CreateBizEntityTagRelationRequest as CreateBizEntityTagRelationRequest
from ..model.create_biz_entity_tag_relation_response import CreateBizEntityTagRelationResponse as CreateBizEntityTagRelationResponse
from ..model.get_biz_entity_tag_relation_request import GetBizEntityTagRelationRequest as GetBizEntityTagRelationRequest
from ..model.get_biz_entity_tag_relation_response import GetBizEntityTagRelationResponse as GetBizEntityTagRelationResponse
from ..model.update_biz_entity_tag_relation_request import UpdateBizEntityTagRelationRequest as UpdateBizEntityTagRelationRequest
from ..model.update_biz_entity_tag_relation_response import UpdateBizEntityTagRelationResponse as UpdateBizEntityTagRelationResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class BizEntityTagRelation:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateBizEntityTagRelationRequest, option: RequestOption | None = None) -> CreateBizEntityTagRelationResponse: ...
    async def acreate(self, request: CreateBizEntityTagRelationRequest, option: RequestOption | None = None) -> CreateBizEntityTagRelationResponse: ...
    def get(self, request: GetBizEntityTagRelationRequest, option: RequestOption | None = None) -> GetBizEntityTagRelationResponse: ...
    async def aget(self, request: GetBizEntityTagRelationRequest, option: RequestOption | None = None) -> GetBizEntityTagRelationResponse: ...
    def update(self, request: UpdateBizEntityTagRelationRequest, option: RequestOption | None = None) -> UpdateBizEntityTagRelationResponse: ...
    async def aupdate(self, request: UpdateBizEntityTagRelationRequest, option: RequestOption | None = None) -> UpdateBizEntityTagRelationResponse: ...
