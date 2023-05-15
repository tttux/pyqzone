"""说说相关实体类"""
from .misc import *


class Emotion(Feed):
    """说说类"""

    tid: str = None
    """说说tid"""

    text: str = None
    """说说文字内容"""

