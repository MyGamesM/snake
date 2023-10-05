import os, sys, pygame
from pygame import Vector2

from classes.map import Map
from classes.tile import Tile
from classes.keyqueue import KeyQueue

from classes.tiles.apple import Apple

os.system("cls")

class Game:
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_caption("Snake")

		self.screen = pygame.display.set_mode((750, 750))
		self.clock = pygame.time.Clock()
		self.running: bool = True
		self.tick: int = 0
		self.eaten: int = 0
		self.diagonal: tuple[Vector2, Vector2, Vector2, Vector2] = (
			Vector2(1, 1), Vector2(-1, 1), Vector2(1, -1), Vector2(-1, -1)
		)

		self.map: Map = Map(10, 10)
		self.map.set_snake_head(Vector2(0, 0))
		self.map.spawn_apple()

		self.key_queue = KeyQueue()

		self.screen.fill("black")
		self.main_loop()

	def draw(self) -> None:
		blockSize = 65
		for y in range(10):
			for x in range(10):
				tile_type: Tile = self.map.get_tile(Vector2(x, y))
				pygame.draw.rect(self.screen, tile_type.color, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))

	def die(self) -> None:
		pygame.quit()
		sys.exit()

	def on_tick(self) -> None:
		self.tick += 1

		if self.tick > 59:
			self.tick = 0

		if self.tick == 59 or self.tick == 29:
			self.move()

	def move(self, next_move: Vector2 = Vector2(0, 0)) -> None:
		coords = self.map.snake_head.get_coords()
		if next_move.length() == 0: next_move = self.key_queue.calculate_next_move()

		if next_move in self.diagonal:
			self.move_diagonal(next_move)
			return

		new_coords = coords + next_move

		self.check_collision(new_coords)

		self.map.set_tile_possition(coords, new_coords)
		self.map.snake_head.set_coords(new_coords)

	def move_diagonal(self, next_move: Vector2) -> None:
		self.move(Vector2(next_move.x, 0))
		self.move(Vector2(0, next_move.y))

	def check_collision(self, vec: Vector2) -> None:
		if vec.x > 9 or vec.x < 0: self.die()
		if vec.y > 9 or vec.y < 0: self.die()

		if isinstance(self.map.get_tile(vec), Apple):
			self.eaten += 1
			self.map.eat_apple(self.map.apple.get_coords())

	def main_loop(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.running = False
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						self.key_queue.append(Vector2(0, -1))
					if event.key == pygame.K_DOWN or event.key == pygame.K_s:
						self.key_queue.append(Vector2(0, 1))
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						self.key_queue.append(Vector2(-1, 0))
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						self.key_queue.append(Vector2(1, 0))

			self.draw()
			pygame.display.flip()
			self.on_tick()
			self.clock.tick(60)

if __name__ == "__main__":
	game = Game()