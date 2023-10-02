from dataclasses import dataclass

@dataclass
class Tile:
	type: str
	color: tuple[int, int, int]