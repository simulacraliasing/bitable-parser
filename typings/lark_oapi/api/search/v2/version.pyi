from .resource import *

class V2:
    app: App
    data_source: DataSource
    data_source_item: DataSourceItem
    message: Message
    schema: Schema
    def __init__(self, config: Config) -> None: ...
