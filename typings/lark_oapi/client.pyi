from .core.model import *
from .api.acs.service import AcsService as AcsService
from .api.admin.service import AdminService as AdminService
from .api.aily.service import AilyService as AilyService
from .api.apaas.service import ApaasService as ApaasService
from .api.application.service import ApplicationService as ApplicationService
from .api.approval.service import ApprovalService as ApprovalService
from .api.attendance.service import AttendanceService as AttendanceService
from .api.auth.service import AuthService as AuthService
from .api.authen.service import AuthenService as AuthenService
from .api.baike.service import BaikeService as BaikeService
from .api.base.service import BaseService as BaseService
from .api.bitable.service import BitableService as BitableService
from .api.block.service import BlockService as BlockService
from .api.board.service import BoardService as BoardService
from .api.calendar.service import CalendarService as CalendarService
from .api.cardkit.service import CardkitService as CardkitService
from .api.compensation.service import CompensationService as CompensationService
from .api.contact.service import ContactService as ContactService
from .api.corehr.service import CorehrService as CorehrService
from .api.docs.service import DocsService as DocsService
from .api.document_ai.service import DocumentAiService as DocumentAiService
from .api.docx.service import DocxService as DocxService
from .api.drive.service import DriveService as DriveService
from .api.ehr.service import EhrService as EhrService
from .api.event.service import EventService as EventService
from .api.helpdesk.service import HelpdeskService as HelpdeskService
from .api.hire.service import HireService as HireService
from .api.human_authentication.service import HumanAuthenticationService as HumanAuthenticationService
from .api.im.service import ImService as ImService
from .api.lingo.service import LingoService as LingoService
from .api.mail.service import MailService as MailService
from .api.mdm.service import MdmService as MdmService
from .api.meeting_room.service import MeetingRoomService as MeetingRoomService
from .api.minutes.service import MinutesService as MinutesService
from .api.moments.service import MomentsService as MomentsService
from .api.okr.service import OkrService as OkrService
from .api.optical_char_recognition.service import OpticalCharRecognitionService as OpticalCharRecognitionService
from .api.passport.service import PassportService as PassportService
from .api.payroll.service import PayrollService as PayrollService
from .api.performance.service import PerformanceService as PerformanceService
from .api.personal_settings.service import PersonalSettingsService as PersonalSettingsService
from .api.report.service import ReportService as ReportService
from .api.search.service import SearchService as SearchService
from .api.security_and_compliance.service import SecurityAndComplianceService as SecurityAndComplianceService
from .api.sheets.service import SheetsService as SheetsService
from .api.speech_to_text.service import SpeechToTextService as SpeechToTextService
from .api.task.service import TaskService as TaskService
from .api.tenant.service import TenantService as TenantService
from .api.translation.service import TranslationService as TranslationService
from .api.vc.service import VcService as VcService
from .api.verification.service import VerificationService as VerificationService
from .api.wiki.service import WikiService as WikiService
from .api.workplace.service import WorkplaceService as WorkplaceService
from .core import JSON as JSON, logger as logger
from .core.const import APPLICATION_JSON as APPLICATION_JSON, UTF_8 as UTF_8
from .core.http import Transport as Transport
from .core.token import TokenManager as TokenManager, verify as verify
from .core.utils.files import Files as Files

class Client:
    helpdesk: HelpdeskService | None
    personal_settings: PersonalSettingsService | None
    auth: AuthService | None
    block: BlockService | None
    im: ImService | None
    meeting_room: MeetingRoomService | None
    sheets: SheetsService | None
    performance: PerformanceService | None
    compensation: CompensationService | None
    docs: DocsService | None
    moments: MomentsService | None
    okr: OkrService | None
    contact: ContactService | None
    mail: MailService | None
    human_authentication: HumanAuthenticationService | None
    minutes: MinutesService | None
    apaas: ApaasService | None
    attendance: AttendanceService | None
    payroll: PayrollService | None
    translation: TranslationService | None
    verification: VerificationService | None
    aily: AilyService | None
    baike: BaikeService | None
    docx: DocxService | None
    hire: HireService | None
    board: BoardService | None
    mdm: MdmService | None
    admin: AdminService | None
    application: ApplicationService | None
    document_ai: DocumentAiService | None
    task: TaskService | None
    vc: VcService | None
    ehr: EhrService | None
    wiki: WikiService | None
    cardkit: CardkitService | None
    event: EventService | None
    lingo: LingoService | None
    optical_char_recognition: OpticalCharRecognitionService | None
    passport: PassportService | None
    workplace: WorkplaceService | None
    authen: AuthenService | None
    base: BaseService | None
    corehr: CorehrService | None
    drive: DriveService | None
    security_and_compliance: SecurityAndComplianceService | None
    tenant: TenantService | None
    calendar: CalendarService | None
    report: ReportService | None
    search: SearchService | None
    speech_to_text: SpeechToTextService | None
    acs: AcsService | None
    approval: ApprovalService | None
    bitable: BitableService | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ClientBuilder: ...
    def request(self, request: BaseRequest, option: RequestOption | None = None) -> BaseResponse: ...
    async def arequest(self, request: BaseRequest, option: RequestOption | None = None) -> BaseResponse: ...

class ClientBuilder:
    def __init__(self) -> None: ...
    def app_id(self, app_id: str) -> ClientBuilder: ...
    def app_secret(self, app_secret: str) -> ClientBuilder: ...
    def domain(self, domain: str) -> ClientBuilder: ...
    def timeout(self, timeout: float) -> ClientBuilder: ...
    def app_type(self, app_type: AppType) -> ClientBuilder: ...
    def app_ticket(self, app_ticket: str) -> ClientBuilder: ...
    def enable_set_token(self, enable_set_token: bool) -> ClientBuilder: ...
    def cache(self, cache: ICache) -> ClientBuilder: ...
    def log_level(self, log_level: LogLevel) -> ClientBuilder: ...
    def build(self) -> Client: ...
