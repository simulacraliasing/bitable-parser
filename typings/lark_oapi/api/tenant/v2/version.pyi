from .resource import *

class V2:
    tenant: Tenant
    tenant_product_assign_info: TenantProductAssignInfo
    def __init__(self, config: Config) -> None: ...
