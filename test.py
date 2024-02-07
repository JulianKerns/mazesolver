import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 1
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells3(self):
        num_cols = 15
        num_rows = 15
        m1 = Maze(20, 20, num_rows, num_cols, 100 , 100)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_break_walls(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(20, 20, num_rows, num_cols, 100 , 100)
        self.assertEqual(m1._cells[0][0].has_top_wall,
                        False,)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)


    def test_maze_break_walls_r_and_revisited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(20, 20, num_rows, num_cols, 50 , 50, None , 10)
        self.assertEqual(m1._cells[0][0]._visited,False)
        self.assertEqual(m1._cells[-1][-1]._visited, False)

if __name__ == "__main__":
    unittest.main()

