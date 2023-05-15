from ..model import AbstractProfileAPIGroup
from .host import WebAPI


class WebProfileAPI(WebAPI, AbstractProfileAPIGroup):

    def get_visitor_count(self) -> tuple[int, int]:
        pass
