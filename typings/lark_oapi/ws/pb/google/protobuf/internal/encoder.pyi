from _typeshed import Incomplete
from lark_oapi.ws.pb.google.protobuf.internal import wire_format as wire_format

Int32Sizer: Incomplete
Int64Sizer: Incomplete
EnumSizer: Incomplete
UInt32Sizer: Incomplete
UInt64Sizer: Incomplete
SInt32Sizer: Incomplete
SInt64Sizer: Incomplete
Fixed32Sizer: Incomplete
SFixed32Sizer: Incomplete
FloatSizer: Incomplete
Fixed64Sizer: Incomplete
SFixed64Sizer: Incomplete
DoubleSizer: Incomplete
BoolSizer: Incomplete

def StringSizer(field_number, is_repeated, is_packed): ...
def BytesSizer(field_number, is_repeated, is_packed): ...
def GroupSizer(field_number, is_repeated, is_packed): ...
def MessageSizer(field_number, is_repeated, is_packed): ...
def MessageSetItemSizer(field_number): ...
def MapSizer(field_descriptor, is_message_map): ...
def TagBytes(field_number, wire_type): ...

Int32Encoder: Incomplete

Int64Encoder: Incomplete

EnumEncoder: Incomplete
UInt32Encoder: Incomplete
UInt64Encoder: Incomplete
SInt32Encoder: Incomplete
SInt64Encoder: Incomplete
Fixed32Encoder: Incomplete
Fixed64Encoder: Incomplete
SFixed32Encoder: Incomplete
SFixed64Encoder: Incomplete
FloatEncoder: Incomplete
DoubleEncoder: Incomplete

def BoolEncoder(field_number, is_repeated, is_packed): ...
def StringEncoder(field_number, is_repeated, is_packed): ...
def BytesEncoder(field_number, is_repeated, is_packed): ...
def GroupEncoder(field_number, is_repeated, is_packed): ...
def MessageEncoder(field_number, is_repeated, is_packed): ...
def MessageSetItemEncoder(field_number): ...
def MapEncoder(field_descriptor): ...
