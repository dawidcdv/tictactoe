from abc import ABCMeta, abstractmethod

class InputAdapter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def convertToGamePosition(self, position : str) -> int:
        raise NotImplemented