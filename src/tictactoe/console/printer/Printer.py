from src.tictactoe.game.Tictactoe import Tictactoe
from src.tictactoe.game.Board import Board
import abc

class Printer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def printBoard(self,board: Tictactoe):
        return

    def getCharForMark(self,mark) -> str:
        if mark == Board.Mark.NOUGHT: return "O"
        elif mark == Board.Mark.CROSS: return "X"
        return " "

    def printWinner(self,mark : Board.Mark):
        if(Board.Mark.CROSS == mark):
            print("Wygral Krzyzyk")
        elif(Board.Mark.NOUGHT == mark):
            print("Wygralo Kolko")
        else:
            print("Nikt nie wygral")

    def showCurrentMarkMove(self,mark: Board.Mark):
        print("Ruch: " + self.getCharForMark(mark))

