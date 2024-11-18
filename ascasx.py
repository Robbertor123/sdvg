import pygame as pg
import pygame
import sys, time, os
import tkinter as tk
from tkinter import PhotoImage
from tkinter import Canvas

pygame.init()


def close_window5():
    appw.destroy()


def close_window1():
    app2.destroy()


def close_window7():
    appw2.destroy()


def kon():
    global l
    l = False


def rev():
    global s, w1, w2
    s = 0
    w1 = 0
    w2 = 0
    global d, d1, d2, d3, d4, d5, d6, d7, d8, k
    sc.fill(BLACK)
    wow()
    pg.display.update()
    d = 0
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0
    d7 = 0
    d8 = 0
    k = 0

    def click1():
        global k
        k = 1

    def click2():
        global k
        k = 2

    def close_window():
        app.destroy()

    app = tk.Tk()
    app.title('Game')
    app.geometry("300x250")
    label = tk.Label(text='Кто же первый?', font=("Arial", 14))
    label.pack()
    btn1 = tk.Button(app,
                     text='Кресты',
                     width=8,
                     height=5,
                     command=lambda: [click1(), close_window()])
    btn1.pack(expand=True, ipadx=20, ipady=1, side=tk.LEFT)
    btn2 = tk.Button(app,
                     text="Нули",
                     width=8,
                     height=5,
                     command=lambda: [click2(), close_window()])
    btn2.pack(expand=True, ipadx=20, ipady=1, side=tk.RIGHT)
    app.mainloop()


k = 0


def click1():
    global k
    k = 1


def click2():
    global k
    k = 2


def close_window():
    app.destroy()


app = tk.Tk()
app.title('Game')
app.geometry("300x250")
label = tk.Label(text='Кто же первый?', font=("Arial", 14))
label.pack()
btn1 = tk.Button(app,
                 text='Крест',
                 width=8,
                 height=5,
                 command=lambda: [click1(), close_window()])
btn1.pack(expand=True, ipadx=20, ipady=1, side=tk.LEFT)
btn2 = tk.Button(app,
                 text="Нуль",
                 width=8,
                 height=5,
                 command=lambda: [click2(), close_window()])
btn2.pack(expand=True, ipadx=20, ipady=1, side=tk.RIGHT)
app.mainloop()

print(k)

wh = 800
hh = 500

pygame.display.set_caption('x and 0')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (225, 0, 50)
BLUE = (0, 0, 225)

sc = pg.display.set_mode((wh, hh))
# sc.fill(WHITE)
pg.display.update()

r1 = pygame.Rect(((wh / 2) - 300, (hh / 2) - 190, 600, 350))


def wow():
    pygame.draw.rect(sc, LIGHT_BLUE, r1, 8)
    pygame.draw.rect(sc, LIGHT_BLUE,
                     pygame.Rect(((wh / 2) - 300, (hh / 2) - 90, 600, 130)), 8)
    pygame.draw.rect(sc, LIGHT_BLUE,
                     pygame.Rect(((wh / 2) - 300, (hh / 2) - 190, 200, 350)), 8)
    pygame.draw.rect(sc, LIGHT_BLUE,
                     pygame.Rect(((wh / 2) + 100, (hh / 2) - 190, 200, 350)), 8)
    pg.display.update()


wow()

d = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d8 = 0
s = 0
w1 = 0
w2 = 0

l = True
if k == 0:
    l = False
while l:
    if w1 == 1:
        appw = tk.Tk()
        appw.title('Победа христианства')
        appw.geometry("300x250")
        label = tk.Label(text='Крестики победили!', font=("Arial", 13))
        canvas = Canvas(bg="white", width=100, height=100)
        canvas.pack()
        python_image = PhotoImage(
            file=r"C:\Users\Huawei\Pictures\qqq.png")
        canvas.create_image(5, 5, anchor='nw', image=python_image)
        label.pack()
        btn1 = tk.Button(appw,
                         text='Еще разок',
                         width=8,
                         height=5,
                         command=lambda: [close_window5(), rev()])
        btn1.pack(expand=True, ipadx=20, ipady=1, side=tk.RIGHT)
        btn2 = tk.Button(appw,
                         text="Хватит",
                         width=8,
                         height=5,
                         command=lambda: [kon(), close_window5()])
        btn2.pack(expand=True, ipadx=20, ipady=1, side=tk.LEFT)
        appw.mainloop()

    elif w2 == 1:
        appw2 = tk.Tk()
        appw2.title('Я тебя на ноль УМНОЖУ')
        appw2.geometry("300x250")
        label = tk.Label(text='Ноли Winbet!', font=("Arial", 13))
        label.pack()
        canvas = Canvas(bg="white", width=150, height=100)
        canvas.pack()
        python_image = PhotoImage(
            file=
            r"C:\Users\Huawei\Pictures\yeey.png"
        )
        canvas.create_image(5, 5, anchor='nw', image=python_image)
        label.pack()
        btn1 = tk.Button(appw2,
                         text='Ну последний',
                         width=8,
                         height=5,
                         command=lambda: [close_window7(), rev()])
        btn1.pack(expand=True, ipadx=20, ipady=1, side=tk.RIGHT)
        btn2 = tk.Button(appw2,
                         text="Я устал",
                         width=8,
                         height=5,
                         command=lambda: [kon(), close_window7()])
        btn2.pack(expand=True, ipadx=20, ipady=1, side=tk.LEFT)
        appw2.mainloop()

    if s == 9:
        app2 = tk.Tk()
        app2.title('Ничья')
        app2.geometry("300x250")
        label = tk.Label(text='Ничья? Или все-таки реванш?', font=("Arial", 13))
        label.pack()
        btn1 = tk.Button(app2,
                         text='Реванш',
                         width=8,
                         height=5,
                         command=lambda: [close_window1(), rev()])
        btn1.pack(expand=True, ipadx=20, ipady=1, side=tk.RIGHT)
        btn2 = tk.Button(app2,
                         text="Иди нафиг",
                         width=8,
                         height=5,
                         command=lambda: [kon(), close_window1()])
        btn2.pack(expand=True, ipadx=20, ipady=1, side=tk.LEFT)
        app2.mainloop()

    for i in pygame.event.get():
        if i == pygame.KEYDOWN:
            if i == pygame.K_ESCAPE:
                sys.exit()
        if i.type == pygame.MOUSEMOTION:
            x, y = i.pos
            print(x, y)
            os.system('cls')
            if (x in range(0, 50)) and (y in range(0, 50)):
                print('курсор в регионе')
                time.sleep(0.5)

        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                # pg.draw.circle(sc, RED, i.pos, 20)
                if k == 1:
                    if x >= 108 and x <= 290 and y >= 67 and y <= 156:
                        if d != 2:
                            d = 1
                            pygame.draw.line(sc, WHITE, [290, 156], [108, 67], 3)
                            if d == 1 and d1 == 1 and d2 == 1:
                                pygame.draw.line(sc, RED, [199, 65], [199, 406], 8)
                                w1 = 1
                            if d == 1 and d3 == 1 and d6 == 1:
                                pygame.draw.line(sc, RED, [106, 109], [692, 109], 8)
                                w1 = 1
                            if d == 1 and d4 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [108, 66], [692, 402], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [290, 69], [108, 157], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 108 and x <= 290 and y >= 167 and y <= 281:
                        if d1 != 2:
                            d1 = 1
                            pygame.draw.line(sc, WHITE, [290, 281], [108, 167], 3)
                            if d == 1 and d1 == 1 and d2 == 1:
                                pygame.draw.line(sc, RED, [199, 65], [199, 406], 8)
                                w1 = 1
                            if d1 == 1 and d4 == 1 and d7 == 1:
                                pygame.draw.line(sc, RED, [106, 221], [692, 222], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [290, 169], [108, 280], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 108 and x <= 290 and y >= 289 and y <= 399:
                        if d2 != 2:
                            d2 = 1
                            pygame.draw.line(sc, WHITE, [290, 399], [108, 289], 3)
                            if d == 1 and d1 == 1 and d2 == 1:
                                pygame.draw.line(sc, RED, [199, 65], [199, 406], 8)
                                w1 = 1
                            if d2 == 1 and d5 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [106, 344], [693, 344], 8)
                                w1 = 1
                            if d2 == 1 and d4 == 1 and d6 == 1:
                                pygame.draw.line(sc, RED, [106, 402], [691, 67], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [290, 289], [108, 398], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 300 and x <= 490 and y >= 67 and y <= 160:
                        if d3 != 2:
                            d3 = 1
                            pygame.draw.line(sc, WHITE, [300, 67], [500, 160], 3)
                            if d3 == 1 and d4 == 1 and d5 == 1:
                                pygame.draw.line(sc, RED, [402, 66], [400, 404], 8)
                                w1 = 1
                            if d == 1 and d3 == 1 and d6 == 1:
                                pygame.draw.line(sc, RED, [106, 109], [692, 109], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [300, 156], [500, 69], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 300 and x <= 490 and y >= 167 and y <= 278:
                        if d4 != 2:
                            d4 = 1
                            pygame.draw.line(sc, WHITE, [300, 167], [500, 280], 3)
                            if d3 == 1 and d4 == 1 and d5 == 1:
                                pygame.draw.line(sc, RED, [402, 66], [400, 404], 8)
                                w1 = 1
                            if d1 == 1 and d4 == 1 and d7 == 1:
                                pygame.draw.line(sc, RED, [106, 221], [692, 222], 8)
                                w1 = 1
                            if d == 1 and d4 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [108, 66], [692, 402], 8)
                                w1 = 1
                            if d2 == 1 and d4 == 1 and d6 == 1:
                                pygame.draw.line(sc, RED, [106, 402], [691, 67], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [300, 278], [500, 167], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 300 and x <= 490 and y >= 289 and y <= 400:
                        if d5 != 2:
                            d5 = 1
                            pygame.draw.line(sc, WHITE, [300, 289], [500, 399], 3)
                            if d3 == 1 and d4 == 1 and d5 == 1:
                                pygame.draw.line(sc, RED, [402, 66], [400, 404], 8)
                                w1 = 1
                            if d2 == 1 and d5 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [106, 344], [693, 344], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [300, 400], [500, 290], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 509 and x <= 691 and y >= 67 and y <= 160:
                        if d6 != 2:
                            d6 = 1
                            pygame.draw.line(sc, WHITE, [509, 67], [691, 159], 3)
                            if d6 == 1 and d7 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [602, 66], [601, 402], 8)
                                w1 = 1
                            if d == 1 and d3 == 1 and d6 == 1:
                                pygame.draw.line(sc, RED, [106, 109], [692, 109], 8)
                                w1 = 1
                            if d2 == 1 and d4 == 1 and d6 == 1:
                                pygame.draw.line(sc, RED, [106, 402], [691, 67], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [509, 159], [691, 67], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 509 and x <= 691 and y >= 167 and y <= 280:
                        if d7 != 2:
                            d7 = 1
                            pygame.draw.line(sc, WHITE, [509, 167], [691, 280], 3)
                            if d6 == 1 and d7 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [602, 66], [601, 402], 8)
                                w1 = 1
                            if d1 == 1 and d4 == 1 and d7 == 1:
                                pygame.draw.line(sc, RED, [106, 221], [692, 222], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [509, 280], [691, 169], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                    if x >= 509 and x <= 691 and y > 290 and y <= 400:
                        if d8 != 2:
                            d8 = 1
                            pygame.draw.line(sc, WHITE, [509, 290], [691, 400], 3)
                            if d6 == 1 and d7 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [602, 66], [601, 402], 8)
                                w1 = 1
                            if d2 == 1 and d5 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [106, 344], [693, 344], 8)
                                w1 = 1
                            if d == 1 and d4 == 1 and d8 == 1:
                                pygame.draw.line(sc, RED, [108, 66], [692, 402], 8)
                                w1 = 1
                            pygame.draw.line(sc, WHITE, [509, 400], [691, 290], 3)
                            pg.display.update()
                            k = 2
                            s += 1
                if k == 2:
                    if x >= 108 and x <= 290 and y >= 67 and y <= 156:
                        if d != 1:
                            d = 2
                            pygame.draw.circle(sc, WHITE, (200, 113), 50, 3)
                            if d == 2 and d1 == 2 and d2 == 2:
                                pygame.draw.line(sc, RED, [199, 65], [199, 406], 8)
                                w2 = 1
                            if d == 2 and d3 == 2 and d6 == 2:
                                pygame.draw.line(sc, RED, [106, 109], [692, 109], 8)
                                w2 = 1
                            if d == 2 and d4 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [108, 66], [692, 402], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 108 and x <= 290 and y >= 167 and y <= 281:
                        if d1 != 1:
                            d1 = 2
                            pygame.draw.circle(sc, WHITE, (198, 225), 50, 3)
                            if d == 2 and d1 == 2 and d2 == 2:
                                pygame.draw.line(sc, RED, [199, 65], [199, 406], 8)
                                w2 = 1
                            if d1 == 2 and d4 == 2 and d7 == 2:
                                pygame.draw.line(sc, RED, [106, 221], [692, 222], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 108 and x <= 290 and y >= 289 and y <= 399:
                        if d2 != 1:
                            d2 = 2
                            pygame.draw.circle(sc, WHITE, (198, 345), 50, 3)
                            if d == 2 and d1 == 2 and d2 == 2:
                                pygame.draw.line(sc, RED, [199, 65], [199, 406], 8)
                                w2 = 1
                            if d2 == 2 and d5 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [106, 344], [693, 344], 8)
                                w2 = 1
                            if d2 == 2 and d4 == 2 and d6 == 2:
                                pygame.draw.line(sc, RED, [106, 402], [691, 67], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 300 and x <= 490 and y >= 67 and y <= 160:
                        if d3 != 1:
                            d3 = 2
                            pygame.draw.circle(sc, WHITE, (398, 115), 50, 3)
                            if d3 == 2 and d4 == 2 and d5 == 2:
                                pygame.draw.line(sc, RED, [402, 66], [400, 404], 8)
                                w2 = 1
                            if d == 2 and d3 == 2 and d6 == 2:
                                pygame.draw.line(sc, RED, [106, 109], [692, 109], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 300 and x <= 490 and y >= 167 and y <= 278:
                        if d4 != 1:
                            d4 = 2
                            pygame.draw.circle(sc, WHITE, (398, 224), 50, 3)
                            if d3 == 2 and d4 == 2 and d5 == 2:
                                pygame.draw.line(sc, RED, [402, 66], [400, 404], 8)
                                w2 = 1
                            if d1 == 2 and d4 == 2 and d7 == 2:
                                pygame.draw.line(sc, RED, [106, 221], [692, 222], 8)
                                w2 = 1
                            if d == 2 and d4 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [108, 66], [692, 402], 8)
                                w2 = 1
                            if d2 == 2 and d4 == 2 and d6 == 2:
                                pygame.draw.line(sc, RED, [106, 402], [691, 67], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 300 and x <= 490 and y >= 289 and y <= 400:
                        if d5 != 1:
                            d5 = 2
                            pygame.draw.circle(sc, WHITE, (401, 345), 50, 3)
                            if d3 == 2 and d4 == 2 and d5 == 2:
                                pygame.draw.line(sc, RED, [402, 66], [400, 404], 8)
                                w2 = 1
                            if d2 == 2 and d5 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [106, 344], [693, 344], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 509 and x <= 691 and y >= 67 and y <= 160:
                        if d6 != 1:
                            d6 = 2
                            pygame.draw.circle(sc, WHITE, (599, 113), 50, 3)
                            if d6 == 2 and d7 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [602, 66], [601, 402], 8)
                                w2 = 1
                            if d == 2 and d3 == 2 and d6 == 2:
                                pygame.draw.line(sc, RED, [106, 109], [692, 109], 8)
                                w2 = 1
                            if d2 == 2 and d4 == 2 and d6 == 2:
                                pygame.draw.line(sc, RED, [106, 402], [691, 67], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 509 and x <= 691 and y >= 167 and y <= 280:
                        if d7 != 1:
                            d7 = 2
                            pygame.draw.circle(sc, WHITE, (600, 224), 50, 3)
                            if d6 == 2 and d7 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [602, 66], [601, 402], 8)
                                w2 = 1
                            if d1 == 2 and d4 == 2 and d7 == 2:
                                pygame.draw.line(sc, RED, [106, 221], [692, 222], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1
                    if x >= 509 and x <= 691 and y > 290 and y <= 400:
                        if d8 != 1:
                            d8 = 2
                            pygame.draw.circle(sc, WHITE, (600, 347), 50, 3)
                            if d6 == 2 and d7 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [602, 66], [601, 402], 8)
                                w2 = 1
                            if d2 == 2 and d5 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [106, 344], [693, 344], 8)
                                w2 = 1
                            if d == 2 and d4 == 2 and d8 == 2:
                                pygame.draw.line(sc, RED, [108, 66], [692, 402], 8)
                                w2 = 1
                            pg.display.update()
                            k = 1
                            s += 1

            elif i.button == 3:
                sc.fill(BLACK)
                wow()
                d = 0
                d1 = 0
                d2 = 0
                d3 = 0
                d4 = 0
                d5 = 0
                d6 = 0
                d7 = 0
                d8 = 0
                k = 0
                app = tk.Tk()
                app.title('Game')
                app.geometry("300x250")
                label = tk.Label(text='Кто же первый?', font=("Arial", 14))
                label.pack()
                btn1 = tk.Button(app,
                                 text='Кресты',
                                 width=8,
                                 height=5,
                                 command=lambda: [click1(), close_window()])
                btn1.pack(expand=True, ipadx=20, ipady=1, side=tk.LEFT)
                btn2 = tk.Button(app,
                                 text="Нули",
                                 width=8,
                                 height=5,
                                 command=lambda: [click2(), close_window()])
                btn2.pack(expand=True, ipadx=20, ipady=1, side=tk.RIGHT)
                app.mainloop()
                pg.display.update()

    pg.time.delay(20)
