from abc import ABCMeta, abstractmethod

from src.tictactoe.game.Tictactoe import Tictactoe


class Application:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, game=Tictactoe): raise NotImplementedError