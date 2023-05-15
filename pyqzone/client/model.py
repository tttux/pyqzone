from abc import ABC, abstractmethod
from ..api.model import AbstractAPIHost


class AbstractClient(ABC):

    api_host: AbstractAPIHost = None

    @abstractmethod
    def login(self, *args, **kwargs):
        pass

    @property
    def api(self):
        return self.api_host
    