from src.tictactoe.console.input.Input import Input
from src.tictactoe.game import Tictactoe
from src.tictactoe.Application import Application
from src.tictactoe.game.Board import Board
from src.tictactoe.console.printer.Printer import Printer
from src.tictactoe.game.Tictactoe import Tictactoe


class Console(Application):

    def __init__(self,  printer : Printer, input : Input):
        self.printer = printer
        self.input = input

    def run(self, game=None):
        self.game = game or Tictactoe()

        while not self.game.isFinished():
            self.printer.showCurrentMarkMove(self.game.curentMark)
            try:
                pos = self.input.askForPosition()
                self.game.select(pos)
            except Exception as e:
                print(e)
                continue

            self.printer.printBoard(self.game)

        mark : Board.Mark = self.game.getWinner()
        self.printer.printWinner(mark)


