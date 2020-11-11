from src.tictactoe.game.Board import Board

class Tictactoe:

    def __init__(self, board : Board = None, firstMoveMark : Board.Mark = None):
        self.__board = board or Board()
        self.curentMark = firstMoveMark or Board.Mark.CROSS


    def isFinished(self) -> bool:
        return True if self.isWinner() or self.isEndOfMoves() else False

    def isWinner(self) -> bool:
        return  self.getWinner() != None

    def select(self, pos):
        self.__board.select(pos, self.curentMark)
        self.__changeMark()


        return True

    def getBoardAsArray(self) -> [int]:
        return self.__board.asArray()

    def getWinner(self) -> Board.Mark:
        board = self.__board.asArray()
        if board[0]== board[1] and board[1] == board[2] and board[2] != Board.Mark.EMPTY: return board[2]
        if board[3]== board[4] and board[4] == board[5] and board[5] != Board.Mark.EMPTY: return board[5]
        if board[6]== board[7] and board[7] == board[8] and board[8] != Board.Mark.EMPTY: return board[8]
        if board[0]== board[3] and board[3] == board[6] and board[6] != Board.Mark.EMPTY: return board[6]
        if board[1]== board[4] and board[4] == board[7] and board[7] != Board.Mark.EMPTY: return board[7]
        if board[2]== board[5] and board[5] == board[8] and board[8] != Board.Mark.EMPTY: return board[8]
        if board[0]== board[4] and board[4] == board[8] and board[8] != Board.Mark.EMPTY: return board[8]
        if board[2]== board[4] and board[4] == board[6] and board[6] != Board.Mark.EMPTY: return board[6]
        return None;

    def __changeMark(self):
        self.curentMark = Board.Mark.NOUGHT if self.curentMark == Board.Mark.CROSS else Board.Mark.CROSS

    def isEndOfMoves(self) -> bool:
        for mark in self.__board.asArray():
            if mark is Board.Mark.EMPTY:
                return False
        return True