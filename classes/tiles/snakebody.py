from pygame import Vector2

from ..tile import Tile

class SnakeBody(Tile):
	def __init__(self, coords: Vector2, movement_vec: Vector2) -> None:
		self.color = (0, 225, 0)
		self.__coords = coords
		self.__movement_vector = movement_vec

	@property
	def coords(self) -> Vector2:
		return self.__coords

	@coords.setter
	def coords(self, _coords) -> None:
		self.__coords = _coords

	@property
	def movement_vector(self) -> Vector2:
		return self.__movement_vector
	
	@movement_vector.setter
	def movement_vector(self, vec: Vector2) -> None:
		self.__movement_vector = vec