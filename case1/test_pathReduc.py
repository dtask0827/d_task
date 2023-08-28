from reduction import pathReduc
import unittest


class TestPathReduc(unittest.TestCase):
    def test_pathReduc(self):
        self.assertEqual(pathReduc(["NORTH", "WEST", "SOUTH", "EAST"]), [
                         "NORTH", "WEST", "SOUTH", "EAST"])
        self.assertEqual(pathReduc(["NORTH", "SOUTH", "EAST", "WEST"]), [])
        self.assertEqual(pathReduc(
            ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]), ["WEST", "WEST"])
        self.assertEqual(pathReduc(
            ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
        self.assertEqual(pathReduc(["NORTH", "EAST", "EAST", "WEST", "NORTH", "NORTH", "SOUTH"]), [
                         "NORTH", "EAST", "NORTH"])
        self.assertEqual(pathReduc(["NORTH", "NORTH", "EAST", "EAST", "SOUTH", "SOUTH", "WEST", "WEST"]), [
                         "NORTH", "NORTH", "EAST", "EAST", "SOUTH", "SOUTH", "WEST", "WEST"])
        self.assertEqual(
            pathReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]), [])
        self.assertEqual(pathReduc(["NORTH", "WEST", "SOUTH", "EAST"]), [
                         "NORTH", "WEST", "SOUTH", "EAST"])


if __name__ == '__main__':
    unittest.main()
