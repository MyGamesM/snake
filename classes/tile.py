from .types import types

class Tile:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y
		self.type = types["GRASS"]

	def get_possition(self) -> tuple[int, int]:
		return self.x, self.y
	
	def update_position(self, new_x: int, new_y: int) -> None:
		self.x = new_x
		self.y = new_y

	def get_type(self) -> int:
		return self.type