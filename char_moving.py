# Drill 06  2017180022 오지원 
from pico2d import *
import math
os.chdir('d:/2DGP/Lecture04_2D_Rendering')
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def rendering(X,Y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(X,Y)

x=400
y= 90

while True:
    theta = 0
    while x < 780:
        rendering(x,y)
        x += 4
        delay(0.01)
    while y < 550:
        rendering(x,y)
        y += 4
        delay(0.01)
    while x > 20:
        rendering(x,y)
        x -= 4
        delay(0.01)
    while y > 90:
        rendering(x,y)
        y -= 4
        delay(0.01)
    while x < 400:
        rendering(x,y)
        x += 4
        delay(0.01)
    while theta < 360:
        rendering(x + (250*math.sin((theta-180) / 360 * 2 * math.pi)),y+280 + 250*(math.cos((theta-180) / 360 * 2 * math.pi)))
        theta += 3
        delay(0.01)

close_canvas()
