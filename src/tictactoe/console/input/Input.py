from src.tictactoe.console.input.InputAdapter import InputAdapter

class Input:

    def __init__(self, adapter : InputAdapter):
        self.adapter = adapter

    def askForPosition(self) -> int:
        return self.adapter.convertToGamePosition(input("Podaj wspolrzedne "))
