from .tile import Tile
from .types import types

class Head(Tile):
	def __init__(self, x: int, y: int, dir: int) -> None:
		super().__init__(x, y)
		self.dir = dir
		self.type = types["HEAD"]

	def get_dir(self) -> int:
		return self.dir
	
	def update_dir(self, dir: int) -> None:
		self.dir = dir