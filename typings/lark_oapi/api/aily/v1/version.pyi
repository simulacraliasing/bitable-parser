from .resource import *

class V1:
    aily_session: AilySession
    aily_session_aily_message: AilySessionAilyMessage
    aily_session_run: AilySessionRun
    app_data_asset: AppDataAsset
    app_data_asset_tag: AppDataAssetTag
    app_knowledge: AppKnowledge
    app_skill: AppSkill
    def __init__(self, config: Config) -> None: ...
