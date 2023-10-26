from pygame import Vector2
from ..tile import Tile

class SnakeHead(Tile):
	def __init__(self, coords: Vector2) -> None:
		self.color = (0, 255, 0)
		self.__coords = coords

	@property
	def coords(self) -> Vector2:
		return self.__coords

	@coords.setter
	def coords(self, coords: Vector2) -> None:
		self.__coords = coords