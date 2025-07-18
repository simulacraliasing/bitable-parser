from .segment_style import SegmentStyle as SegmentStyle
from lark_oapi.core.construct import init as init

class File:
    file_token: str | None
    name: str | None
    segment_style: SegmentStyle | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> FileBuilder: ...

class FileBuilder:
    def __init__(self) -> None: ...
    def file_token(self, file_token: str) -> FileBuilder: ...
    def name(self, name: str) -> FileBuilder: ...
    def segment_style(self, segment_style: SegmentStyle) -> FileBuilder: ...
    def build(self) -> File: ...
