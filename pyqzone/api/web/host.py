from ..model import *
from .emotion import *
from .blog import *
from .album import *
from .board import *
from .profile import *
from .friend import *

from ...client.web.host import WebClient

class WebAPIHost(AbstractAPIHost):
    
    def __init__(self, client: WebClient):
        self.emotion = WebEmotionAPI(self)
        self.blog = WebBlogAPI(self)
        self.album = WebAlbumAPI(self)
        self.board = WebBoardAPI(self)
        self.profile = WebProfileAPI(self)
        self.friend = WebFriendAPI(self)