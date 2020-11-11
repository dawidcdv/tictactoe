from tkinter import  Button, messagebox
from abc import ABCMeta, abstractmethod
from src.tictactoe.game.Board import Board


class View:

    class Controller:
        __metaclass__ = ABCMeta
        @abstractmethod
        def select(self, position : int): raise NotImplementedError


    def __init__(self, tk, controller: Controller):
        self.root = tk
        self.controller = controller
        self.buttons = [None] * 9

    def createBoard(self):
        for i in range(9):
            self.buttons[i] = Button(self.root, text="", height=4, width=8,
                                     command=lambda pos=i: self.controller.select(pos))
            self.buttons[i].grid(row=((int)(i / 3)), column=(i % 3))

    def showWinner(self, mark : Board.Mark):
        if mark is None:
            message = "Remis"
        elif mark is Board.Mark.CROSS:
            message = "Wygral krzyzyk"
        else :
            message = "Wygralo kolko"
        messagebox.showinfo(title="Zwyciezca", message=message)

    def showError(self,errorText):
        messagebox.showerror(title="Blad", message=errorText)

    def checkOnBoard(self, pos, mark : Board.Mark):
        self.buttons[pos]["text"] = "X" if mark == Board.Mark.CROSS else "O"
