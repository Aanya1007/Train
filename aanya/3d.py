from ursina import *
import random
app = Ursina()

cube = Entity(model="character.glb", position = (0,5,5), scale = 5)
track = Entity(model="track.glb",  position = (0,-0.7,30), scale = (1,1,3))
track.rotation_x -= 8
lanes = [-5, 0, 5]
obstacle = Entity(model = "untitled.glb", position = (random.choice(lanes), 0,0,30))
obstacle.rotation_y += 90
obstacle.rotation_z+= 10
def input(key):
    if key == 'a' and cube.x != lanes[0]:
        if cube.x ==5:
            cube.x = lanes[1]
        elif cube.x ==0:
            cube.x = lanes[0]
    if key == 'd'and cube.x != lanes[2]:
        if cube.x == -5:
            cube.x = lanes[1]
        elif cube.x == 0:
            cube.x = lanes[2]

def update():
    obstacle.y -= 0.1
    obstacle.z -= 0.8
    if obstacle.y <= -20 or obstacle.z <= -20:
        obstacle.y = 0
        obstacle.z = 30
        obstacle.x = random.choice(lanes)

app.run()