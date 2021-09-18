import random

from server_models import Move, Board, Snake

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""

POSSIBLE_MOVES = {Move.up, Move.down, Move.left, Move.right}

def choose_move(data: dict) -> str:
    '''
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.
    '''

    board = Board(data['board'])
    snake = Snake(data['you'])

    possible_moves = POSSIBLE_MOVES

    deadly_moves = {
        # Don't let your Battlesnake move beyond the edges of the board.
        board.check_top_edge(snake.head),
        board.check_bottom_edge(snake.head),
        board.check_left_edge(snake.head),
        board.check_right_edge(snake.head),

        # Don't let your Battlesnake pick a move that would go back on itself.
        snake.get_neck_direction(),

        # Don't let your Battlesnake pick a move that would hit its own body.
        *snake.get_body_directions(),
    }

    available_moves = possible_moves - deadly_moves

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake.

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board.
    
    move = random.choice(list(available_moves))

    # TODO: Explore new strategies for picking a move that are better than random.

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {available_moves}")

    return move
