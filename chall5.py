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

speed = 5
# loop until closed by user
done = False


# begin function definitions --------------------
joysticks = []
for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)
        print(f"found joystick: {joystick.get_name()}({joystick.get_id()})")

def drawChar(x,y):
	pygame.draw.circle(screen, RED, (x,y), 40, 0)

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
	x+=xSpeed
	y+=ySpeed

	# begin drawing code -----------------------------


	# update screen with drawings
	pygame.display.flip()

	# limit framerate to 60fps
	clock.tick(60)

# close window and quit
pygame.quit()
