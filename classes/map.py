from .tile import Tile
from .tiles.grass import Grass
from .tiles.snakehead import SnakeHead

class Map:
	def __init__(self, width: int, height: int) -> None:
		self.width: int = width
		self.height: int = height
		self.tiles: list[list[Tile]] = [[Grass() for _ in range(10)] for _ in range(10)]

	def set_tile(self, x: int, y: int, tile: Tile) -> None:
		self.tiles[y][x] = tile

	def get_tile(self, x: int, y: int) -> Tile:
		return self.tiles[y][x]

	def set_snake_head(self, x: int, y: int) -> None:
		self.snake_head = SnakeHead(3, 3)
		self.set_tile(y, x, self.snake_head)
		self.snake_head.set_coords(x, y)

	def set_tile_possition(self, x: int, y: int, new_x: int, new_y: int) -> None:
		self.tiles[y][x], self.tiles[new_y][new_x] = self.tiles[new_x][new_y], self.tiles[y][x]