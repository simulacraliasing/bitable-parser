from lark_oapi.ws.const import *
from lark_oapi.ws.exception import *
from lark_oapi.ws.model import *
from _typeshed import Incomplete
from lark_oapi.core.cache import ExpiringCache as ExpiringCache
from lark_oapi.core.const import FEISHU_DOMAIN as FEISHU_DOMAIN, UTF_8 as UTF_8
from lark_oapi.core.enum import LogLevel as LogLevel
from lark_oapi.core.json import JSON as JSON
from lark_oapi.core.log import logger as logger
from lark_oapi.core.utils import Strings as Strings
from lark_oapi.event.dispatcher_handler import EventDispatcherHandler as EventDispatcherHandler
from lark_oapi.ws.enum import FrameType as FrameType, MessageType as MessageType
from lark_oapi.ws.pb.google.protobuf.internal.containers import RepeatedCompositeFieldContainer as RepeatedCompositeFieldContainer
from lark_oapi.ws.pb.pbbp2_pb2 import Frame as Frame

loop: Incomplete

class Client:
    def __init__(self, app_id: str, app_secret, log_level: LogLevel = ..., event_handler: EventDispatcherHandler = None, domain: str = ..., auto_reconnect: bool = True) -> None: ...
    def start(self) -> None: ...
