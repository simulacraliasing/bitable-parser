from .resource import *

class V1:
    custom_workplace_access_data: CustomWorkplaceAccessData
    workplace_access_data: WorkplaceAccessData
    workplace_block_access_data: WorkplaceBlockAccessData
    def __init__(self, config: Config) -> None: ...
