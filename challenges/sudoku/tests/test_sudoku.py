from challenges.sudoku.src.sudoku import Sudoku


def test_check_sudoku():
    puzzle1 = [[], [], [], [], [], [], [], [], []]
    assert not Sudoku.check_sudoku(puzzle1)

    puzzle2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert not Sudoku.check_sudoku(puzzle2)

    puzzle3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
               [2, 2, 2, 2, 2, 2, 2, 2, 2],
               [3, 3, 3, 3, 3, 3, 3, 3, 3],
               [4, 4, 4, 4, 4, 4, 4, 4, 4],
               [5, 5, 5, 5, 5, 5, 5, 5, 5],
               [6, 6, 6, 6, 6, 6, 6, 6, 6],
               [7, 7, 7, 7, 7, 7, 7, 7, 7],
               [8, 8, 8, 8, 8, 8, 8, 8, 8],
               [9, 9, 9, 9, 9, 9, 9, 9, 9]]
    assert not Sudoku.check_sudoku(puzzle3)

    puzzle4 = [[1, 2, 3, 1, 2, 3, 1, 2, 3],
               [4, 5, 6, 4, 5, 6, 4, 5, 6],
               [7, 8, 9, 7, 8, 9, 7, 8, 9],
               [1, 2, 3, 1, 2, 3, 1, 2, 3],
               [4, 5, 6, 4, 5, 6, 4, 5, 6],
               [7, 8, 9, 7, 8, 9, 7, 8, 9],
               [1, 2, 3, 1, 2, 3, 1, 2, 3],
               [4, 5, 6, 4, 5, 6, 4, 5, 6],
               [7, 8, 9, 7, 8, 9, 7, 8, 9]]
    assert not Sudoku.check_sudoku(puzzle4)

