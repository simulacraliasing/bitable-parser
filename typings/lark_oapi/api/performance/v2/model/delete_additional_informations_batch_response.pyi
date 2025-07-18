from .delete_additional_informations_batch_response_body import DeleteAdditionalInformationsBatchResponseBody as DeleteAdditionalInformationsBatchResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteAdditionalInformationsBatchResponse(BaseResponse):
    data: DeleteAdditionalInformationsBatchResponseBody | None
    def __init__(self, d=None) -> None: ...
