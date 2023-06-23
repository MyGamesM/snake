import os, pygame
from classes.tile import Tile
from classes.head import Head
from classes.types import types

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
		self.map: list[list[Tile]] = [[Tile(j, i) for j in range(10)] for i in range(10)]
		self.head_pos = (3, 3)

		self.map[3][3] = Head(3, 3, 1)

		self.screen.fill("black")

		self.main_loop()

	def draw(self) -> None:
		blockSize = 65
		for y in range(10):
			for x in range(10):
				tile = self.map[x][y].get_type()
				if tile == types["GRASS"]:
					pygame.draw.rect(self.screen, self.GRAY, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))
				elif tile == types["HEAD"]:
					pygame.draw.rect(self.screen, self.GREEN, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))

	def on_tick(self) -> None:
		self.tick += 1

		if self.tick > 59:
			self.tick = 0

		if self.tick == 44:
			y, x = self.head_pos
			self.map[y][x].update_position(x + 1, y)
			self.head_pos = (y, x + 1)

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
			print(self.head_pos)

			self.clock.tick(60)

if __name__ == "__main__":
	game = Game()