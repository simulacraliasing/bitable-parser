from lark_oapi.core.construct import init as init

class ConnectorInstanceDefinition:
    connector_source_type: str | None
    connector_api_name: str | None
    action_api_name: str | None
    connection_api_name: str | None
    input_data: str | None
    output_data_schema: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ConnectorInstanceDefinitionBuilder: ...

class ConnectorInstanceDefinitionBuilder:
    def __init__(self) -> None: ...
    def connector_source_type(self, connector_source_type: str) -> ConnectorInstanceDefinitionBuilder: ...
    def connector_api_name(self, connector_api_name: str) -> ConnectorInstanceDefinitionBuilder: ...
    def action_api_name(self, action_api_name: str) -> ConnectorInstanceDefinitionBuilder: ...
    def connection_api_name(self, connection_api_name: str) -> ConnectorInstanceDefinitionBuilder: ...
    def input_data(self, input_data: str) -> ConnectorInstanceDefinitionBuilder: ...
    def output_data_schema(self, output_data_schema: str) -> ConnectorInstanceDefinitionBuilder: ...
    def build(self) -> ConnectorInstanceDefinition: ...
