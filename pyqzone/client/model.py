from abc import ABC, abstractmethod
from ..api.model import *


class AbstractClient(ABC):

    emotion: AbstractEmotionAPIGroup
    """说说API"""

    blog: AbstractBlogAPIGroup
    """日志API"""

    album: AbstractAlbumAPIGroup
    """相册API"""

    board: AbstractBoardAPIGroup
    """留言板API"""

    profile: AbstractProfileAPIGroup
    """个人信息API"""

    friend: AbstractFriendAPIGroup
    """好友信息API"""

    uin: int = 0 
    """登录的QQ号"""

    @abstractmethod
    def login(self, *args, **kwargs):
        pass

    