from ..model import AbstractAPIGroup
from ...client.web.client import WebClient


class WebAPI(AbstractAPIGroup):

    client: WebClient
    
