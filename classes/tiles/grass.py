from ..tile import Tile

class Grass(Tile):
	def __init__(self) -> None:
		self.type = "Grass"
		self.color = (0, 255, 0)