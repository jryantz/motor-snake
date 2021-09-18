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

    nearest_food_location = board.get_nearest_food_location(snake.head)
    
    moves: set[str] = {}
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

    # Get the distance to the nearest piece of food.
    # Then add 5% margin of error to the distance.
    nearest_food_distance = board.get_nearest_food_distance(snake.head)
    #nearest_food_distance = nearest_food_distance + (nearest_food_distance * 0.05)

    recommended_moves: set[str] = available_moves
    # The snake loses 1 health with each move.
    # Therefore, if the health is less than or equal to the nearest food - start moving to it.
    if snake.health <= nearest_food_distance:
        # Make your Battlesnake move towards a piece of food on the board.
        goto_food_moves = get_food_moves(board, snake)
        recommended_moves = recommended_moves & goto_food_moves
    else:
        # Avoid food at all costs until necessary.
        avoid_food_moves = snake.get_food_directions(board.get_food())
        recommended_moves = recommended_moves - avoid_food_moves

        # Make sure that there are still moves available.
        # If not, add back the avoided food moves so that the snake doesn't kill itself.
        if len(recommended_moves) == 0:
            recommended_moves = available_moves

    move = random.choice(list(recommended_moves))

    # TODO: Explore new strategies for picking a move that are better than random.

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {recommended_moves}")

    return move
