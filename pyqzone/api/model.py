from abc import ABC, abstractmethod


class AbstractAPIHost(ABC):
    
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass
    