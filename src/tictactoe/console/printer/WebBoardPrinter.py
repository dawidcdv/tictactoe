from src.tictactoe.game.Tictactoe import Tictactoe
import webbrowser
from src.helper.FileHelper import FileHelper
from src.tictactoe.console.printer.Printer import Printer

class WebPrinter(Printer):

    HTML_TEMPLATE_FILE = 'template.html'
    HTML_VIEW_FILE = 'view.html'


    def printBoard(self, game :Tictactoe):
        boardArray = game.getBoardAsArray()
        view = self.getHtmlView(boardArray)

        self.__saveHtmlView(view)
        webbrowser.open("file://" + FileHelper.getTmpFilePath(self.HTML_VIEW_FILE))

    def getHtmlView(self,boardArray) -> str:
        template = self.__getTemplate()


        for i in range(len(boardArray)):
            template = template.replace(self.__getPlaceHolder(i), self.getCharForMark(boardArray[i]))

        return template

    def __getPlaceHolder(self, pos: int) -> str:
        return "${" + str(pos) + "}"

    def __saveHtmlView(self, html):
        FileHelper.saveInTmp(self.HTML_VIEW_FILE, html)

    def __getTemplate(self) -> str:
        path = FileHelper.getTemplateFilePath(self.HTML_TEMPLATE_FILE)
        with open(path, 'r') as file:
            return file.read()





