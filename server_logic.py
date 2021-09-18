import random

from server_models import Move, Board, Snake

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""

POSSIBLE_MOVES = {Move.up, Move.down, Move.left, Move.right}

def get_deadly_moves(board: Board, snake: Snake) -> set[str]:
    '''
    Returns a set of every move that could kill the snake.

    return: Set representing all deadly moves.
    '''

    return {
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

def get_food_moves(board: Board, snake: Snake) -> set[str]:
    '''
    Returns a dictionary of moves that will navigate the snake to food.
    
    If there is no need for the snake to move to food, then every move is returned.

    return: Dictionary representing any move that would get the snake to food.
    '''

    # The list of moves to make to get to the nearest piece of food.
    moves: set[str] = {}

    # Get the distance to the nearest piece of food.
    nearest_food_distance = board.get_nearest_food_distance(snake.head)
    # Add a 30% margin of error to the distance.
    nearest_food_distance = nearest_food_distance + (nearest_food_distance * 0.3)

    # The snake loses 1 health with each move.
    # Therefore, if the health is less than or equal to the nearest food - start moving to it.
    if snake.health <= nearest_food_distance:
        nearest_food_location = board.get_nearest_food_location(snake.head)
        
        # If the head is to the left of the food, move right.
        if snake.head.x < nearest_food_location.x:
            moves.add(Move.right)
        # If the head is to the right of the food, move left.
        if snake.head.x > nearest_food_location.x:
            moves.add(Move.left)
        # If the head is above the food, move down.
        if snake.head.y > nearest_food_location.y:
            moves.add(Move.down)
        # If the head is below the food, move up.
        if snake.head.y < nearest_food_location.y:
            moves.add(Move.up)

        # Return the list of possible moves that will get the snake to the food.
        return moves

    # If the snake has no need to get food, then return a list of every possible move.
    return POSSIBLE_MOVES

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
    deadly_moves = get_deadly_moves(board, snake)
    available_moves = possible_moves - deadly_moves

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake.

    # Make your Battlesnake move towards a piece of food on the board.
    food_moves = get_food_moves(board, snake)
    
    # Get a set of all recommended moves with the intersection.
    # If moving to food isn't necessary, then food_moves will contain a list of every possible move.
    # With every possible move, this negates the effect of the food_moves set by returning just the available moves.
    recommended_moves = available_moves & food_moves
    move = random.choice(list(recommended_moves))

    # TODO: Explore new strategies for picking a move that are better than random.

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {recommended_moves}")

    return move
