from ..model import AbstractClient
from ...api import web as web_api

import requests


class WebClient(AbstractClient):

    cookies: str
    """Cookies字符串"""

    cookies_dict: dict[str, str]
    """Cookie dict"""

    headers: dict[str, str]
    """请求头"""

    def __init__(
        self,
        cookies: str = ""
    ):
        self.cookies = cookies

        # 把cookies转换成cookie_dict
        self.cookies_dict = {}
        if self.cookies:
            for cookie in self.cookies.split(";"):
                key, value = cookie.split("=")
                self.cookies_dict[key] = value

        self.uin = int(self.cookies_dict['uin'][1:])

        self.emotion = web_api.WebEmotionAPI(self)
        self.blog = web_api.WebBlogAPI(self)
        self.album = web_api.WebAlbumAPI(self)
        self.board = web_api.WebBoardAPI(self)
        self.profile = web_api.WebProfileAPI(self)
        self.friend = web_api.WebFriendAPI(self)

    def request_wrapper(
        self,
        method: str,
        url: str,
        extra_headers: dict[str, str] = None,
        extra_cookies: dict[str, str] = None,
        post_data: dict[str, str] = None,
        timeout: int = 10,
    ):
        """带上客户端的Cookies和Headers发起请求"""
        final_headers = self.headers + (extra_headers if extra_headers else [])
        final_cookies = self.cookies + (extra_cookies if extra_cookies else [])

        if method == "GET":
            return requests.get(
                url,
                headers=final_headers,
                cookies=final_cookies,
                timeout=timeout
            )
        if method == "POST":
            return requests.post(
                url,
                headers=final_headers,
                cookies=final_cookies,
                data=post_data,
                timeout=timeout
            )

        raise NotImplementedError

    def get(
        self,
        url: str,
        extra_headers: dict[str, str] = None,
        extra_cookies: dict[str, str] = None,
        timeout: int = 10,
    ):
        return self.request_wrapper(
            method="GET",
            url=url,
            extra_headers=extra_headers,
            extra_cookies=extra_cookies,
            timeout=timeout
        )

    def post(
        self,
        url: str,
        extra_headers: dict[str, str] = None,
        extra_cookies: dict[str, str] = None,
        post_data: dict[str, str] = None,
        timeout: int = 10,
    ):
        return self.request_wrapper(
            method="POST",
            url=url,
            extra_headers=extra_headers,
            extra_cookies=extra_cookies,
            post_data=post_data,
            timeout=timeout
        )

    @property
    def gtk(self) -> str:
        """生成gtk"""
        skey = self.cookies_dict['p_skey']
        hash_val = 5381
        
        for i in range(len(skey)):
            hash_val += (hash_val << 5) + ord(skey[i])

        return str(hash_val & 2147483647)
    