from .resource import *

class V1:
    comment: Comment
    post: Post
    post_statistics: PostStatistics
    reaction: Reaction
    def __init__(self, config: Config) -> None: ...
