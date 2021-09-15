"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python tests.py -v

"""
import unittest

from server_logic import POSSIBLE_MOVES, choose_move

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
