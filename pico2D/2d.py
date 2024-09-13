from pico2d import *

open_canvas()

#os.chdir('..')
os.chdir('images')
grass = load_image("grass.png")
character = load_image('character.png')

x = 0
while x < 900:
	clear_canvas_now()
	grass.draw_now(400, 30)
	character.draw_now(x, 90)
	delay(0.01)
	x += 2

close_canvas()