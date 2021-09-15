import random
from typing import List, Dict, Tuple

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

POSSIBLE_MOVES = {UP, DOWN, LEFT, RIGHT}

class Coord:
    def __init__(self, data):
        self.x = data['x']
        self.y = data['y']

        self.up = (self.x, self.y + 1)
        self.down = (self.x, self.y - 1)
        self.left = (self.x - 1, self.y)
        self.right = (self.x + 1, self.y)
    
    def as_tuple(self) -> Tuple:
        return (self.x, self.y)

class Board:
    def __init__(self, data):
        self.height = data['height']
        self.width = data['width']

        self.top_edge = self.height - 1
        self.bottom_edge = 0
        self.left_edge = 0
        self.right_edge = self.width - 1

class Snake:
    def __init__(self, data):
        self.head = Coord(data['head'])
        self.body = Tuple(Coord(c) for c in data['body'])

def neck_direction(head: Coord, body: Tuple[Coord]):
    neck = body[1].as_tuple()

    if neck == head.up:
        return UP
    if neck == head.down:
        return DOWN
    if neck == head.left:
        return LEFT
    if neck == head.right:
        return RIGHT

def entire_body(head: Coord, body: Tuple[Coord]):
    body_as_tuples = [p.as_tuple() for p in body]

    deadly_moves = []

    if head.up in body_as_tuples:
        deadly_moves.append(UP)
    if head.down in body_as_tuples:
        deadly_moves.append(DOWN)
    if head.left in body_as_tuples:
        deadly_moves.append(LEFT)
    if head.right in body_as_tuples:
        deadly_moves.append(RIGHT)

    return deadly_moves

def top_edge(head: Coord, board: Board):
    if head.y == board.top_edge:
        return UP

def bottom_edge(head: Coord, board: Board):
    if head.y == board.bottom_edge:
        return DOWN

def left_edge(head: Coord, board: Board):
    if head.x == board.left_edge:
        return LEFT

def right_edge(head: Coord, board: Board):
    if head.x == board.right_edge:
        return RIGHT

def is_edge(coord: Tuple, board: Board):
    return (
        coord[1] == board.top_edge
        or coord[1] == board.bottom_edge
        or coord[0] == board.left_edge
        or coord[0] == board.right_edge
    )

def edge_moves(head: Coord, board: Board):
    moves = []

    if is_edge(head.up, board):
        moves.append(UP)
    if is_edge(head.down, board):
        moves.append(DOWN)
    if is_edge(head.left, board):
        moves.append(LEFT)
    if is_edge(head.right, board):
        moves.append(RIGHT)

    return {m for m in moves}

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
        top_edge(snake.head, board),
        bottom_edge(snake.head, board),
        left_edge(snake.head, board),
        right_edge(snake.head, board),

        # Don't let your Battlesnake pick a move that would go back on itself.
        neck_direction(snake.head, snake.body),

        # Don't let your Battlesnake pick a move that would hit its own body.
        *entire_body(snake.head, snake.body),
    }

    available_moves = possible_moves - deadly_moves

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake.

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board.
    
    move = random.choice(List(available_moves))

    # TODO: Explore new strategies for picking a move that are better than random.

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {available_moves}")

    return move
