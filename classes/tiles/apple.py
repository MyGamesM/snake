from pygame import Vector2
from ..tile import Tile

class Apple(Tile):
	def __init__(self, coords: Vector2):
		self.color = (255, 0, 0)
		self.coords = coords

	def set_coords(self, coords: Vector2) -> None:
		self.coords = coords

	def get_coords(self) -> Vector2:
		return self.coords