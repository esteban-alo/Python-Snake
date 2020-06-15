import pygame

class Cube(object):
	
	rows = 20
	width = 500
	
	def __init__(self, start, dirnx=1, dirny=0, color=(0, 255, 0)):
		self.position = start
		self.dirnx = 1
		self.dirny = 0
		self.color = color
		
	def move(self, dirnx, dirny):
		"""
		Change cube position
		"""
		self.dirnx = dirnx
		self.dirny = dirny
		self.position = (self.position[0] + self.dirnx, self.position[1] + self.dirny)

	def draw(self, surface, eyes=False):
		"""
		Calculate the cube postion over the grid
		"""
		dis = self.width // self.rows
		i = self.position[0]
		j = self.position[1]

		pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
		if eyes:
			centre = dis//2
			radius = 3
			circleMiddle = (i*dis+centre-radius, j*dis+8)
			circleMiddle2 = (i*dis+dis-radius*2, j*dis+8)
			pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
			pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)