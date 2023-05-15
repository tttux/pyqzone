from ..model import AbstractBlogAPIGroup
from .host import WebAPI


class WebBlogAPI(WebAPI, AbstractBlogAPIGroup):
    pass