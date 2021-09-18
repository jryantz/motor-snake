from typing import List

from scipy.spatial.distance import cdist

class Move:
    up = 'up'
    down = 'down'
    left = 'left'
    right = 'right'

class Coord:
    def __init__(self, data):
        if isinstance(data, dict):
            self.x = data['x']
            self.y = data['y']
        elif isinstance(data, tuple):
            self.x = data[0]
            self.y = data[1]
        else:
            raise Exception('data must be dict or tuple')

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
        self.food: tuple = tuple(Coord(x) for x in data['food'])

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

    def get_food(self) -> List[tuple]:
        '''
        Use this function to get the location of all of the food on the board.

        return: A list of tuples that contains all of the food on the board.
        '''

        return [x.get_xy() for x in self.food]

    def get_nearest_food_distance(self, head: Coord) -> float:
        '''
        Use this function to get the nearest food to the snakes head.

        return: The rough distance to the food.
        '''

        head = head.get_xy()
        food = self.get_food()

        # Check that there is food.
        if len(food) <= 0:
            return None

        distances = cdist([head], food, metric='cityblock')
        nearest = distances.min()

        return nearest

    def get_nearest_food_location(self, head: Coord) -> Coord:
        '''
        Use this function to get the nearest food to the snakes head.

        return: The Coord representing where the nearest piece of food is.
        '''

        head = head.get_xy()
        food = self.get_food()

        # Check that there is food.
        if len(food) <= 0:
            return None

        distances = cdist([head], food, metric='cityblock')
        nearest_index = distances.argmin()
        nearest = food[nearest_index]

        return Coord(nearest)

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

    def get_body(self) -> List[tuple]:
        '''
        Use this function to get the location of all of the snake's body parts.

        return: A list of tuples that contains all of the points of the snakes body.
        '''

        return [x.get_xy() for x in self.body]
    
    def get_body_directions(self) -> set[str]:
        '''
        Use this function to rule out the possibility of running into any of the snake's body parts.

        return: A list of moves that would kill the snake by eating itself.
        '''

        body = self.get_body()
        
        moves: set[str] = set()
        if self.head.up in body:
            moves.add(Move.up)
        if self.head.down in body:
            moves.add(Move.down)
        if self.head.left in body:
            moves.add(Move.left)
        if self.head.right in body:
            moves.add(Move.right)

        return moves

    def get_food_directions(self, food: set[Coord]) -> set[str]:
        '''
        Use this function to rule out the possibility of eating unintentionally.

        return: Set representing all moves where the snake would get food.
        '''
    
        moves: set[str] = set()
        if self.head.up in food:
            moves.add(Move.up)
        if self.head.down in food:
            moves.add(Move.down)
        if self.head.left in food:
            moves.add(Move.left)
        if self.head.right in food:
            moves.add(Move.right)

        return moves