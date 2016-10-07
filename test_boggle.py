import unittest
import Boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):

    def test_can_create_an_empty_grid(self):
        grid = Boggle.make_grid(0,0)
        self.assertEqual(len(grid), 0)

    def test_grid_size_is_width_times_height(self):
        grid = Boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        grid = Boggle.make_grid(2,2)
        self.assertTrue((0, 0) in grid)
        self.assertTrue((0, 1) in grid)
        self.assertTrue((1, 0) in grid)
        self.assertTrue((1, 1) in grid)
        self.assertTrue((2, 2) not in grid)

    def test_grid_is_filled_with_letters(self):
        grid = Boggle.make_grid(2, 3)
        for L in grid.values():
            self.assertTrue(L in ascii_uppercase)

    def test_neighbours_of_a_position(self):
        neighbours = Boggle.neighbours_of_position((1, 2))
        self.assertTrue((0, 1) in neighbours)
        self.assertTrue((0, 2) in neighbours)
        self.assertTrue((0, 3) in neighbours)
        self.assertTrue((1, 1) in neighbours)
        self.assertTrue((1, 3) in neighbours)
        self.assertTrue((2, 1) in neighbours)
        self.assertTrue((2, 2) in neighbours)
        self.assertTrue((2, 3) in neighbours)

    def test_all_grid_neighbours(self):
        grid = Boggle.make_grid (2, 2)
        neighbours = Boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        others = []
        for pos in grid:
            others[:] = grid
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))

    def test_converting_a_path_to_a_word(self):
        grid = Boggle.make_grid(2,2)
        oneLetterWord = Boggle.path_to_word(grid, [(0,0)])
        twoLetterWord = Boggle.path_to_word(grid, [(0,0),(1,1)])
        self.assertEqual(oneLetterWord, grid[(0,0)])
        self.assertEqual(twoLetterWord, grid[(0,0)] + grid[(1,1)])

    def test_search_grid_for_words(self):
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = "EEE"

        fullWords = [twoLetterWord, threeLetterWord, notThereWord]
        stems = ['A', 'AB', 'E', 'EE']
        dictionary = fullWords, stems

        foundWords = Boggle.search(grid, dictionary)

        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)

    def test_load_dictionary(self):
        dictionary = Boggle.get_dictionary('bogwords.txt')
        self.assertGreater(len(dictionary), 0)

    def test_is_this_thing_on(self):
        self.assertEquals(1, Boggle.check())