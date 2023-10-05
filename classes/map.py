from random import randint
from pygame import Vector2

from .tile import Tile
from .tiles.grass import Grass
from .tiles.snakehead import SnakeHead
from .tiles.apple import Apple

class Map:
	def __init__(self, width: int, height: int) -> None:
		self.width: int = width
		self.height: int = height
		self.tiles: list[list[Tile]] = [[Grass() for _ in range(10)] for _ in range(10)]

	def set_tile(self, coords: Vector2, tile: Tile) -> None:
		self.tiles[int(coords.y)][int(coords.x)] = tile

	def get_tile(self, coords: Vector2) -> Tile:
		return self.tiles[int(coords.y)][int(coords.x)]

	def set_snake_head(self, coords: Vector2) -> None:
		self.snake_head = SnakeHead(coords)
		self.set_tile(coords, self.snake_head)
		self.snake_head.set_coords(coords)

	def set_tile_possition(self, coords: Vector2, new_coords: Vector2) -> None:
		x, y = coords.xy
		new_x, new_y = new_coords.xy
		x, y = int(x), int(y)
		new_x, new_y = int(new_x), int(new_y)

		self.tiles[y][x], self.tiles[new_y][new_x] = self.tiles[new_y][new_x], self.tiles[y][x]

	def spawn_apple(self) -> None:
		x, y = randint(0, 9), randint(0, 9)
		if (x, y) != self.snake_head.get_coords().xy:
			self.apple = Apple(Vector2(x, y))
			self.set_tile(Vector2(x, y), self.apple)
		else: self.spawn_apple()

	def eat_apple(self, apple_coords: Vector2) -> None:
		self.set_tile(apple_coords, Grass())
		self.spawn_apple()