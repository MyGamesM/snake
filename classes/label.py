import pygame

class Label:
	def __init__(self, screen: pygame.Surface, text: str,
			    coords: pygame.Vector2, font_size: int, color: pygame.Color) -> None:
		self.x: int = int(coords.x)
		self.y: int = int(coords.y)
		self.font_size: int = font_size
		self.color: pygame.Color = color
		self.screen: pygame.Surface = screen

		self.font = pygame.font.Font('./fonts/Hack.ttf', self.font_size)
		self.text = self.font.render(text, False, self.color)

	def draw(self) -> None:
		self.screen.blit(self.text, (self.x, self.y))

	def update(self, new_text: str) -> None:
		self.text = self.font.render(new_text, False, self.color)
		self.draw()
