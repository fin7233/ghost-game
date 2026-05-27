# fin7233
# ghost game

# import modules
import pygame
import random
# initiate Pygame engine
pygame.init()

# define Pygame window
screenX = 1280
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("ghost game")

# define Pygame clock
clock = pygame.time.Clock()
# fonts:D
bigFont = pygame.font.Font(None,72)
midFont = pygame.font.Font(None,30)
smlFont = pygame.font.Font(None,17)

# colourful world!!
BLACK = (   0,   0,   0 )
WHITE = ( 255, 255, 255 )
RED   = ( 255,   0,   0 )
GREEN = (   0, 255,   0 )
BLUE  = (   0,   0, 255 )
PINK  = ( 255, 182, 193 )

# begin variable definitions --------------------

LeftArrow=RightArrow=UpArrow=DownArrow=0
x = y = 300
speed = 8
score = 0
# loop until closed by user
done = False
# begin function definitions --------------------

def randScreenPos(xOffset,yOffset):
	randX = random.randint(xOffset,1280-xOffset)
	randY = random.randint(yOffset,800-yOffset)
	return (randX,randY)

def drawChar(x,y):
	pygame.draw.circle(screen, RED, (x,y), 40, 0)

def drawPellets():
	global score
	for i in pellets:
		pygame.draw.circle(screen,BLUE, i, 10,0)
		if arbitraryCollisionCheck((x,y),i,40,10):
			i[0],i[1] = randScreenPos(5,5)
			score += 1
			print(f"score: {score}")



def drawGhosts():
	for i in ghosts:
		ghostSpeedX = i[2]
		ghostSpeedY = i[3]
		diffX = x-i[0]
		diffY = y-i[1]
		if x > i[0]:
			i[0] += ghostSpeedX
		if x < i[0]:
			i[0] -= ghostSpeedX
		if y > i[1]:
			i[1] += ghostSpeedY
		if y < i[1]:
			i[1] -= ghostSpeedY
		pygame.draw.circle(screen,GREEN, (i[0],i[1]),30,0)

def arbitraryCollisionCheck(obj1,obj2,obj1Rad,obj2Rad):
	"""
	checks for collision between two objects
	inputs:
		obj1: tuple of (object1X,object1Y) (object center)
		obj2: tuple of (object2X,object2Y) (object center)
		obj1Rad: radius of object 1
		obj2Rad: radius of object 2
	returns: 
		True if collision is true, otherwise returns False
	"""
	if (
		obj1[0] + obj1Rad >= obj2[0] - obj2Rad and
		obj1[0] - obj1Rad <= obj2[0] + obj2Rad and
		obj1[1] + obj1Rad >= obj2[1] - obj2Rad and
		obj1[1] - obj1Rad <= obj2[1] + obj2Rad
	):
		return True
	else:
		return False
	

ghosts = []
for i in range (5):
	randGhostX,randGhostY = randScreenPos(100,80)
	randGhostXSpeed = random.randint(5,7)
	randGhostYSpeed = random.randint(2,4)
	ghosts.append([randGhostX,randGhostY,randGhostXSpeed,randGhostYSpeed])

pellets = []
for i in range(3):
	pelletX,pelletY = randScreenPos(5,5)
	pellets.append([pelletX,pelletY])

joysticks = []
for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)
        print(f"found joystick: {joystick.get_name()}({joystick.get_id()})")

# main program loop -----------------------------
while not done:
	for event in pygame.event.get(): # for user input
		# event loop - all event processing goes here
		if event.type == pygame.QUIT: # if closed by user
			done = True             # break loop
		elif event.type == pygame.JOYBUTTONDOWN:
			if event.button == 0:
				robotColour = (255,0,0)
			elif event.button == 1:
				robotColour = (0,255,0)
			elif event.button == 2:
				robotColour = BLUE
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				done = True
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				LeftArrow = -1
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				RightArrow = 1
			elif event.key == pygame.K_UP or event.key == pygame.K_w:
				UpArrow = -1
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				DownArrow = 1
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				LeftArrow = 0
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				RightArrow = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_w:
				UpArrow = 0
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				DownArrow = 0
	if joysticks:
		currentJoystick = joysticks[0]
		# update joystick direction vars
		joyDirX = currentJoystick.get_axis(0) * speed
		joyDirY = currentJoystick.get_axis(1) * speed
	# clear screen
	screen.fill(WHITE)
	# begin logic code -------------------------------
	# sum inputs and multiply by general speed
	xSpeed = (LeftArrow+RightArrow)*speed
	ySpeed = (UpArrow+DownArrow)*speed
	# update position
	x+=xSpeed+joyDirX
	y+=ySpeed+joyDirY

	# begin drawing code -----------------------------
	drawChar(x,y)
	drawGhosts()
	drawPellets()
	# update screen with drawings
	pygame.display.flip()

	# limit framerate to 60fps
	clock.tick(30)

# close window and quit
pygame.quit()
