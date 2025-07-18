from ..model.get_application_collaborators_request import GetApplicationCollaboratorsRequest as GetApplicationCollaboratorsRequest
from ..model.get_application_collaborators_response import GetApplicationCollaboratorsResponse as GetApplicationCollaboratorsResponse
from ..model.update_application_collaborators_request import UpdateApplicationCollaboratorsRequest as UpdateApplicationCollaboratorsRequest
from ..model.update_application_collaborators_response import UpdateApplicationCollaboratorsResponse as UpdateApplicationCollaboratorsResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationCollaborators:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetApplicationCollaboratorsRequest, option: RequestOption | None = None) -> GetApplicationCollaboratorsResponse: ...
    async def aget(self, request: GetApplicationCollaboratorsRequest, option: RequestOption | None = None) -> GetApplicationCollaboratorsResponse: ...
    def update(self, request: UpdateApplicationCollaboratorsRequest, option: RequestOption | None = None) -> UpdateApplicationCollaboratorsResponse: ...
    async def aupdate(self, request: UpdateApplicationCollaboratorsRequest, option: RequestOption | None = None) -> UpdateApplicationCollaboratorsResponse: ...
