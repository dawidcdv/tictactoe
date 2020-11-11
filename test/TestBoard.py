import unittest
from src.tictactoe.game.Board import Board
from src.tictactoe.game.BoardException import BoardException

class BoardTest((unittest.TestCase)):
    def setUp(self):
        self.board = Board()

    def test_selected_field_board_is_correct(self):
        self.board.select(0,Board.Mark.CROSS)
        self.assertEqual(self.board.asArray()[0], Board.Mark.CROSS)

    def test_selected_all_fields_board_is_correct(self):
        for i in range(9):
            mark = Board.Mark.CROSS if i % 2 == 0 else Board.Mark.NOUGHT
            self.board.select(i, mark)

        expectArray=[Board.Mark.CROSS, Board.Mark.NOUGHT, Board.Mark.CROSS,
                     Board.Mark.NOUGHT, Board.Mark.CROSS, Board.Mark.NOUGHT,
                     Board.Mark.CROSS, Board.Mark.NOUGHT, Board.Mark.CROSS]

        self.assertEqual(expectArray,self.board.asArray())


    def test_select_out_of_top_range(self):
        with self.assertRaises(BoardException):
            self.board.select(9, Board.Mark.CROSS)

    def test_select_out_of_low_range(self):
        with self.assertRaises(BoardException):
            self.board.select(-1, Board.Mark.CROSS)

    def test_select_same_field_twice(self):
        with self.assertRaises(BoardException):
            self.board.select(4, Board.Mark.CROSS)
            self.board.select(4, Board.Mark.CROSS)



if __name__ == '__main__':
    unittest.main()


