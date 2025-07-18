from .filter_schema import FilterSchema as FilterSchema
from .model_config import ModelConfig as ModelConfig
from lark_oapi.core.construct import init as init

class Dataset:
    dataset_id: str | None
    app_id: str | None
    create_time: str | None
    update_time: str | None
    chunk_num: int | None
    doc_num: int | None
    name: str | None
    description: str | None
    filter_schemas: list[FilterSchema] | None
    model_config: ModelConfig | None
    viewer_app_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> DatasetBuilder: ...

class DatasetBuilder:
    def __init__(self) -> None: ...
    def dataset_id(self, dataset_id: str) -> DatasetBuilder: ...
    def app_id(self, app_id: str) -> DatasetBuilder: ...
    def create_time(self, create_time: str) -> DatasetBuilder: ...
    def update_time(self, update_time: str) -> DatasetBuilder: ...
    def chunk_num(self, chunk_num: int) -> DatasetBuilder: ...
    def doc_num(self, doc_num: int) -> DatasetBuilder: ...
    def name(self, name: str) -> DatasetBuilder: ...
    def description(self, description: str) -> DatasetBuilder: ...
    def filter_schemas(self, filter_schemas: list[FilterSchema]) -> DatasetBuilder: ...
    def model_config(self, model_config: ModelConfig) -> DatasetBuilder: ...
    def viewer_app_ids(self, viewer_app_ids: list[str]) -> DatasetBuilder: ...
    def build(self) -> Dataset: ...
