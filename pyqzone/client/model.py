from abc import ABC, abstractmethod
from ..api.model import AbstractAPIHost


class AbstractClient(ABC):

    __api__: AbstractAPIHost = None

    @abstractmethod
    def login(self, *args, **kwargs):
        pass

    @property
    def api(self):
        return self.__api__
    