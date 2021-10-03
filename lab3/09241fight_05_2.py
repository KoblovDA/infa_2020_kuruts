import math
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
scale = 0.45  # scale of window with the picture
screen = pygame.display.set_mode((int(2500 * scale), int(1666 * scale)))

yellow_sky_up = (254, 213, 162)
yellow_sky_middle = (254, 213, 148)
pink_sky = (254, 213, 196)
sun_color = (252, 238, 33)
orange = (252, 152, 49)
red = (172, 67, 52)
pink_ground = (179, 134, 148)
dark_ground = (48, 16, 38)
dark_birds = (66, 33, 11)


def background(scr, scl, color1, color2, color3, color4):
    rect(scr, color1, [0, 0, 2500 * scl, 349 * scl])
    rect(scr, color2, [0, 349 * scl, 2500 * scl, 492 * scl])
    rect(scr, color3, [0, 711 * scl, 2500 * scl, 354 * scl])
    rect(scr, color4, [0, 1065 * scl, 2500 * scl, 834 * scl])


def print_bird(scr, scl, height, width, x, y, size, color):
    d_y = height * size
    d_x = width * size
    r = 15 * size
    circle(scr, color, ((x - d_x) * scl, (y - d_y) * scl), (r * scl))
    polygon(scr, color,
            [[(x - d_x + r / 2 ** 0.5) * scl - 1, (y - d_y - r / 2 ** 0.5) * scl],
             [(x - d_x - r / 2 ** 0.5) * scl + 3, (y - d_y + r / 2 ** 0.5) * scl],
             [x * scl, y * scl],
             [(x + d_x) * scl, (y - d_y) * scl], [(x + d_x / 2) * scl, (y - d_y * 2 / 2) * scl],
             [x * scl, (y - d_y / 2) * scl]
             ])


def sun(scr, scl, color, x, y, size):
    # The size is the radius of the sun, but maybe something else will be added
    circle(scr, color, (x * scl, y * scl), (size * scl))


def smart_polygon(scr, scl, color, points):
    new_points = []
    for i in points:
        new_points.append((i[0] * scale, i[1] * scale))
    polygon(scr, color, new_points)


background(screen, scale, yellow_sky_up, pink_sky, yellow_sky_middle, pink_ground)
sun(screen, scale, sun_color, 1192, 345, 144)
mountains = [(0, 775), (30, 674), (514, 327), (611, 357), (644, 411),
             (653, 419), (958, 625), (1123, 603), (1212, 647), (1331, 531),
             (1450, 552), (1500, 500), (1770, 265), (1868, 309),
             (1980, 415), (2071, 390), (2339, 473), (2325, 471),
             (2500, 520)]
smart_polygon(screen, scale, orange, mountains)  # mountains

arc(screen, orange, [1750 * scale, 245 * scale, 100 * scale, 200 * scale], 0, math.pi, int(200 * scale))
# тройное повторение с небольшим изменением координат потому что без него какая-то фигня с заливкой
arc(screen, orange, [1750 * scale + 1, 245 * scale, 100 * scale, 200 * scale], 0, math.pi, int(200 * scale))
arc(screen, orange, [
    1750 * scale - 1, 245 * scale, 100 * scale, 200 * scale], 0, math.pi, int(200 * scale))

red_forest = [(0, 1125), (0, 830), (71, 858), (250, 825),
              (436, 1068), (546, 885), (723, 979),
              (807, 750), (1000, 800), (1200, 930),
              (1430, 876), (1750, 687), (2044, 845), (2153, 755),
              (2253, 820), (2300, 738), (2407, 743), (2500, 590),
              (2500, 1071)]
smart_polygon(screen, scale, red, red_forest)  # red forest

arc(screen, red, [1450 * scale, 687 * scale, 600 * scale, 550 * scale], math.pi / 2, math.pi * 0.9,
    int(200 * scale))
# тройное повторение с небольшим изменением координат потому что без него какая-то фигня с заливкой
arc(screen, red, [1450 * scale + 1, 687 * scale, 600 * scale, 550 * scale], math.pi / 2, math.pi * 0.9,
    int(200 * scale))
arc(screen, red, [1450 * scale - 1, 687 * scale, 600 * scale, 550 * scale], math.pi / 2, math.pi * 0.9,
    int(200 * scale))

arc(screen, red, [60 * scale, 660 * scale, 400 * scale, 900 * scale], 0, math.pi * 5 / 6,
    int(383 * scale))
arc(screen, red, [60 * scale + 1, 660 * scale, 400 * scale, 900 * scale], 0, math.pi * 5 / 6,
    int(383 * scale))
arc(screen, red, [60 * scale - 1, 660 * scale, 400 * scale, 900 * scale], 0, math.pi * 5 / 6,
    int(383 * scale))

# темная земля на переднем плане
polygon(screen, dark_ground,
        [[0, 1666 * scale], [0, 857 * scale], [302 * scale, 937 * scale], [531 * scale, 1232 * scale],
         [813 * scale, 1580 * scale], [1171 * scale, 1637 * scale], [1579 * scale, 1408 * scale],
         [1689 * scale, 1463 * scale], [2089 * scale, 1400 * scale], [2500 * scale, 1000 * scale],
         [2500 * scale, 1666 * scale]
         ])
birds = [(960, 600, 1), (1185, 621, 1), (1185, 709, 1.05), (991, 778, 1), (1944, 1335, 1.5), (1985, 1206, 0.6),
         (1700, 1252, 0.8), (1568, 1127, 1.0)]
for i in birds:
    print_bird(screen, scale, 50, 65, i[0], i[1], i[2], dark_birds)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
