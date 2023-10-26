import os, sys, pygame
from copy import copy
from pygame import Vector2

from classes.map import Map
from classes.tile import Tile
from classes.label import Label
from classes.keyqueue import KeyQueue

from classes.tiles.grass import Grass
from classes.tiles.apple import Apple
from classes.tiles.snakebody import SnakeBody

os.system("cls")

class Game:
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_caption("Snake")

		self.screen = pygame.display.set_mode((750, 750))
		self.clock = pygame.time.Clock()
		self.running: bool = True
		self.tick: int = 0
		self.move_ticks: list[int] = [19, 39, 59]
		self.move_tail_on_next_tick: bool = True
		self.eaten: int = 0
		self.diagonal: tuple[Vector2, Vector2, Vector2, Vector2] = (
			Vector2(1, 1), Vector2(-1, 1), Vector2(1, -1), Vector2(-1, -1)
		)

		self.map: Map = Map(10, 10)
		self.map.spawn_snake(Vector2(2, 1))
		self.map.spawn_apple()

		self.key_queue = KeyQueue()

		self.label = Label(self.screen, f"Apples: {self.eaten}", Vector2(20, 5), 30, pygame.Color(255, 255, 255))

		self.screen.fill("black")
		self.main_loop()

	def draw(self) -> None:
		blockSize = 65
		for y in range(10):
			for x in range(10):
				pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), pygame.Rect(0, 0, 200, 50))
				self.label.update(f"Apples: {self.eaten}")
				tile_type: Tile = self.map.get_tile(Vector2(x, y))
				pygame.draw.rect(self.screen, tile_type.color, (x * 65 + 50, y * 65 + 50, blockSize, blockSize))

	def die(self) -> None:
		pygame.quit()
		sys.exit()

	def on_tick(self) -> None:
		self.tick += 1
		self.draw()

		if self.tick > 59:
			self.tick = 0

		if self.tick in self.move_ticks:
			self.move()

	def move(self, movement_vector: Vector2 = Vector2(0, 0)) -> None:
		coords = self.map.snake_head.coords
		movement_vector = self.key_queue.get_next_move()

		new_coords = coords + movement_vector

		self.check_collision(new_coords)

		self.map.swap_tile_possition(coords, new_coords)
		self.map.snake_head.coords = new_coords

		new_tail_pos = copy(self.map.snake_body_list[-1].coords)

		for i, body_tile in enumerate(self.map.snake_body_list):
			self.map.swap_tile_possition(body_tile.coords, body_tile.coords + body_tile.movement_vector)
			body_tile.coords += body_tile.movement_vector

			if i == 0: body_tile.movement_vector = movement_vector
			else: body_tile.movement_vector = self.map.snake_body_list[i - 1].movement_vector

		if not self.move_tail_on_next_tick:
			self.move_tail_on_next_tick = True
			return

		self.map.swap_tile_possition(
			self.map.snake_tail.coords,
			new_tail_pos
		)
		self.map.snake_tail.coords = new_tail_pos

	def check_collision(self, vec: Vector2) -> None:
		if vec.x > 9 or vec.x < 0: self.die()
		if vec.y > 9 or vec.y < 0: self.die()

		if isinstance(self.map.get_tile(vec), Apple):
			self.eaten += 1
			self.map.eat_apple(self.map.apple.coords)
		elif not isinstance(self.map.get_tile(vec), Grass): self.die()

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

			pygame.display.flip()
			self.on_tick()
			self.clock.tick(60)

if __name__ == "__main__":
	game = Game()