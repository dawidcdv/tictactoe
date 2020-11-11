from src.tictactoe.console.printer.Printer import Printer
from src.tictactoe.game.Tictactoe import Tictactoe

class ConsoleBoardPrinter(Printer):

    def printBoard(self,game: Tictactoe):
        boardArray : list = game.getBoardAsArray()
        output : str = ""

        for i in range(len(boardArray)):
            if( (i + 1) % 3 == 0 ):
                output += self.getCharForMark(boardArray[i]) + self.__rowSeparator()
            else:
                output += self.getCharForMark(boardArray[i]) + self.__betweenSeparator()

        print(self.__trimLastRowSeparator(output))


    def __rowSeparator(self) -> str:
        return "\n-|-|-\n"

    def __betweenSeparator(self) -> str:
        return "|"

    def __trimLastRowSeparator(self, string: str) -> str:
        return string[0:len(string)-len(self.__rowSeparator())]



