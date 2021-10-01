import math
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
scale = 0.45 #scale of window with the picture
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

def background(scr, color1, color2, color3, color4):
    pygame.draw.rect(scr, color1, [0, 0, 2500 * scale, 349 * scale])
    pygame.draw.rect(scr, color2, [0, 349 * scale, 2500 * scale, 492 * scale])
    pygame.draw.rect(scr, color3, [0, 711 * scale, 2500 * scale, 354 * scale])
    pygame.draw.rect(scr, color4, [0, 1065 * scale, 2500 * scale, 834 * scale])
background(screen, yellow_sky_up, pink_sky, yellow_sky_middle, pink_ground)

pygame.draw.circle(screen, sun_color, (1192 * scale, 345 * scale), (144 * scale))

# ораньжевые горы

pygame.draw.polygon(screen, orange,
                    [[0, 775 * scale], [30 * scale, 674 * scale], [514 * scale, 327 * scale], [611 * scale, 357 * scale],
                     [644 * scale, 411 * scale], [653 * scale, 419 * scale], [958 * scale, 625 * scale],
                     [1123 * scale, 603 * scale], [1212 * scale, 647 * scale], [1331 * scale, 531 * scale], [1450 * scale, 552 * scale],
                     [1500 * scale, 500 * scale], [1770 * scale, 265 * scale], [1868 * scale, 309 * scale], [1980 * scale, 415 * scale],
                     [2071 * scale, 390 * scale], [2339 * scale, 473 * scale], [2325 * scale, 471 * scale],
                     [2500 * scale, 520 * scale]
                     ])

pygame.draw.arc(screen, orange, [1750 * scale, 245 * scale, 100 * scale, 200 * scale], 0, math.pi, int(200 * scale))
# тройное повторение с небольшим изменением координат потому что без него какая-то фигня с заливкой
pygame.draw.arc(screen, orange, [
    1750 * scale + 1, 245 * scale, 100 * scale, 200 * scale], 0, math.pi, int(200 * scale))
pygame.draw.arc(screen, orange, [
    1750 * scale - 1, 245 * scale, 100 * scale, 200 * scale], 0, math.pi, int(200 * scale))

# красный лес
pygame.draw.polygon(screen, red,
                    [[0, 1125 * scale], [0, 830 * scale], [71 * scale, 858 * scale], [250 * scale, 825 * scale],
                     [436 * scale, 1068 * scale], [546 * scale, 885 * scale], [723 * scale, 979 * scale],
                     [807 * scale, 750 * scale], [1000 * scale, 800 * scale], [1200 * scale, 930 * scale], [1430 * scale, 876 * scale],
                     [1750 * scale, 687 * scale], [2044 * scale, 845 * scale], [2153 * scale, 755 * scale], [2253 * scale, 820 * scale],
                     [2300 * scale, 738 * scale], [2407 * scale, 743 * scale], [2500 * scale, 590 * scale],
                     [2500 * scale, 1071 * scale]
                     ])

pygame.draw.arc(screen, red, [1450 * scale, 687 * scale, 600 * scale, 550 * scale], math.pi / 2, math.pi * 0.9, int(200 * scale))
# тройное повторение с небольшим изменением координат потому что без него какая-то фигня с заливкой
pygame.draw.arc(screen, red, [1450 * scale + 1, 687 * scale, 600 * scale, 550 * scale], math.pi / 2, math.pi * 0.9, int(200 * scale))
pygame.draw.arc(screen, red, [1450 * scale - 1, 687 * scale, 600 * scale, 550 * scale], math.pi / 2, math.pi * 0.9, int(200 * scale))

pygame.draw.arc(screen, red, [60 * scale, 660 * scale, 400 * scale, (900) * scale], 0, math.pi * 5 / 6, int(383 * scale))
pygame.draw.arc(screen, red, [60 * scale + 1, 660 * scale, 400 * scale, (900) * scale], 0, math.pi * 5 / 6, int(383 * scale))
pygame.draw.arc(screen, red, [60 * scale - 1, 660 * scale, 400 * scale, (900) * scale], 0, math.pi * 5 / 6, int(383 * scale))

# темная земля на переднем плане
pygame.draw.polygon(screen, dark_ground,
                    [[0, 1666 * scale], [0, 857 * scale], [302 * scale, 937 * scale], [531 * scale, 1232 * scale],
                     [813 * scale, 1580 * scale], [1171 * scale, 1637 * scale], [1579 * scale, 1408 * scale],
                     [1689 * scale, 1463 * scale], [2089 * scale, 1400 * scale], [2500 * scale, 1000 * scale],
                     [2500 * scale, 1666 * scale]
                     ])


# и finally птички

# 960 600


def print_bird(Xc, Yc, size):
    dY = 50 * size
    dX = 65 * size
    r = 15 * size
    pygame.draw.circle(screen, dark_birds, ((Xc - dX) * scale, (Yc - dY) * scale), (r * scale))
    pygame.draw.polygon(screen, dark_birds,
                        [[(Xc - dX + r / 2 ** 0.5) * scale - 1, (Yc - dY - r / 2 ** 0.5) * scale],
                         [(Xc - dX - r / 2 ** 0.5) * scale + 3, (Yc - dY + r / 2 ** 0.5) * scale],
                         [Xc * scale, Yc * scale],
                         [(Xc + dX) * scale, (Yc - dY) * scale], [(Xc + dX / 2) * scale, (Yc - dY * 2 / 2) * scale],
                         [Xc * scale, (Yc - dY / 2) * scale]
                         ])
birds = [(960, 600, 1), (1185, 621, 1), (1185, 709, 1.05), (991, 778, 1), (1944, 1335, 1.5), (1985, 1206, 0.6), (1700, 1252, 0.8), (1568, 1127, 1.0)]
for i in birds:
    print_bird(i[0], i[1], i[2])

###

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
