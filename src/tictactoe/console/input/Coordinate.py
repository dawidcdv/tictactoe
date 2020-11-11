from src.tictactoe.console.input.InputAdapter import InputAdapter
from src.tictactoe.console.input.InputException import InputException


class Coordinate(InputAdapter):

    def convertToGamePosition(self, position : str) -> int:
        try:
            coordinates = position.split(",")
            row = ((int)(coordinates[0]))
            column = (int)(coordinates[1])
        except Exception as e:
            raise InputException("Wprowadzono nieprawidlowe wspolrzedne. Wprowadz dwie liczby od 1 do 3 rozdzielone przecinkiem")

        if(row not in [1,2,3] or column not in [1,2,3]):
            raise InputException("Wprowadzono wspolrzedne poza skala. Wprowadz dwie liczby od 1 do 3 rozdzielone przecinkiem")

        return row * 3 - 3 + column - 1