from enum import IntEnum
from src.tictactoe.game.BoardException import BoardException


class Board:

    class Mark(IntEnum):
        EMPTY = 0
        NOUGHT = 1
        CROSS = 2

    def __init__(self):
        self.__board : [] = [self.Mark.EMPTY] * 9
        pass

    def select(self, pos : int, mark : Mark):
        if pos >= len(self.__board) or pos < 0:
            raise BoardException("Nieprawidlowe wspolrzedne")
        if (self.__board[pos] != Board.Mark.EMPTY):
            raise BoardException("Wybrano zajete pole")
        self.__board[pos] = mark

    def asArray(self) -> [int]:
        return self.__board


    @staticmethod
    def getUserMarks():
        return [Board.Mark.NOUGHT, Board.Mark.CROSS]

