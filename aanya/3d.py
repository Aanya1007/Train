from ursina import *
import random
app = Ursina()

cube = Entity(model="character.glb", position = (0,5,5), scale = 5, collider = "box")
track = Entity(model="track.glb",  position = (0,-0.7,30), scale = (1,1,3))
track.rotation_x -= 8
lanes = [-7.5, 0, 7.5]
obstacle = Entity(model = "ATrain.glb", position = (random.choice(lanes), 0,0,50), collider = "box")
obstacle.rotation_y += 90
obstacle.rotation_z+= 10
def input(key):
    if key == 'a' and cube.x != lanes[0]:
        if cube.x == 7.5:
            cube.x = lanes[1]
        elif cube.x ==0:
            cube.x = lanes[0]
    if key == 'd'and cube.x != lanes[2]:
        if cube.x == -7.5:
            cube.x = lanes[1]
        elif cube.x == 0:
            cube.x = lanes[2]

def update():
    obstacle.y -= 0.05
    obstacle.z -= 0.4
    if obstacle.y <= -20 or obstacle.z <= -20:
        obstacle.y = 0
        obstacle.z = 30
        obstacle.x = random.choice(lanes)
    if obstacle.intersects(cube).hit:
        print("dead")
        exit()
    

app.run()
