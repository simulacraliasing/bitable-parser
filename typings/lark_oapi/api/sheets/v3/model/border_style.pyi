from .bottom_border_style import BottomBorderStyle as BottomBorderStyle
from .left_border_style import LeftBorderStyle as LeftBorderStyle
from .right_border_style import RightBorderStyle as RightBorderStyle
from .top_border_style import TopBorderStyle as TopBorderStyle
from lark_oapi.core.construct import init as init

class BorderStyle:
    top: TopBorderStyle | None
    left: LeftBorderStyle | None
    right: RightBorderStyle | None
    bottom: BottomBorderStyle | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BorderStyleBuilder: ...

class BorderStyleBuilder:
    def __init__(self) -> None: ...
    def top(self, top: TopBorderStyle) -> BorderStyleBuilder: ...
    def left(self, left: LeftBorderStyle) -> BorderStyleBuilder: ...
    def right(self, right: RightBorderStyle) -> BorderStyleBuilder: ...
    def bottom(self, bottom: BottomBorderStyle) -> BorderStyleBuilder: ...
    def build(self) -> BorderStyle: ...
