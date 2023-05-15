"""杂项实体类"""
from .friend import *


class Comment(object):
    """评论实体类"""
    pass


class Traffic(object):
    """流量实体类"""

    like_count: int = None
    """点赞数"""

    likers: list[User] = None
    """点赞人列表"""

    view_count: int = None
    """浏览数"""

    forward_count: int = None
    """转发数"""

    forwarders: list[User] = None
    """转发人列表"""

    comment_count: int = None
    """评论数"""

    comments: list[Comment] = None
    """评论列表"""


class Feed(object):
    """动态基类"""

    timestamp: int = None
    """动态时间戳"""

    user: User = None
    """动态发表人"""

    traffic: Traffic = None
    """动态流量"""
