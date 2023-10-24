from pygame import Vector2

from ..tile import Tile

class SnakeBody(Tile):
	def __init__(self, coords) -> None:
		self.color = (0, 225, 0)
		self.__coords = coords

	@property
	def coords(self) -> Vector2:
		return self.__coords

	@coords.setter
	def set_coords(self, _coords) -> None:
		self.__coords = _coords