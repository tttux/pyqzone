from pyqzone.entities import emotion
from ..model import AbstractEmotionAPIGroup


class WebEmotionAPI(AbstractEmotionAPIGroup):
    """PCWeb端的说说API组"""
    
    def fetch_feeds(self, page: int, **kwargs) -> list[emotion.Feed]:
        pass