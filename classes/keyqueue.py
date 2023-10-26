from pygame import Vector2

class KeyQueue:
	def __init__(self) -> None:
		self.queue: list[Vector2] = []
		self.previous_move: Vector2 = Vector2(1, 0)
		self.previous_movement_vector: Vector2 = Vector2(1, 0)

	def append(self, vec: Vector2) -> None:
		self.queue.append(vec)

	def get_previous_movement_vector(self) -> Vector2:
		return self.previous_movement_vector

	def get_next_move(self) -> Vector2:
		if len(self.queue):
			next_move = self.queue.pop(0)
			if next_move == self.previous_movement_vector * -1:
				return self.previous_movement_vector

			self.previous_move = next_move
			self.previous_movement_vector = next_move
			return self.previous_movement_vector

		return self.previous_move