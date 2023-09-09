from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
window.color = color.light_gray
camera.orthographic = True
camera.fov = 20

ground = Entity(
    model="cube",
    color=color.olive.tint(-.4),
    z=-.1,
    y=-1,
    origin_y=.5,
    scale=(1000, 100, 10),
    collider='box',
    ignore=True,
)
random.seed(4)

for i in range(10):
    Entity(
        model="cube", color=color.dark_gray, collider='box', ignore=True,
        position=(random.randint(-20, 20), random.randint(0, 10)),
        scale=(random.randint(1, 20), random.randint(2, 5), 10)
    )

player = PlatformerController2d(
    position=(1, 0),  # Set the initial position
    collision=True,
    max_jumps=2,  # Maximum number of jumps
)
camera.add_script(SmoothFollow(target=player, offset=[0, 0, -30], speed=4))

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')

app.run()
