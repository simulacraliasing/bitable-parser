from _typeshed import Incomplete
from lark_oapi.ws.pb.google.protobuf import message as message
from lark_oapi.ws.pb.google.protobuf.internal import containers as containers, encoder as encoder, wire_format as wire_format

def ReadTag(buffer, pos): ...
def EnumDecoder(field_number, is_repeated, is_packed, key, new_default, clear_if_default: bool = False): ...

Int32Decoder: Incomplete
Int64Decoder: Incomplete
UInt32Decoder: Incomplete
UInt64Decoder: Incomplete
SInt32Decoder: Incomplete
SInt64Decoder: Incomplete
Fixed32Decoder: Incomplete
Fixed64Decoder: Incomplete
SFixed32Decoder: Incomplete
SFixed64Decoder: Incomplete
FloatDecoder: Incomplete
DoubleDecoder: Incomplete
BoolDecoder: Incomplete

def StringDecoder(field_number, is_repeated, is_packed, key, new_default, clear_if_default: bool = False): ...
def BytesDecoder(field_number, is_repeated, is_packed, key, new_default, clear_if_default: bool = False): ...
def GroupDecoder(field_number, is_repeated, is_packed, key, new_default): ...
def MessageDecoder(field_number, is_repeated, is_packed, key, new_default): ...

MESSAGE_SET_ITEM_TAG: Incomplete

def MessageSetItemDecoder(descriptor): ...
def MapDecoder(field_descriptor, new_default, is_message_map): ...

SkipField: Incomplete
