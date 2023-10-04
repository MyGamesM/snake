from pygame import Vector2

class KeyQueue:
	def __init__(self) -> None:
		self.queue: list[Vector2] = []
		self.previous_move: Vector2 = Vector2(1, 0)

	def append(self, vec: Vector2) -> None:
		self.queue.append(vec)

	def get_previous_move(self) -> Vector2:
		return self.previous_move


	def calculate_next_move(self) -> Vector2:
		result: Vector2 = Vector2(0, 0)
		last: Vector2 = Vector2(0, 0)
		if self.queue != []: last = self.queue[len(self.queue) - 1]

		for vec in self.queue:
			result += vec
		self.queue.clear()

		if result.length() != 0:
			self.previous_move = result
			return result
		else:
			return self.previous_move