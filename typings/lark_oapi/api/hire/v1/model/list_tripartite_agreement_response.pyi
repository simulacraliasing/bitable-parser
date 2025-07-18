from .list_tripartite_agreement_response_body import ListTripartiteAgreementResponseBody as ListTripartiteAgreementResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTripartiteAgreementResponse(BaseResponse):
    data: ListTripartiteAgreementResponseBody | None
    def __init__(self, d=None) -> None: ...
