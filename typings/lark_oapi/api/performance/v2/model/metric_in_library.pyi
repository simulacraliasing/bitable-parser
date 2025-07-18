from .formula import Formula as Formula
from .metric_field_in_library import MetricFieldInLibrary as MetricFieldInLibrary
from .metric_tag import MetricTag as MetricTag
from .user import User as User
from lark_oapi.core.construct import init as init

class MetricInLibrary:
    metric_id: int | None
    name: str | None
    type_id: int | None
    tags: list[MetricTag] | None
    fields: list[MetricFieldInLibrary] | None
    scoring_setting_type: str | None
    scoring_formula: Formula | None
    data_source_inputters: list[User] | None
    range_of_availability: str | None
    is_active: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MetricInLibraryBuilder: ...

class MetricInLibraryBuilder:
    def __init__(self) -> None: ...
    def metric_id(self, metric_id: int) -> MetricInLibraryBuilder: ...
    def name(self, name: str) -> MetricInLibraryBuilder: ...
    def type_id(self, type_id: int) -> MetricInLibraryBuilder: ...
    def tags(self, tags: list[MetricTag]) -> MetricInLibraryBuilder: ...
    def fields(self, fields: list[MetricFieldInLibrary]) -> MetricInLibraryBuilder: ...
    def scoring_setting_type(self, scoring_setting_type: str) -> MetricInLibraryBuilder: ...
    def scoring_formula(self, scoring_formula: Formula) -> MetricInLibraryBuilder: ...
    def data_source_inputters(self, data_source_inputters: list[User]) -> MetricInLibraryBuilder: ...
    def range_of_availability(self, range_of_availability: str) -> MetricInLibraryBuilder: ...
    def is_active(self, is_active: bool) -> MetricInLibraryBuilder: ...
    def build(self) -> MetricInLibrary: ...
