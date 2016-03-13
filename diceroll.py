import os, sys, pygame, pygbutton, dice

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BACKGROUND_COLOR = (34, 177, 26)

#MISC
DIE_CT  = os.getcwd() + '\pictures\misc\die-ct.png'
DIE_T   = os.getcwd() + '\pictures\misc\die-t.png'
DUMMY   = pygame.image.load(os.getcwd() + '\pictures\misc\dummy.png')
#PISTOLS
USP_S    = pygame.image.load(os.getcwd() + '\pictures\pistols\usp-s.png')
GLOCK    = pygame.image.load(os.getcwd() + '\pictures\pistols\dummy.png') 
BERETTAS = pygame.image.load(os.getcwd() + '\pictures\pistols\dual_berettas.png') 
P250     = pygame.image.load(os.getcwd() + '\pictures\pistols\p250.png')
CZ75     = pygame.image.load(os.getcwd() + '\pictures\pistols\cz75.png') 
DEAGLE   = pygame.image.load(os.getcwd() + '\pictures\pistols\deagle.png') 
#HEAVY
NOVA      = pygame.image.load(os.getcwd() + '\pictures\heavy\\fruktsallad.png')
XM1014    = pygame.image.load(os.getcwd() + '\pictures\heavy\\xm1014.png')
MAG7      = pygame.image.load(os.getcwd() + '\pictures\heavy\dummy.png')
SAWED_OFF = pygame.image.load(os.getcwd() + '\pictures\heavy\dummy.png')
M249      = pygame.image.load(os.getcwd() + '\pictures\heavy\dummy.png')
NEGEV     = pygame.image.load(os.getcwd() + '\pictures\heavy\\negev.png')
#SMGS
MAC10    = pygame.image.load(os.getcwd() + '\pictures\smg\mac10.png')
MP9      = pygame.image.load(os.getcwd() + '\pictures\smg\mp9.png')
MP7      = pygame.image.load(os.getcwd() + '\pictures\smg\mp7.png')
UMP45    = pygame.image.load(os.getcwd() + '\pictures\smg\ump45.png')
P90      = pygame.image.load(os.getcwd() + '\pictures\smg\p90.png')
PP_BIZON = pygame.image.load(os.getcwd() + '\pictures\smg\dummy.png')
#RIFLES

FAMAS = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
GALIL = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
M4A4  = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
AK47  = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
SCOUT = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
SG553 = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
AUG   = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
AWP   = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
AUTO  = pygame.image.load(os.getcwd() + '\pictures\\rifles/dummy.png')
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

	roll_button = pygbutton.PygButton((WINDOW_WIDTH - 100, 0, 100, 50), normal=DIE_CT)
	current_die = 'ct'

	quit = False

	t_pistol_img  = [GLOCK, BERETTAS, P250, CZ75, DEAGLE]
	ct_pistol_img = [USP_S, BERETTAS, P250, CZ75, DEAGLE]

	t_heavy_img   = [NOVA, XM1014, SAWED_OFF, M249, NEGEV]
	ct_heavy_img  = [NOVA, XM1014, MAG7, M249, NEGEV]

	t_smg_img     = [MAC10, MP7, UMP45, P90, PP_BIZON]
	ct_smg_img    = [MP9, MP7, UMP45, P90, PP_BIZON]

	t_rifle_img   = [GALIL, AK47, SCOUT, SG553, AWP, AUTO]
	ct_rifle_img  = [FAMAS, M4A4, SCOUT, AUG, AWP, AUTO]
	
	nades_img     = [MOLOTOV, DECOY, FLASHBANG, HE_GRENADE, SMOKE]
	equips_img    = [KEVLAR, HELMET, ZEUS, DEFKIT]
	
	pistol_img = ct_pistol_img
	heavy_img  = ct_heavy_img
	smg_img    = ct_smg_img
	rifle_img  = ct_rifle_img

	prim  = None
	sec   = None
	nades = []
	equip = []

	while not quit:
		pygame.draw.rect(screen, (200, 200, 200), prim_rect)
		pygame.draw.rect(screen, (200, 200, 200), sec_rect)
		pygame.draw.rect(screen, (200, 200, 200), nades_rect)
		pygame.draw.rect(screen, (200, 200, 200), equip_rect)

		pygame.draw.rect(screen, (100, 100, 100), prim_frame, 2)
		pygame.draw.rect(screen, (100, 100, 100), sec_frame, 2)
		pygame.draw.rect(screen, (100, 100, 100), nades_frame, 2)
		pygame.draw.rect(screen, (100, 100, 100), equip_frame, 2)

		roll_button.draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True



			if 'click' in roll_button.handleEvent(event):
				if event.button == 3:
					if current_die == 'ct':
						roll_button = pygbutton.PygButton((WINDOW_WIDTH - 100, 0, 100, 50), normal=DIE_T)
						current_die = 't'
						pistol_img = t_pistol_img
						heavy_img  = t_heavy_img
						smg_img    = t_smg_img
						rifle_img  = t_rifle_img
					else: 
						roll_button = pygbutton.PygButton((WINDOW_WIDTH - 100, 0, 100, 50), normal=DIE_CT)
						current_die = 'ct'
						pistol_img = ct_pistol_img
						heavy_img  = ct_heavy_img
						smg_img    = ct_smg_img
						rifle_img  = ct_rifle_img
				else:
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

		
		#ADD PISTOL
		if sec is not None:
			screen.blit(pistol_img[sec[1]-1], sec_rect)
		#ADD PRIMARY WEAPON
		if prim is not None:
			if prim[0] == 2:
				screen.blit(heavy_img[prim[1]-1], prim_rect)
			elif prim[0] == 3:
				screen.blit(smg_img[prim[1]-1], prim_rect)
			elif prim[0] == 4:
				screen.blit(rifle_img[prim[1]-1], prim_rect)
		#ADD NADES
		nade_index = 0
		for nade in nades:
			nade_img = nades_img[nade[1]-1]
			left = (nades_rect.left + 3) + (69 * (nade_index%2))
			top = (nades_rect.top + 2) + (41 * (nade_index/2))
			screen.blit(nade_img, pygame.Rect(left, top, 65, 35))
			nade_index += 1
		#ADD EQUIPMENT
		equip_index = 0
		for item in equip:
			if current_die == 't' and item[1] == 4:
				continue
			equip_img = equips_img[item[1]-1]
			left = (equip_rect.left + 3) + (69 * (equip_index%2))
			top = (equip_rect.top + 2) + (41 * (equip_index/2))
			screen.blit(equip_img, pygame.Rect(left, top, 65, 35))
			equip_index += 1

		pygame.display.flip()
		clock.tick(60)




if __name__ == '__main__':
	main()
	sys.exit()