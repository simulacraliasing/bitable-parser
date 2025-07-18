from ..model.create_tripartite_agreement_request import CreateTripartiteAgreementRequest as CreateTripartiteAgreementRequest
from ..model.create_tripartite_agreement_response import CreateTripartiteAgreementResponse as CreateTripartiteAgreementResponse
from ..model.delete_tripartite_agreement_request import DeleteTripartiteAgreementRequest as DeleteTripartiteAgreementRequest
from ..model.delete_tripartite_agreement_response import DeleteTripartiteAgreementResponse as DeleteTripartiteAgreementResponse
from ..model.list_tripartite_agreement_request import ListTripartiteAgreementRequest as ListTripartiteAgreementRequest
from ..model.list_tripartite_agreement_response import ListTripartiteAgreementResponse as ListTripartiteAgreementResponse
from ..model.update_tripartite_agreement_request import UpdateTripartiteAgreementRequest as UpdateTripartiteAgreementRequest
from ..model.update_tripartite_agreement_response import UpdateTripartiteAgreementResponse as UpdateTripartiteAgreementResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class TripartiteAgreement:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateTripartiteAgreementRequest, option: RequestOption | None = None) -> CreateTripartiteAgreementResponse: ...
    async def acreate(self, request: CreateTripartiteAgreementRequest, option: RequestOption | None = None) -> CreateTripartiteAgreementResponse: ...
    def delete(self, request: DeleteTripartiteAgreementRequest, option: RequestOption | None = None) -> DeleteTripartiteAgreementResponse: ...
    async def adelete(self, request: DeleteTripartiteAgreementRequest, option: RequestOption | None = None) -> DeleteTripartiteAgreementResponse: ...
    def list(self, request: ListTripartiteAgreementRequest, option: RequestOption | None = None) -> ListTripartiteAgreementResponse: ...
    async def alist(self, request: ListTripartiteAgreementRequest, option: RequestOption | None = None) -> ListTripartiteAgreementResponse: ...
    def update(self, request: UpdateTripartiteAgreementRequest, option: RequestOption | None = None) -> UpdateTripartiteAgreementResponse: ...
    async def aupdate(self, request: UpdateTripartiteAgreementRequest, option: RequestOption | None = None) -> UpdateTripartiteAgreementResponse: ...
