import pygame
from Cube import Cube

class Snake(object):
	
	body = []
	turns = {}
	
	def __init__(self, color, position):
		self.color = color
		self.head = Cube(position)
		self.body.append(self.head)
		self.dirnx = 0
		self.dirny = 1

	def move(self):
		"""
		Evaluates Snake move action by key events
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dirnx = -1
					self.dirny = 0
					self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_RIGHT]:
					self.dirnx = 1
					self.dirny = 0
					self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_UP]:
					self.dirnx = 0
					self.dirny = -1
					self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_DOWN]:
					self.dirnx = 0
					self.dirny = 1
					self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

		for i, c in enumerate(self.body): # Loop through every cube in our body
			grid_position = c.position[:] # This stores the cubes position on the grid
			if grid_position in self.turns: # If the cubes current position is one where we turned
				turn = self.turns[grid_position] # Get the direction we should turn
				c.move(turn[0],turn[1]) # Move our cube in that direction
				if i == len(self.body)-1: # If this is the last cube in our body remove the turn from the dict
					self.turns.pop(grid_position)
			else:
				# If the cube reaches the edge of the screen we will make it appear on the opposite side
				if c.dirnx == -1 and c.position[0] <= 0: 
					c.position = (c.rows-1, c.position[1])
				elif c.dirnx == 1 and c.position[0] >= c.rows-1: 
					c.position = (0,c.position[1])
				elif c.dirny == 1 and c.position[1] >= c.rows-1: 
					c.position = (c.position[0], 0)
				elif c.dirny == -1 and c.position[1] <= 0: 
					c.position = (c.position[0],c.rows-1)
				else: c.move(c.dirnx,c.dirny) # If we haven't reached the edge just move in our current direction
		

	def reset(self, position):
		self.head = cube(position)
		self.body = []
		self.body.append(self.head)
		self.turns = {}
		self.dirnx = 0
		self.dirny = 1


	def add_cube(self):
		"""
		Adds a cube to snake body
		"""
		tail = self.body[-1]
		dx, dy = tail.dirnx, tail.dirny

		if dx == 1 and dy == 0:
			self.body.append(Cube((tail.position[0]-1,tail.position[1])))
		elif dx == -1 and dy == 0:
			self.body.append(Cube((tail.position[0]+1,tail.position[1])))
		elif dx == 0 and dy == 1:
			self.body.append(Cube((tail.position[0],tail.position[1]-1)))
		elif dx == 0 and dy == -1:
			self.body.append(Cube((tail.position[0],tail.position[1]+1)))

		self.body[-1].dirnx = dx
		self.body[-1].dirny = dy
		

	def draw(self, surface):
		"""
		Draws each cube in the Snake body
		"""
		for i, c in enumerate(self.body):
			if i ==0:
				c.draw(surface, True)
			else:
				c.draw(surface)