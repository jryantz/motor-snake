# Battlesnake

**Snake Base - motor-snake**

## Layout

**Server Models**

The models used for translating the move data and providing accessor functions.

_Coord_: Represents each cell on the Board.

_Board_: Contains the size of the board and provides accessors for checking if the snake is near the edge of the board.

_Snake_: Represents one of the snakes on the board and contains accessors for getting stake location attributes.

**Server Logic**

The logic for moving the snake.

*choose_move*: Picks the most reasonable move to reduce the chance of death.

## Running Tests

``` shell
python tests.py -v
```