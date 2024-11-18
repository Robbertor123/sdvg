import pygame as pg
import keyboard
import sys, time, os
import random

pg.init()

wh = 800
hh = 500
pg.display.set_caption('xz')
sc = pg.display.set_mode((wh, hh))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sc.fill(BLACK)
clock = pg.time.Clock()

pg.display.update()

x = [80, 0]
y = [80, 95]
x1 = [720, 0]
y1 = [720, 95]
a = 400
b = 250
dx, dy = 1.3, 2.3
p = random.randint(1, 2)
while 1:
    print(a, b, p)
    pg.display.update()
    if p == 1:
        dx = dx * -1
        dy = dy * -1
        if a < 729:
            sc.fill(BLACK)
            pg.draw.line(sc, WHITE, x1, y1, 10)
            pg.draw.line(sc, WHITE, x, y, 10)
            if a < 716 or b < x1[1] or b > y1[1]:
                a += 3  ## a+=dx
                b += dy
                pg.draw.rect(sc, WHITE, (a, b, 9, 9))
                pg.display.update()
            else:
                p = 2
        else:
            sc.fill(BLACK)
            pg.draw.line(sc, WHITE, x1, y1, 10)
            pg.draw.line(sc, WHITE, x, y, 10)
            a += 5  # здесь может быть счетчик
            pg.draw.rect(sc, WHITE, (a, b, 9, 9))
            pg.display.update()

    if p == 2:
        if a > 75:
            sc.fill(BLACK)
            pg.draw.line(sc, WHITE, x1, y1, 10)
            pg.draw.line(sc, WHITE, x, y, 10)
            if a > 80 or b < x[1] or b > y[1]:
                a -= 3
                pg.draw.rect(sc, WHITE, (a, b, 9, 9))
                pg.display.update()
            else:
                p = 1
        else:
            sc.fill(BLACK)
            pg.draw.line(sc, WHITE, x1, y1, 10)
            pg.draw.line(sc, WHITE, x, y, 10)
            a -= 5  # счетчик
            pg.draw.rect(sc, WHITE, (a, b, 9, 9))
            pg.display.update()

    if keyboard.is_pressed('W'):
        sc.fill(BLACK)
        pg.draw.line(sc, WHITE, x1, y1, 10)
        if x[1] > 0:
            x[1] -= 5
            y[1] -= 5
        pg.draw.line(sc, WHITE, x, y, 10)
        pg.draw.rect(sc, WHITE, (a, b, 9, 9))
        pg.display.update()
    if keyboard.is_pressed('S'):
        sc.fill(BLACK)
        pg.draw.line(sc, WHITE, x1, y1, 10)
        if y[1] < 500:
            x[1] += 5
            y[1] += 5
        pg.draw.line(sc, WHITE, x, y, 10)
        pg.draw.rect(sc, WHITE, (a, b, 9, 9))
        pg.display.update()
    if keyboard.is_pressed('L'):
        sc.fill(BLACK)
        pg.draw.line(sc, WHITE, x, y, 10)
        if y1[1] < 500:
            x1[1] += 5
            y1[1] += 5
        pg.draw.line(sc, WHITE, x1, y1, 10)
        pg.draw.rect(sc, WHITE, (a, b, 9, 9))
        pg.display.update()
    if keyboard.is_pressed('P'):
        sc.fill(BLACK)
        pg.draw.line(sc, WHITE, x, y, 10)
        if x1[1] > 0:
            x1[1] -= 5
            y1[1] -= 5
        pg.draw.line(sc, WHITE, x1, y1, 10)
        pg.draw.rect(sc, WHITE, (a, b, 9, 9))
        pg.display.update()

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    clock.tick(60)
