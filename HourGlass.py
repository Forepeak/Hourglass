import pygame
from random import randrange
import pygame as pg
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 800, 800
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)
image = pygame.image.load('cosm.png')
#image = pygame.transform.scale(image, (800, 800))



space = pymunk.Space()
space.gravity = 0, 1000


##############
thickness = 5
ball_mass, ball_radius = 5, 5
##############

p1, p2, p3, p4, p5, p6 = (250,100), (550,100),  (412+20,400),  (550,700),  (250,700),  (387-20,400),
l1, l2, l3, l4, l5, l6 = (p1, p2), (p2, p3), (p3, p4), (p4, p5), (p5, p6), (p6, p1)
list = l1, l2, l3, l4, l5, l6



####################################################################################
def create_lines (ps):
    segment_glass = pymunk.Segment(space.static_body, ps[0], ps[1], thickness)
    segment_glass.color = [randrange(256) for i in range(4)]
    segment_glass.elasticity = 0.5
    segment_glass.friction = 1
    space.add(segment_glass)


for x in range (250, 550, ball_radius*4):
    for y in range (100, 700, ball_radius*4):
        ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
        ball_body = pymunk.Body(ball_mass, ball_moment)
        ball_body.position = x,y
        ball_shape = pymunk.Circle(ball_body, ball_radius)
        ball_shape.elasticity = 0.5
        ball_shape.friction = 0.5
        ball_shape.color = [randrange(256) for i in range(4)]
        space.add(ball_body, ball_shape)

def any_gravity ():
    space.gravity = randrange(-1000, 1000, 100), randrange(-1000, 1000, 100)



# box_mass, box_size = 1, (10, 10)
# for x in range(120, WIDTH - 120, box_size[0]):
#     for y in range(HEIGHT//2, HEIGHT-62, box_size[1]):
#         box_moment = pymunk.moment_for_box(box_mass, box_size)
#         box_body = pymunk.Body(box_mass, box_moment)
#         box_body.position = x, y
#         box_shape = pymunk.Poly.create_box(box_body, box_size)
#         box_shape.elasticity = 0.9
#         box_shape.friction = 1.0
#         box_shape.color = [randrange(256) for i in range(4)]
#         space.add(box_body, box_shape)

#####################################################################################
for i in list:
    create_lines (i)


def colors():
    for i in list:
        create_lines (i)


while True:
    surface.fill(pg.Color('black'))
    surface.blit(image, (0, 0))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            any_gravity()
            colors()

    space.step(1 / FPS)
    space.debug_draw(draw_options)


    pg.display.flip()
    clock.tick(FPS)
