import unittest
from unittest import mock
from unittest.mock import Mock

from src.tictactoe.game.Board import Board
from src.tictactoe.game.Tictactoe import Tictactoe


class TictactoeTest((unittest.TestCase)):
    def test_not_finished_game(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.NOUGHT, Board.Mark.NOUGHT, Board.Mark.CROSS,
                                                           Board.Mark.EMPTY, Board.Mark.CROSS, Board.Mark.NOUGHT,
                                                           Board.Mark.EMPTY, Board.Mark.CROSS, Board.Mark.EMPTY]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), False)
            self.assertEqual(game.getWinner(), None)
            self.assertEqual(game.isFinished(), False)


    def test_draw(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.NOUGHT, Board.Mark.NOUGHT, Board.Mark.CROSS,
                                                           Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.NOUGHT,
                                                           Board.Mark.NOUGHT, Board.Mark.CROSS, Board.Mark.NOUGHT]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), False)
            self.assertEqual(game.getWinner(), None)
            self.assertEqual(game.isFinished(), True)

    def test_win_in_first_rows(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.CROSS,
                                                           Board.Mark.NOUGHT, Board.Mark.NOUGHT, Board.Mark.EMPTY,
                                                           Board.Mark.EMPTY, Board.Mark.EMPTY, Board.Mark.EMPTY]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.CROSS)
            self.assertEqual(game.isFinished(), True)

    def test_win_in_second_rows(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.NOUGHT, Board.Mark.NOUGHT, Board.Mark.EMPTY,
                                                           Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.CROSS,
                                                           Board.Mark.EMPTY, Board.Mark.EMPTY, Board.Mark.EMPTY]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.CROSS)
            self.assertEqual(game.isFinished(), True)

    def test_win_in_third_rows(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.EMPTY,
                                                           Board.Mark.EMPTY, Board.Mark.EMPTY, Board.Mark.EMPTY,
                                                           Board.Mark.NOUGHT, Board.Mark.NOUGHT, Board.Mark.NOUGHT]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.NOUGHT)
            self.assertEqual(game.isFinished(), True)

    def test_win_in_first_column(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.EMPTY,
                                                           Board.Mark.CROSS, Board.Mark.NOUGHT, Board.Mark.EMPTY,
                                                           Board.Mark.CROSS, Board.Mark.NOUGHT, Board.Mark.NOUGHT]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.CROSS)
            self.assertEqual(game.isFinished(), True)

    def test_win_in_second_column(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.NOUGHT, Board.Mark.CROSS, Board.Mark.EMPTY,
                                                           Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.EMPTY,
                                                           Board.Mark.NOUGHT, Board.Mark.CROSS, Board.Mark.NOUGHT]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.CROSS)
            self.assertEqual(game.isFinished(), True)

    def test_win_in_third_column(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.NOUGHT, Board.Mark.CROSS, Board.Mark.NOUGHT,
                                                           Board.Mark.CROSS, Board.Mark.EMPTY, Board.Mark.NOUGHT,
                                                           Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.NOUGHT]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.NOUGHT)
            self.assertEqual(game.isFinished(), True)


    def test_win_diagonally_from_left_top(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.NOUGHT, Board.Mark.CROSS, Board.Mark.EMPTY,
                                                           Board.Mark.CROSS, Board.Mark.NOUGHT, Board.Mark.NOUGHT,
                                                           Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.NOUGHT]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.NOUGHT)
            self.assertEqual(game.isFinished(), True)


    def test_win_diagonally_from_right_top(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.NOUGHT, Board.Mark.NOUGHT, Board.Mark.CROSS,
                                                           Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.NOUGHT,
                                                           Board.Mark.CROSS, Board.Mark.CROSS, Board.Mark.NOUGHT]
            game = Tictactoe(MockBoard())
            self.assertEqual(game.isWinner(), True)
            self.assertEqual(game.getWinner(), Board.Mark.CROSS)
            self.assertEqual(game.isFinished(), True)

    def test_board_as_array(self):
        with mock.patch('src.tictactoe.game.Board') as MockBoard:
            MockBoard.return_value.asArray.return_value = [Board.Mark.CROSS] * 9
            game = Tictactoe(MockBoard())
            self.assertEqual(game.getBoardAsArray(), [Board.Mark.CROSS] * 9)
            MockBoard.return_value.asArray.assert_called_once()


if __name__ == '__main__':
    unittest.main()


