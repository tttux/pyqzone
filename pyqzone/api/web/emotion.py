from pyqzone.entities import emotion
from ..model import AbstractEmotionAPIGroup
from .host import WebAPI


class WebEmotionAPI(WebAPI, AbstractEmotionAPIGroup):
    """PCWeb端的说说API组"""
  
    def fetch_feeds(self, page: int, **kwargs) -> list[emotion.Feed]:
        pass
