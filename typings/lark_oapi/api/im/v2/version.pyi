from .resource import *

class V2:
    app_feed_card: AppFeedCard
    app_feed_card_batch: AppFeedCardBatch
    biz_entity_tag_relation: BizEntityTagRelation
    chat_button: ChatButton
    feed_card: FeedCard
    tag: Tag
    url_preview: UrlPreview
    def __init__(self, config: Config) -> None: ...
