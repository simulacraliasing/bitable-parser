from .resource import *

class V1:
    classification: Classification
    draft: Draft
    entity: Entity
    file: File
    repo: Repo
    def __init__(self, config: Config) -> None: ...
