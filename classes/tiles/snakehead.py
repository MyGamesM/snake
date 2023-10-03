from pygame import Vector2
from ..tile import Tile

class SnakeHead(Tile):
	def __init__(self, coords: Vector2) -> None:
		self.color = (0, 255, 0)
		self.coords = coords

	def set_coords(self, coords: Vector2) -> None:
		self.coords = coords

	def get_coords(self) -> Vector2:
		return self.coords

	def calculate_direction(self, vec1: Vector2, vec2: Vector2) -> Vector2:
		return Vector2(
			max(min(vec1.x + vec2.x, 1), 0),
			max(min(vec2.x + vec2.y, 1), 0)
		)