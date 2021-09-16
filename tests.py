"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python tests.py -v

"""

import unittest

from server_logic import POSSIBLE_MOVES, UP, DOWN, LEFT, RIGHT, Coord, Board
from server_logic import neck_direction, top_edge, bottom_edge, left_edge, right_edge, entire_body, choose_move

class AvoidNeckTest(unittest.TestCase):
    def test_neck_at_starting_position(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = tuple(Coord(p) for p in [{"x": 5, "y": 5}, {"x": 5, "y": 5}, {"x": 5, "y": 5}])

        # Act
        result_move = neck_direction(test_head, test_body)

        # Assert
        self.assertEqual(result_move, None)

    def test_neck_left(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = tuple(Coord(p) for p in [{"x": 5, "y": 5}, {"x": 4, "y": 5}, {"x": 3, "y": 5}])

        # Act
        result_move = neck_direction(test_head, test_body)

        # Assert
        self.assertEqual(result_move, LEFT)

    def test_neck_right(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = tuple(Coord(p) for p in [{"x": 5, "y": 5}, {"x": 6, "y": 5}, {"x": 7, "y": 5}])

        # Act
        result_move = neck_direction(test_head, test_body)

        # Assert
        self.assertEqual(result_move, RIGHT)

    def test_neck_up(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = tuple(Coord(p) for p in [{"x": 5, "y": 5}, {"x": 5, "y": 6}, {"x": 5, "y": 7}])

        # Act
        result_move = neck_direction(test_head, test_body)

        # Assert
        self.assertEqual(result_move, UP)

    def test_neck_down(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = tuple(Coord(p) for p in [{"x": 5, "y": 5}, {"x": 5, "y": 4}, {"x": 5, "y": 3}])

        # Act
        result_move = neck_direction(test_head, test_body)

        # Assert
        self.assertEqual(result_move, DOWN)

class AvoidEdgeTest(unittest.TestCase):
    def test_top_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        test_head = Coord({"x": 5, "y": board.top_edge})

        # Act
        result_move = top_edge(test_head, board)

        # Assert
        self.assertEqual(result_move, UP)

    def test_bottom_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        test_head = Coord({"x": 5, "y": board.bottom_edge})

        # Act
        result_move = bottom_edge(test_head, board)

        # Assert
        self.assertEqual(result_move, DOWN)

    def test_left_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        test_head = Coord({"x": board.left_edge, "y": 5})

        # Act
        result_move = left_edge(test_head, board)

        # Assert
        self.assertEqual(result_move, LEFT)

    def test_right_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        test_head = Coord({"x": board.right_edge, "y": 5})

        # Act
        result_move = right_edge(test_head, board)

        # Assert
        self.assertEqual(result_move, RIGHT)

class AvoidSelfTest(unittest.TestCase):
    def test_up(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = (
            Coord({"x": 5, "y": 5}),
            Coord({"x": 5, "y": 6}),
        )

        # Act
        result_moves = entire_body(test_head, test_body)

        # Assert
        self.assertEqual(result_moves, [UP])

    def test_down(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = (
            Coord({"x": 5, "y": 5}),
            Coord({"x": 5, "y": 4}),
        )

        # Act
        result_moves = entire_body(test_head, test_body)

        # Assert
        self.assertEqual(result_moves, [DOWN])

    def test_left(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = (
            Coord({"x": 5, "y": 5}),
            Coord({"x": 4, "y": 5}),
        )

        # Act
        result_moves = entire_body(test_head, test_body)

        # Assert
        self.assertEqual(result_moves, [LEFT])

    def test_right(self):
        # Arrange
        test_head = Coord({"x": 5, "y": 5})
        test_body = (
            Coord({"x": 5, "y": 5}),
            Coord({"x": 6, "y": 5}),
        )

        # Act
        result_moves = entire_body(test_head, test_body)

        # Assert
        self.assertEqual(result_moves, [RIGHT])

class ChooseMoveTest(unittest.TestCase):
    def test_choose_move(self):
        data = {
            "game": {
                "id": "game-00fe20da-94ad-11ea-bb37",
                "ruleset": {
                    "name": "standard",
                    "version": "v.1.2.3"
                },
                "timeout": 500
            },
            "turn": 14,
            "board": {
                "height": 11,
                "width": 11,
                "food": [
                    {"x": 5, "y": 5}, 
                    {"x": 9, "y": 0}, 
                    {"x": 2, "y": 6}
                ],
                "hazards": [
                    {"x": 3, "y": 2}
                ],
                "snakes": [
                {
                    "id": "snake-508e96ac-94ad-11ea-bb37",
                    "name": "My Snake",
                    "health": 54,
                    "body": [
                        {"x": 0, "y": 0}, 
                        {"x": 1, "y": 0}, 
                        {"x": 2, "y": 0}
                    ],
                    "latency": "111",
                    "head": {"x": 0, "y": 0},
                    "length": 3,
                    "shout": "why are we shouting??",
                    "squad": ""
                }, 
                {
                    "id": "snake-b67f4906-94ae-11ea-bb37",
                    "name": "Another Snake",
                    "health": 16,
                    "body": [
                        {"x": 5, "y": 4}, 
                        {"x": 5, "y": 3}, 
                        {"x": 6, "y": 3},
                        {"x": 6, "y": 2}
                    ],
                    "latency": "222",
                    "head": {"x": 5, "y": 4},
                    "length": 4,
                    "shout": "I'm not really sure...",
                    "squad": ""
                }
                ]
            },
            "you": {
                "id": "snake-508e96ac-94ad-11ea-bb37",
                "name": "My Snake",
                "health": 54,
                "body": [
                    {"x": 0, "y": 0}, 
                    {"x": 1, "y": 0}, 
                    {"x": 2, "y": 0}
                ],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": ""
            }
        }

        result = choose_move(data)

        self.assertIn(result, POSSIBLE_MOVES)

if __name__ == "__main__":
    unittest.main()
