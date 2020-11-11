from src.tictactoe.console.input.Coordinate import Coordinate
from src.tictactoe.console.input.InputAdapter import InputAdapter
from src.tictactoe.console.input.Sequence import Sequence

class InputAdapterFactory:

    SEQUENCE = 1
    COORDINATE = 2

    @staticmethod
    def getAdapter(type : int) -> InputAdapter:
        if type == InputAdapterFactory.SEQUENCE: return Sequence()
        elif type == InputAdapterFactory.COORDINATE: return Coordinate()
        else: Exception("Unsopported type")

    @staticmethod
    def getTypes():
        return [InputAdapterFactory.SEQUENCE, InputAdapterFactory.COORDINATE]
