"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python tests.py -v
"""

import unittest

from server_models import Move, Board, Snake
from server_logic import choose_move

class AvoidNeckTest(unittest.TestCase):
    def test_neck_at_starting_position(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 5, 'y': 5}, 
                {'x': 5, 'y': 5}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_neck_direction()

        # Assert
        self.assertEqual(move, None)

    def test_neck_up(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 5, 'y': 6}, 
                {'x': 5, 'y': 7}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_neck_direction()

        # Assert
        self.assertEqual(move, Move.up)
    
    def test_neck_down(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 5, 'y': 4}, 
                {'x': 5, 'y': 3}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_neck_direction()

        # Assert
        self.assertEqual(move, Move.down)

    def test_neck_left(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 4, 'y': 5}, 
                {'x': 3, 'y': 5}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_neck_direction()

        # Assert
        self.assertEqual(move, Move.left)

    def test_neck_right(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 6, 'y': 5}, 
                {'x': 7, 'y': 5}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_neck_direction()

        # Assert
        self.assertEqual(move, Move.right)

class AvoidEdgeTest(unittest.TestCase):
    def test_top_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        snake = Snake({
            'head': {'x': 5, 'y': 10},
            'body': []
        })

        # Act
        move = board.check_top_edge(snake.head)

        # Assert
        self.assertEqual(move, Move.up)

    def test_bottom_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        snake = Snake({
            'head': {'x': 5, 'y': 0},
            'body': []
        })

        # Act
        move = board.check_bottom_edge(snake.head)

        # Assert
        self.assertEqual(move, Move.down)

    def test_left_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        snake = Snake({
            'head': {'x': 0, 'y': 5},
            'body': []
        })

        # Act
        move = board.check_left_edge(snake.head)

        # Assert
        self.assertEqual(move, Move.left)

    def test_right_edge(self):
        # Arrange
        board = Board({'height': 11, 'width': 11})
        snake = Snake({
            'head': {'x': 10, 'y': 5},
            'body': []
        })

        # Act
        move = board.check_right_edge(snake.head)

        # Assert
        self.assertEqual(move, Move.right)

class AvoidSelfTest(unittest.TestCase):
    def test_up(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 5, 'y': 6}, 
                {'x': 5, 'y': 7}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_body_directions()

        # Assert
        self.assertEqual(move, [Move.up])

    def test_down(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 5, 'y': 4}, 
                {'x': 5, 'y': 3}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_body_directions()

        # Assert
        self.assertEqual(move, [Move.down])

    def test_left(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 4, 'y': 5}, 
                {'x': 3, 'y': 5}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_body_directions()

        # Assert
        self.assertEqual(move, [Move.left])

    def test_right(self):
        # Arrange
        snake = Snake({
            'body': [
                {'x': 5, 'y': 5}, 
                {'x': 6, 'y': 5}, 
                {'x': 7, 'y': 5}
            ],
            'head': {'x': 5, 'y': 5}
        })

        # Act
        move = snake.get_body_directions()

        # Assert
        self.assertEqual(move, [Move.right])

class ChooseMoveTest(unittest.TestCase):
    def test_choose_move(self):
        # Arrange
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

        # Act
        result = choose_move(data)

        # Assert
        self.assertIn(result, [Move.up, Move.down, Move.left, Move.right])

if __name__ == "__main__":
    unittest.main()
