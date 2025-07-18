import types
from _typeshed import Incomplete
from lark_oapi.ws.pb.google.protobuf.internal import api_implementation as api_implementation

class Error(Exception): ...
class TypeTransformationError(Error): ...

class DescriptorMetaclass(type):
    def __instancecheck__(cls, obj): ...
DescriptorMetaclass = type

class _Lock:
    def __new__(cls): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class DescriptorBase(metaclass=DescriptorMetaclass):
    has_options: Incomplete
    def __init__(self, options, serialized_options, options_class_name) -> None: ...
    def GetOptions(self): ...

class _NestedDescriptorBase(DescriptorBase):
    name: Incomplete
    full_name: Incomplete
    file: Incomplete
    containing_type: Incomplete
    def __init__(self, options, options_class_name, name, full_name, file, containing_type, serialized_start=None, serialized_end=None, serialized_options=None) -> None: ...
    def CopyToProto(self, proto) -> None: ...

class Descriptor(_NestedDescriptorBase):
    def __new__(cls, name=None, full_name=None, filename=None, containing_type=None, fields=None, nested_types=None, enum_types=None, extensions=None, options=None, serialized_options=None, is_extendable: bool = True, extension_ranges=None, oneofs=None, file=None, serialized_start=None, serialized_end=None, syntax=None, create_key=None): ...
    fields: Incomplete
    fields_by_number: Incomplete
    fields_by_name: Incomplete
    nested_types: Incomplete
    nested_types_by_name: Incomplete
    enum_types: Incomplete
    enum_types_by_name: Incomplete
    enum_values_by_name: Incomplete
    extensions: Incomplete
    extensions_by_name: Incomplete
    is_extendable: Incomplete
    extension_ranges: Incomplete
    oneofs: Incomplete
    oneofs_by_name: Incomplete
    syntax: Incomplete
    def __init__(self, name, full_name, filename, containing_type, fields, nested_types, enum_types, extensions, options=None, serialized_options=None, is_extendable: bool = True, extension_ranges=None, oneofs=None, file=None, serialized_start=None, serialized_end=None, syntax=None, create_key=None) -> None: ...
    @property
    def fields_by_camelcase_name(self): ...
    def EnumValueName(self, enum, value): ...
    def CopyToProto(self, proto) -> None: ...

class FieldDescriptor(DescriptorBase):
    TYPE_DOUBLE: int
    TYPE_FLOAT: int
    TYPE_INT64: int
    TYPE_UINT64: int
    TYPE_INT32: int
    TYPE_FIXED64: int
    TYPE_FIXED32: int
    TYPE_BOOL: int
    TYPE_STRING: int
    TYPE_GROUP: int
    TYPE_MESSAGE: int
    TYPE_BYTES: int
    TYPE_UINT32: int
    TYPE_ENUM: int
    TYPE_SFIXED32: int
    TYPE_SFIXED64: int
    TYPE_SINT32: int
    TYPE_SINT64: int
    MAX_TYPE: int
    CPPTYPE_INT32: int
    CPPTYPE_INT64: int
    CPPTYPE_UINT32: int
    CPPTYPE_UINT64: int
    CPPTYPE_DOUBLE: int
    CPPTYPE_FLOAT: int
    CPPTYPE_BOOL: int
    CPPTYPE_ENUM: int
    CPPTYPE_STRING: int
    CPPTYPE_MESSAGE: int
    MAX_CPPTYPE: int
    LABEL_OPTIONAL: int
    LABEL_REQUIRED: int
    LABEL_REPEATED: int
    MAX_LABEL: int
    MAX_FIELD_NUMBER: Incomplete
    FIRST_RESERVED_FIELD_NUMBER: int
    LAST_RESERVED_FIELD_NUMBER: int
    def __new__(cls, name, full_name, index, number, type, cpp_type, label, default_value, message_type, enum_type, containing_type, is_extension, extension_scope, options=None, serialized_options=None, has_default_value: bool = True, containing_oneof=None, json_name=None, file=None, create_key=None): ...
    name: Incomplete
    full_name: Incomplete
    file: Incomplete
    json_name: Incomplete
    index: Incomplete
    number: Incomplete
    type: Incomplete
    cpp_type: Incomplete
    label: Incomplete
    has_default_value: Incomplete
    default_value: Incomplete
    containing_type: Incomplete
    message_type: Incomplete
    enum_type: Incomplete
    is_extension: Incomplete
    extension_scope: Incomplete
    containing_oneof: Incomplete
    def __init__(self, name, full_name, index, number, type, cpp_type, label, default_value, message_type, enum_type, containing_type, is_extension, extension_scope, options=None, serialized_options=None, has_default_value: bool = True, containing_oneof=None, json_name=None, file=None, create_key=None) -> None: ...
    @property
    def camelcase_name(self): ...
    @property
    def has_presence(self): ...
    @staticmethod
    def ProtoTypeToCppProtoType(proto_type): ...

class EnumDescriptor(_NestedDescriptorBase):
    def __new__(cls, name, full_name, filename, values, containing_type=None, options=None, serialized_options=None, file=None, serialized_start=None, serialized_end=None, create_key=None): ...
    values: Incomplete
    values_by_name: Incomplete
    values_by_number: Incomplete
    def __init__(self, name, full_name, filename, values, containing_type=None, options=None, serialized_options=None, file=None, serialized_start=None, serialized_end=None, create_key=None) -> None: ...
    def CopyToProto(self, proto) -> None: ...

class EnumValueDescriptor(DescriptorBase):
    def __new__(cls, name, index, number, type=None, options=None, serialized_options=None, create_key=None) -> None: ...
    name: Incomplete
    index: Incomplete
    number: Incomplete
    type: Incomplete
    def __init__(self, name, index, number, type=None, options=None, serialized_options=None, create_key=None) -> None: ...

class OneofDescriptor(DescriptorBase):
    def __new__(cls, name, full_name, index, containing_type, fields, options=None, serialized_options=None, create_key=None): ...
    name: Incomplete
    full_name: Incomplete
    index: Incomplete
    containing_type: Incomplete
    fields: Incomplete
    def __init__(self, name, full_name, index, containing_type, fields, options=None, serialized_options=None, create_key=None) -> None: ...

class ServiceDescriptor(_NestedDescriptorBase):
    def __new__(cls, name=None, full_name=None, index=None, methods=None, options=None, serialized_options=None, file=None, serialized_start=None, serialized_end=None, create_key=None): ...
    index: Incomplete
    methods: Incomplete
    methods_by_name: Incomplete
    def __init__(self, name, full_name, index, methods, options=None, serialized_options=None, file=None, serialized_start=None, serialized_end=None, create_key=None) -> None: ...
    def FindMethodByName(self, name): ...
    def CopyToProto(self, proto) -> None: ...

class MethodDescriptor(DescriptorBase):
    def __new__(cls, name, full_name, index, containing_service, input_type, output_type, client_streaming: bool = False, server_streaming: bool = False, options=None, serialized_options=None, create_key=None): ...
    name: Incomplete
    full_name: Incomplete
    index: Incomplete
    containing_service: Incomplete
    input_type: Incomplete
    output_type: Incomplete
    client_streaming: Incomplete
    server_streaming: Incomplete
    def __init__(self, name, full_name, index, containing_service, input_type, output_type, client_streaming: bool = False, server_streaming: bool = False, options=None, serialized_options=None, create_key=None) -> None: ...
    def CopyToProto(self, proto) -> None: ...

class FileDescriptor(DescriptorBase):
    def __new__(cls, name, package, options=None, serialized_options=None, serialized_pb=None, dependencies=None, public_dependencies=None, syntax=None, pool=None, create_key=None): ...
    pool: Incomplete
    message_types_by_name: Incomplete
    name: Incomplete
    package: Incomplete
    syntax: Incomplete
    serialized_pb: Incomplete
    enum_types_by_name: Incomplete
    extensions_by_name: Incomplete
    services_by_name: Incomplete
    dependencies: Incomplete
    public_dependencies: Incomplete
    def __init__(self, name, package, options=None, serialized_options=None, serialized_pb=None, dependencies=None, public_dependencies=None, syntax=None, pool=None, create_key=None) -> None: ...
    def CopyToProto(self, proto) -> None: ...

def MakeDescriptor(desc_proto, package: str = '', build_file_if_cpp: bool = True, syntax=None): ...
