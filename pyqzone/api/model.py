"""定义各个服务分类的API组接口

实现时先由一个类FooAPI继承`AbstractAPIGroup`类，重写`client`属性，
重新指定其类型为此实现对应的客户端实现类，以便于代码补全和类型提示。
之后每个分类的API实现均继承于FooAPI以及相应的分组API接口
"""

from abc import ABC, abstractmethod
from ..entities import emotion
from ..client import model as clientModel


class AbstractAPIGroup(ABC):
    """分类API基类抽象类"""

    client: clientModel.AbstractClient

    def __init__(self, client: clientModel.AbstractClient):
        self.client = client


class AbstractEmotionAPIGroup(AbstractAPIGroup):
    """说说相关API组"""
    
    @abstractmethod
    def fetch_feeds(
        self,
        page: int,
        **kwargs
    ) -> list[emotion.Feed]:
        """获取最新动态列表
        
        Parameters:
        ----------
        page: int (optional)  页码

        Returns:
        -------
        list[emotion.Feed] 最新动态列表
        """


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
    
    @abstractmethod
    def get_visitor_count(self) -> tuple[int, int]:
        """获取访客人数
        
        Returns:
        -------
        tuple[int, int]: 今日访客量, 访客总量
        """


class AbstractFriendAPIGroup(AbstractAPIGroup):
    """好友信息相关API组"""
    pass


__all__ = [
    'AbstractAPIGroup',
    'AbstractEmotionAPIGroup',
    'AbstractBlogAPIGroup',
    'AbstractAlbumAPIGroup',
    'AbstractBoardAPIGroup',
    'AbstractProfileAPIGroup',
    'AbstractFriendAPIGroup',
]
