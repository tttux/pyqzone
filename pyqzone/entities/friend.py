
class User(object):
    """用户实体类"""

    uin: int
    """QQ号"""

    name: str
    """QQ昵称"""

    nick: str
    """备注的昵称"""

    is_friend: bool
    """是否为好友"""