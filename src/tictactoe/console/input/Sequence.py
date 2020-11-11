from src.tictactoe.console.input.InputAdapter import InputAdapter
from src.tictactoe.console.input.InputException import InputException


class Sequence(InputAdapter):

    def convertToGamePosition(self, position : str) -> int:
        try:
            return (int)(position) - 1
        except ValueError as e:
            raise InputException("Nie wprowadzono wartosci numerczynej. Wprowadz liczbe od 1 do 9")