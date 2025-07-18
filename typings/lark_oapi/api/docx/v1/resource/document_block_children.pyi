from ..model.batch_delete_document_block_children_request import BatchDeleteDocumentBlockChildrenRequest as BatchDeleteDocumentBlockChildrenRequest
from ..model.batch_delete_document_block_children_response import BatchDeleteDocumentBlockChildrenResponse as BatchDeleteDocumentBlockChildrenResponse
from ..model.create_document_block_children_request import CreateDocumentBlockChildrenRequest as CreateDocumentBlockChildrenRequest
from ..model.create_document_block_children_response import CreateDocumentBlockChildrenResponse as CreateDocumentBlockChildrenResponse
from ..model.get_document_block_children_request import GetDocumentBlockChildrenRequest as GetDocumentBlockChildrenRequest
from ..model.get_document_block_children_response import GetDocumentBlockChildrenResponse as GetDocumentBlockChildrenResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class DocumentBlockChildren:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_delete(self, request: BatchDeleteDocumentBlockChildrenRequest, option: RequestOption | None = None) -> BatchDeleteDocumentBlockChildrenResponse: ...
    async def abatch_delete(self, request: BatchDeleteDocumentBlockChildrenRequest, option: RequestOption | None = None) -> BatchDeleteDocumentBlockChildrenResponse: ...
    def create(self, request: CreateDocumentBlockChildrenRequest, option: RequestOption | None = None) -> CreateDocumentBlockChildrenResponse: ...
    async def acreate(self, request: CreateDocumentBlockChildrenRequest, option: RequestOption | None = None) -> CreateDocumentBlockChildrenResponse: ...
    def get(self, request: GetDocumentBlockChildrenRequest, option: RequestOption | None = None) -> GetDocumentBlockChildrenResponse: ...
    async def aget(self, request: GetDocumentBlockChildrenRequest, option: RequestOption | None = None) -> GetDocumentBlockChildrenResponse: ...
