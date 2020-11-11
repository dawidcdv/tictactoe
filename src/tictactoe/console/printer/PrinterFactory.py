from enum import IntEnum
from src.tictactoe.console.printer.ConsoleBoardPrinter import ConsoleBoardPrinter
from src.tictactoe.console.printer.Printer import Printer
from src.tictactoe.console.printer.WebBoardPrinter import WebPrinter


class PrinterFactory:

    class Type(IntEnum):
        Console = 1
        Browser = 2

    @staticmethod
    def getPrinter(type : Type) -> Printer:
        if type == PrinterFactory.Type.Console: return ConsoleBoardPrinter()
        elif type == PrinterFactory.Type.Browser: return WebPrinter()
        else: Exception("Unsoported type")

    @staticmethod
    def getTypes():
        return list(map(int, PrinterFactory.Type))


