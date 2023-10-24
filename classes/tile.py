from dataclasses import dataclass

@dataclass
class Tile:
	_color: tuple[int, int, int]

	@property
	def color(self) -> tuple[int, int, int]:
		return self._color

	@color.setter
	def color(self, color: tuple[int, int, int]) -> None:
		self._color = color