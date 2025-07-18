from .resource import *

class V1:
    access_record: AccessRecord
    access_record_access_photo: AccessRecordAccessPhoto
    device: Device
    rule_external: RuleExternal
    user: User
    user_face: UserFace
    visitor: Visitor
    def __init__(self, config: Config) -> None: ...
