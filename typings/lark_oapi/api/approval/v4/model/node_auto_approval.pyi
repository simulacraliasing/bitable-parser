from lark_oapi.core.construct import init as init

class NodeAutoApproval:
    node_id_type: str | None
    node_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> NodeAutoApprovalBuilder: ...

class NodeAutoApprovalBuilder:
    def __init__(self) -> None: ...
    def node_id_type(self, node_id_type: str) -> NodeAutoApprovalBuilder: ...
    def node_id(self, node_id: str) -> NodeAutoApprovalBuilder: ...
    def build(self) -> NodeAutoApproval: ...
