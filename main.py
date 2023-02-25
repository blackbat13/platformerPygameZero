import pgzrun
import pymunk

WIDTH = 800
HEIGHT = 800

player = Actor("bunny")
player.x = WIDTH / 2
player.y = HEIGHT / 2
player.moving = False

platform = Actor("platform")
platform.x = WIDTH / 2
platform.y = 3 * HEIGHT / 4

space = pymunk.Space()
space.gravity = (0.0, 900.0)

platform.body = pymunk.Body(0, 0, pymunk.body.Body.KINEMATIC)
platform.shape = pymunk.Poly.create_box(platform.body, (380, 94))

space.add(platform.body, platform.shape)

player.body = pymunk.Body(10, pymunk.moment_for_box(10, (120, 201)))
player.shape = pymunk.Poly.create_box(player.body, (120, 201))

space.add(player.body, player.shape)

player.body.position = player.pos
platform.body.position = platform.pos


def draw():
    screen.fill("white")
    player.draw()
    platform.draw()


def update(dt):
    space.step(dt)
    player.pos = player.body.position
    platform.pos = platform.body.position
    platform.body.velocity = (0, 10)

    velx, vely = player.body.velocity
    if keyboard.left:
        player.body.velocity = (-500, vely)
    elif keyboard.right:
        player.body.velocity = (500, vely)
    else:
        player.body.velocity = (0, vely)


def on_key_down(key):
    if key == keys.SPACE:
        player.body.apply_impulse_at_local_point((0, -5000))


pgzrun.go()
