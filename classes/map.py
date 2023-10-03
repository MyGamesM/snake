from pygame import Vector2
from .tile import Tile
from .tiles.grass import Grass
from .tiles.snakehead import SnakeHead

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