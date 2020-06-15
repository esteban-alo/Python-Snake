import pygame
import random
import tkinter as tk
from tkinter import messagebox
from Cube import Cube
from Snake import Snake

def draw_grid(w, rows, surface):
	"""
	Add the grid lines to the window
	"""
	sizeBtwn = w // rows # Distance between the lines

	x = 0 # Keeps track of the current x
	y = 0 # Keeps track of the current y
	for l in range(rows):
		x = x + sizeBtwn
		y = y + sizeBtwn

		pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
		pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

def redraw_window(surface):
	"""
	Refresh 
	"""
	global rows, width, snake, snack
	surface.fill((0,0,0))
	snake.draw(surface)
	snack.draw(surface)
	draw_grid(width,rows, surface)
	pygame.display.update()


def random_snack(rows, item):
	"""
	Add a new cube (snack) in the window every time the snake collide 
	with objects
	"""	
	positions = item.body

	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)
		if len(list(filter(lambda z:z.position == (x,y), positions))) > 0:
			continue
		else:
			break
		
	return (x,y)


def message_box(subject, content):
	"""
	Messahe Box format
	"""
	root = tk.Tk()
	root.attributes("-topmost", True)
	root.withdraw()
	messagebox.showinfo(subject, content)
	try:
		root.destroy()
	except:
		pass


def main():
	global width, rows, snake, snack
	width = 500
	rows = 20
	window = pygame.display.set_mode((width, width))
	snake = Snake((255,0,0), (10,10))
	snack = Cube(random_snack(rows, snake), color=(250, 0, 0))
	flag = True

	clock = pygame.time.Clock()
	
	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		snake.move()
		if snake.body[0].position == snack.position:
			snake.add_cube()
			snack = Cube(random_snack(rows, snake), color=(250, 0, 0))

		for x in range(len(snake.body)):
			if snake.body[x].position in list(map(lambda z:z.position, snake.body[x+1:])): # Check if any of the positions in our body list overlap
				print('Score: ', len(snake.body))
				message_box('You Lost!', 'Play again...')
				snake.reset((10,10))
				break
		
		redraw_window(window)

main()
