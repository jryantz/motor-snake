from typing import List

class Move:
    up = 'up'
    down = 'down'
    left = 'left'
    right = 'right'

class Coord:
    def __init__(self, data):
        self.x = data['x']
        self.y = data['y']

        self.up = (self.x, self.y + 1)
        self.down = (self.x, self.y - 1)
        self.left = (self.x - 1, self.y)
        self.right = (self.x + 1, self.y)

    def get_xy(self) -> tuple:
        '''
        Use this function to get the x,y coordinate as a tuple.

        return: An x,y coordinate tuple.
        '''

        return (self.x, self.y)

class Board:
    def __init__(self, data):
        self.height = data['height']
        self.width = data['width']

        self._top_edge = self.height - 1
        self._bottom_edge = 0
        self._left_edge = 0
        self._right_edge = self.width - 1

    def check_top_edge(self, head: Coord) -> str:
        '''
        Use this function to check if the snake is going to fall off the top edge.

        return: The move that would kill the snake.
        '''

        if head.y == self._top_edge:
            return Move.up

    def check_bottom_edge(self, head: Coord) -> str:
        '''
        Use this function to check if the snake is going to fall off the bottom edge.

        return: The move that would kill the snake.
        '''

        if head.y == self._bottom_edge:
            return Move.down

    def check_left_edge(self, head: Coord) -> str:
        '''
        Use this function to check if the snake is going to fall off the left edge.

        return: The move that would kill the snake.
        '''

        if head.x == self._left_edge:
            return Move.left

    def check_right_edge(self, head: Coord) -> str:
        '''
        Use this function to check if the snake is going to fall off the right edge.

        return: The move that would kill the snake.
        '''

        if head.x == self._right_edge:
            return Move.right

class Snake:
    def __init__(self, data):
        self.head: Coord = Coord(data['head'])
        self.body: tuple = tuple(Coord(x) for x in data['body'])
        
        self.health: int = data['health']

    def get_neck(self) -> Coord:
        '''
        Use this function to get the Coord that the neck is in.

        return: The Coord of the neck.
        '''

        return self.body[1]

    def get_neck_direction(self):
        '''
        Use this function to figure out the direction to avoid so that the snake won't kill itself by eating its neck.

        return: The direction of the neck relative to the head.
        '''

        neck = self.get_neck().get_xy()

        if neck == self.head.up:
            return Move.up
        if neck == self.head.down:
            return Move.down
        if neck == self.head.left:
            return Move.left
        if neck == self.head.right:
            return Move.right

    def get_body(self) -> List[Coord]:
        '''
        Use this function to get the location of all of the snake's body parts.

        return: A Coord list that contains all of the points of the snakes body.
        '''

        return [x.get_xy() for x in self.body]
    
    def get_body_directions(self) -> list:
        '''
        Use this function to rule out the possibility of running into any of the snake's body parts.

        return: A list of moves that would kill the snake by eating itself.
        '''

        body = self.get_body()
        
        moves = []
        if self.head.up in body:
            moves.append(Move.up)
        if self.head.down in body:
            moves.append(Move.down)
        if self.head.left in body:
            moves.append(Move.left)
        if self.head.right in body:
            moves.append(Move.right)

        return moves