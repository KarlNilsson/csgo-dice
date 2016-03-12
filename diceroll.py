import os, sys, pygame, pygbutton

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300


def main():

	init_GUI()
	quit = False
	while not quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True


		pygame.display.update()

def init_GUI():
	pygame.init()
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption('CS:GO dice roll')
	screen.fill((24, 81, 186))

	font = pygame.font.Font(None, 30)
	text = font.render("Next round\'s loadout: ", 1, (40, 10, 10))
	#textpos.centerx = screen.get_rect().centerx
	screen.blit(text, pygame.Rect(10, 10, 150, 14))


	roll_button = pygbutton.PygButton((WINDOW_WIDTH - 100, 0, 100, 50), normal=(os.getcwd() + '\die.png'))
	roll_button.draw(screen)
	





if __name__ == '__main__':
	main()
	sys.exit()