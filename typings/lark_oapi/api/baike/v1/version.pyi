from .resource import *

class V1:
    classification: Classification
    draft: Draft
    entity: Entity
    file: File
    def __init__(self, config: Config) -> None: ...
