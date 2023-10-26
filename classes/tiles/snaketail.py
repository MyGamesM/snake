from pygame import Vector2

from ..tile import Tile

class SnakeTail(Tile):
	def __init__(self, coords) -> None:
		self.color = (0, 200, 0)
		self.__coords = coords

	@property
	def coords(self) -> Vector2:
		return self.__coords

	@coords.setter
	def coords(self, _coords) -> None:
		self.__coords = _coords