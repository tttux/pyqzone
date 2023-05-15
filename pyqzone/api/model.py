from abc import ABC, abstractmethod
from ..entities import emotion
from ..client.model import AbstractClient


class AbstractAPIGroup(ABC):
    """分类API基类"""

    api_host: 'AbstractAPIHost' = None
    """API宿主"""

    def __init__(self, api_host: 'AbstractAPIHost'):
        self.api_host = api_host

    @property
    def host(self):
        return self.api_host


class AbstractEmotionAPIGroup(AbstractAPIGroup):
    """说说相关API组"""
    
    @abstractmethod
    def fetch_feeds(
        self,
        page: int,
        **kwargs
    ) -> list[emotion.Feed]:
        pass


class AbstractBlogAPIGroup(AbstractAPIGroup):
    """日志相关API组"""
    pass


class AbstractAlbumAPIGroup(AbstractAPIGroup):
    """相册相关API组"""
    pass


class AbstractBoardAPIGroup(AbstractAPIGroup):
    """留言板相关API组"""
    pass


class AbstractProfileAPIGroup(AbstractAPIGroup):
    """个人信息相关API组"""
    pass


class AbstractFriendAPIGroup(AbstractAPIGroup):
    """好友信息相关API组"""
    pass

class AbstractAPIHost(ABC):
    """API宿主类"""

    client: AbstractClient

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
    