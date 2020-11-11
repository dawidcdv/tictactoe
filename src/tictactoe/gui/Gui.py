import tkinter as tk

from src.helper.FileHelper import FileHelper
from src.tictactoe.Application import Application
from src.tictactoe.game.Tictactoe import Tictactoe
from src.tictactoe.gui.View import View


class Gui(Application, View.Controller):

    APP_NAME = "Titactoe GUI"

    def __init__(self,root =tk.Tk):
        self.root =  root()


    def run(self, game=Tictactoe()):
        self.game=game
        self.root.title(self.APP_NAME)
        self.root.iconbitmap(FileHelper.getAssetFilePath('icon.ico'))
        self.view=View(self.root,self)
        self.view.createBoard()
        self.root.mainloop()


    def select(self, position : int):
        try:
            mark = self.game.curentMark
            self.game.select(position)
            self.view.checkOnBoard(position, mark)
            self.checkFinalConditions()
        except Exception as e:
            self.view.showError(e)

    def checkFinalConditions(self):
        if(self.game.isFinished()):
            self.view.showWinner(self.game.getWinner())
            exit(0)

