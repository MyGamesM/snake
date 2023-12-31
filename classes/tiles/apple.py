from pygame import Vector2
from ..tile import Tile

class Apple(Tile):
	def __init__(self, coords: Vector2):
		self.color = (255, 0, 0)
		self.__coords = coords

	@property
	def coords(self) -> Vector2:
		return self.__coords

	@coords.setter
	def set_coords(self, coords: Vector2) -> None:
		self.__coords = coords