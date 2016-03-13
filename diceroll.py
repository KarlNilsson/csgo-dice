import os, sys, pygame, pygbutton, dice

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BACKGROUND_COLOR = (24, 81, 186)

#PISTOLS
USP_S = pygame.image.load(os.getcwd() + '\pictures\pistols\usp-s.png')
P250  = pygame.image.load(os.getcwd() + '\pictures\pistols\p250.png')
#GRENADES
HE_GRENADE  = pygame.image.load(os.getcwd() + '\pictures\\nades\he.png')
DECOY	 	= pygame.image.load(os.getcwd() + '\pictures\\nades\decoy.png')
MOLOTOV		= pygame.image.load(os.getcwd() + '\pictures\\nades\molotov.png')
FLASHBANG	= pygame.image.load(os.getcwd() + '\pictures\\nades\\flash.png')
SMOKE  		= pygame.image.load(os.getcwd() + '\pictures\\nades\smoke.png')
#EQUIPMENT
KEVLAR 		= pygame.image.load(os.getcwd() + '\pictures\equipment\kevlar.png')
HELMET 		= pygame.image.load(os.getcwd() + '\pictures\equipment\helmet.png')
ZEUS 		= pygame.image.load(os.getcwd() + '\pictures\equipment\zeus.png')
DEFKIT 		= pygame.image.load(os.getcwd() + '\pictures\equipment\defkit.png')



def main():

	pygame.init()
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption('CS:GO dice roll')
	screen.fill(BACKGROUND_COLOR)
	clock = pygame.time.Clock()

	font1 = pygame.font.Font(None, 30)
	font2 = pygame.font.Font(None, 25)
	h1 = font1.render("Next round\'s loadout: ",	1, (0, 0, 0))

	prim_text  = font2.render("Primary weapon",	1, (20, 10, 10))
	sec_text   = font2.render("Secondary weapon",	1, (20, 10, 10))
	nades_text = font2.render("Grenades",			1, (20, 10, 10))
	equip_text = font2.render("Equipment",		1, (20, 10, 10))

	screen.blit(h1,			pygame.Rect(10, 10, 150, 14))
	screen.blit(prim_text,	pygame.Rect(10, 60, 150, 14))
	screen.blit(sec_text,	pygame.Rect(200, 60, 150, 14))
	screen.blit(nades_text,	pygame.Rect(10, 180, 150, 14))
	screen.blit(equip_text,	pygame.Rect(200, 180, 150, 14))

	prim_rect  = pygame.Rect(10, 90, 140, 80)
	sec_rect   = pygame.Rect(200, 90, 140, 80)
	nades_rect = pygame.Rect(10, 210, 140, 80)
	equip_rect = pygame.Rect(200, 210, 140, 80)

	prim_frame  = pygame.Rect(8, 88, 144, 84)
	sec_frame   = pygame.Rect(198, 88, 144, 84)
	nades_frame = pygame.Rect(8, 208, 144, 84)
	equip_frame = pygame.Rect(198, 208, 144, 84)

	roll_button = pygbutton.PygButton((WINDOW_WIDTH - 100, 0, 100, 50), normal=(os.getcwd() + '\pictures\die.png'))

	quit = False

	prim_img   = None
	sec_img    = [USP_S, P250, USP_S, P250, USP_S, P250]
	nades_img  = [MOLOTOV, DECOY, FLASHBANG, HE_GRENADE, SMOKE]
	equips_img = [KEVLAR, HELMET, ZEUS, DEFKIT]

	prim  = None
	sec   = None
	nades = []
	equip = []

	while not quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True

			pygame.draw.rect(screen, (200, 200, 200), prim_rect)
			pygame.draw.rect(screen, (200, 200, 200), sec_rect)
			pygame.draw.rect(screen, (200, 200, 200), nades_rect)
			pygame.draw.rect(screen, (200, 200, 200), equip_rect)

			pygame.draw.rect(screen, (100, 100, 100), prim_frame, 2)
			pygame.draw.rect(screen, (100, 100, 100), sec_frame, 2)
			pygame.draw.rect(screen, (100, 100, 100), nades_frame, 2)
			pygame.draw.rect(screen, (100, 100, 100), equip_frame, 2)


			if 'click' in roll_button.handleEvent(event):
				prim  = None
				sec   = None
				nades = []
				equip = []
				nade_count = 0
				equip_count = 0
				loadout = dice.roll_session()
				print loadout
				for item in loadout:
					if item[0] == 1:
						sec = item
					elif item[0] == 5:
						equip.append(item)
					elif item[0] == 6:
						nades.append(item)
					else:
						prim = item

		roll_button.draw(screen)

		#if prim_img is not None:
			#screen.blit(prim_img, prim_rect)
		if sec is not None:
			screen.blit(sec_img[sec[1]-1], sec_rect)
			#print sec_img[0]

		nade_index = 0
		for nade in nades:
			nade_img = nades_img[nade[1]-1]

			left = (nades_rect.left + 3) + (69 * (nade_index%2))
			top = (nades_rect.top + 2) + (41 * (nade_index/2))

			screen.blit(nade_img, pygame.Rect(left, top, 65, 35))
			nade_index += 1

		equip_index = 0
		for item in equip:
			equip_img = equips_img[item[1]-1]
			left = (equip_rect.left + 3) + (69 * (equip_index%2))
			top = (equip_rect.top + 2) + (41 * (equip_index/2))

			screen.blit(equip_img, pygame.Rect(left, top, 65, 35))
			equip_index += 1



			
		#for equip in equip_img:
			#screen.blit(equip, pos)


		pygame.display.flip()
		pygame.display.update()




		clock.tick(60)




if __name__ == '__main__':
	main()
	sys.exit()