import os, pygame

from classes.map import Map
from classes.keyqueue import KeyQueue

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

		self.map: Map = Map(10, 10)
		self.map.set_snake_head(pygame.Vector2(0, 0))

		self.key_queue = KeyQueue()

		self.screen.fill("black")

		self.main_loop()

	def draw(self) -> None:
		blockSize = 65
		for y in range(10):
			for x in range(10):
				tile_type = self.map.get_tile(pygame.Vector2(x, y))
				if isinstance(tile_type, Grass):
					pygame.draw.rect(self.screen, tile_type.color, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))
				elif isinstance(tile_type, SnakeHead):
					pygame.draw.rect(self.screen, tile_type.color, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))

	def on_tick(self) -> None:
		self.tick += 1

		if self.tick > 59:
			self.tick = 0

		if self.tick == 59 or self.tick == 29:
			self.move()

	def move(self) -> None:
		coords = self.map.snake_head.get_coords()
		new_coords = coords + self.key_queue.calculate_next_move()
		self.map.set_tile_possition(coords, new_coords)
		self.map.snake_head.set_coords(new_coords)

	def main_loop(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.running = False
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						# self.map.snake_head.set_direction(pygame.Vector2(0, -1))
						self.key_queue.append(pygame.Vector2(0, -1))
					if event.key == pygame.K_DOWN or event.key == pygame.K_s:
						# self.map.snake_head.set_direction(pygame.Vector2(0, 1))
						self.key_queue.append(pygame.Vector2(0, 1))
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						# self.map.snake_head.set_direction(pygame.Vector2(-1, 0))
						self.key_queue.append(pygame.Vector2(-1, 0))
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						# self.map.snake_head.set_direction(pygame.Vector2(1, 0))
						self.key_queue.append(pygame.Vector2(1, 0))

			self.draw()

			pygame.display.flip()

			self.on_tick()

			self.clock.tick(60)

if __name__ == "__main__":
	game = Game()