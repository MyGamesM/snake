from ..tile import Tile

class SnakeHead(Tile):
	def __init__(self, x: int, y: int) -> None:
		self.type = "SnakeHead"
		self.color = (128, 128, 128)
		self.x: int = x
		self.y: int = y

	def set_coords(self, x: int, y: int) -> None:
		self.x, self.y = x, y

	def get_coords(self) -> tuple[int, int]:
		return (self.x, self.y)