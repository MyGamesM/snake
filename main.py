import os, pygame

from classes.map import Map

from classes.tiles.grass import Grass
from classes.tiles.snakehead import SnakeHead

os.system("cls")

class Game:
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_caption("Snake")

		self.screen = pygame.display.set_mode((750, 750))
		self.clock = pygame.time.Clock()
		self.running: bool = True
		self.tick = 0

		self.GRAY: tuple[int, int, int] = (200, 200, 200)
		self.GREEN: tuple[int, int, int] = (0, 255, 0)
		self.map: Map = Map(10, 10)
		self.map.set_snake_head(0, 0)

		self.screen.fill("black")

		self.main_loop()

	def draw(self) -> None:
		blockSize = 65
		for y in range(10):
			for x in range(10):
				tile_type = self.map.get_tile(x, y)
				if isinstance(tile_type, Grass):
					pygame.draw.rect(self.screen, self.GREEN, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))
				elif isinstance(tile_type, SnakeHead):
					pygame.draw.rect(self.screen, self.GRAY, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))

	def on_tick(self) -> None:
		self.tick += 1

		if self.tick > 59:
			self.tick = 0

		if self.tick == 59:
			x, y = self.map.snake_head.get_coords()
			print(f"x: {x} y: {y}")
			self.map.set_tile_possition(x, y, x + 1, y)
			self.map.snake_head.set_coords(x + 1, y)

	def main_loop(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.running = False

			self.draw()

			pygame.display.flip()

			self.on_tick()

			self.clock.tick(60)

if __name__ == "__main__":
	game = Game()