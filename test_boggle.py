import unittest
import Boggle

class TestBoggle(unittest.TestCase):
    def test_Is_This_Thing_On(self):
        self.assertEquals(1, Boggle.check())
    def test_can_create_an_empty_grid(self):
        grid = Boggle.make_grid(0,0)
        self.assertEquals(len(grid), 0)