from ..model import AbstractClient
from ...api import web as web_api


class WebClient(AbstractClient):

    cookies: str
    """Cookies字符串"""

    cookies_dict: dict[str, str]
    """Cookie dict"""
    
    def __init__(
        self,
        cookies: str=""
    ):

        self.cookies = cookies

        # 把cookies转换成cookie_dict
        self.cookies_dict = {}
        if self.cookies:
            for cookie in self.cookies.split(";"):
                key, value = cookie.split("=")
                self.cookies_dict[key] = value

        self.emotion = web_api.WebEmotionAPI(self)
        self.blog = web_api.WebBlogAPI(self)
        self.album = web_api.WebAlbumAPI(self)
        self.board = web_api.WebBoardAPI(self)
        self.profile = web_api.WebProfileAPI(self)
        self.friend = web_api.WebFriendAPI(self)
