from src.tictactoe.Application import Application
from src.tictactoe.console.input.Coordinate import Coordinate
from src.tictactoe.console.input.Input import Input
from src.tictactoe.console.input.InputAdapterFactory import InputAdapterFactory
from src.tictactoe.console.input.Sequence import Sequence
from src.tictactoe.console.printer.PrinterFactory import PrinterFactory
from src.tictactoe.console.Console import Console
from src.tictactoe.game.Tictactoe import Tictactoe
from src.tictactoe.gui.Gui import Gui


def askForIntOrGetZero(msg : str):
    try:
        return (int)(input(msg))
    except Exception:
        return 0

gameType = 0
while gameType not in [1,2]:
        gameType = askForIntOrGetZero("Jak chcesz zagrac ? \n1) GUI \n2) Konsola \n")



app : Application

if gameType == 1:
    app = Gui()

else:
    printerType=0
    while printerType not in PrinterFactory.getTypes():
        printerType = askForIntOrGetZero("Jak chcesz wysweitlac plansze ? \n1) W konsoli ?\n2) W przegladarce ?\n")
    printer = PrinterFactory.getPrinter(PrinterFactory.Type(printerType))

    inputType = 0
    while inputType not in InputAdapterFactory.getTypes():
        inputType = askForIntOrGetZero("Jak chcesz wprowadzac wspolrzedne ?\n 1) Kolejno od 1 do 9\n 2) Wspolrzedne jak dla mecierzy od 1 do 3, wiersz i kolumna rozdzielone przecinkiem ? ")
    inputAdapter = InputAdapterFactory.getAdapter(inputType)
    app = Console(printer, Input(inputAdapter))


app.run(Tictactoe())











