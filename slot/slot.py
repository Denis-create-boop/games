# слот казино ///
import pygame as pg
from random import randint as rd

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

W, H = 1200, 700

screen = pg.display.set_mode((W, H))
COLOR = (153, 255, 255)
COLOR_START = (102, 51, 102)
COLOR_TEXT = (204, 204, 204)
fps = 60
clock = pg.time.Clock()
bg = pg.image.load('img1/bg.jpg').convert_alpha()
bg1 = pg.image.load('img1/bg1.jpg').convert_alpha()
bonus_bg = pg.image.load('img1/bonus_bg.jpg').convert_alpha()
bonus_bg1 = pg.image.load('img1/bonus_bg1.jpg').convert_alpha()

W1, H1 = 820, 450
surf = pg.Surface((W1, H1))
surf.blit(bg1, (0, 0))
surf_rect = surf.get_rect()
coin = 1000
st = 100

img_circle = pg.image.load('img1/refresh.png').convert_alpha()
img = {1: pg.image.load('img1/10.png'), 2: pg.image.load('img1/J.jpg'), 3: pg.image.load('img1/Q.png'), 4: pg.image.load('img1/K.png'), 
       5: pg.image.load('img1/A.png'), 6: pg.image.load('img1/lion.png'), 7: pg.image.load('img1/bear.png'), 8: pg.image.load('img1/rabbit.png'), 
       9: pg.image.load('img1/V.png'), 10: pg.image.load('img1/scater.png')}

money = {'10': {3: 0.5, 4: 2, 5: 4},
         'J': {3: 0.5, 4: 2, 5: 4},
         'Q': {3: 1, 4: 2.5, 5: 5},
         'K': {3: 1, 4: 2.5, 5: 5},
         'A': {3: 1.5, 4: 3, 5: 7},
         'lion': {2: 1, 3: 3, 4: 5, 5: 10},
         'bear': {2: 1, 3: 3, 4: 5, 5: 10},
         'rabbit': {2: 1.5, 3: 4, 4: 7, 5: 15},
         'V': {5: 20}}

def scater(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15):
    total_scater = 0
    list = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15]
    for i in list:
        if i == 10:
            total_scater += 1
    return total_scater


class Check:

    def __init__(self, num_1, num_2, num_3, num_4, num_5):
        self.num1 = num_1
        self.num2 = num_2
        self.num3 = num_3
        self.num4 = num_4
        self.num5 = num_5

    def check(self):
        self.answer = 0
        if 9 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
            if self.num1 == self.num2 == self.num3 == self.num4 == self.num5:
                self.answer = 5

            elif self.num1 == self.num2 == self.num3 == self.num4 != self.num5:
                self.answer = 4
            
            elif self.num1 == self.num2 == self.num3 != self.num4:
                self.answer = 3
            
            elif self.num1 not in [1, 2, 3, 4, 5, 10] and self.num2 not in [1, 2, 3, 4, 5, 10]:
                if self.num1 == self.num2 != self.num3:
                    self.answer = 2
        
        else:
            if 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 8 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 7 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 6 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 5 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 4 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 3 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 2 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5
            elif 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 8 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 7 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 6 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 5 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 4 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 3 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 1 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5
            elif 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 8 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 7 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 6 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 5 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 4 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 1 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 2 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5
            elif 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 8 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 7 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 6 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 5 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 1 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 3 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 2 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5
            elif 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 8 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 7 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 6 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 1 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 4 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 3 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 2 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5
            elif 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 8 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 7 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 1 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 5 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 4 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 3 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 2 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5
            elif 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 8 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 1 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 6 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 5 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 4 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 3 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 2 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5
            elif 10 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 1 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 7 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 6 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 5 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 4 not in [self.num1, self.num2, self.num3, self.num4, self.num5]  and 3 not in [self.num1, self.num2, self.num3, self.num4, self.num5] and 2 not in [self.num1, self.num2, self.num3, self.num4, self.num5]:
                self.answer = 5

            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 8 not in [self.num1, self.num2, self.num3, self.num4] and 7 not in [self.num1, self.num2, self.num3, self.num4] and 6 not in [self.num1, self.num2, self.num3, self.num4] and 5 not in [self.num1, self.num2, self.num3, self.num4] and 4 not in [self.num1, self.num2, self.num3, self.num4]  and 3 not in [self.num1, self.num2, self.num3, self.num4] and 2 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [1, 9]:
                self.answer = 4
            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 8 not in [self.num1, self.num2, self.num3, self.num4] and 7 not in [self.num1, self.num2, self.num3, self.num4] and 6 not in [self.num1, self.num2, self.num3, self.num4] and 5 not in [self.num1, self.num2, self.num3, self.num4] and 4 not in [self.num1, self.num2, self.num3, self.num4]  and 3 not in [self.num1, self.num2, self.num3, self.num4] and 1 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [2, 9]:
                self.answer = 4
            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 8 not in [self.num1, self.num2, self.num3, self.num4] and 7 not in [self.num1, self.num2, self.num3, self.num4] and 6 not in [self.num1, self.num2, self.num3, self.num4] and 5 not in [self.num1, self.num2, self.num3, self.num4] and 4 not in [self.num1, self.num2, self.num3, self.num4]  and 1 not in [self.num1, self.num2, self.num3, self.num4] and 2 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [3, 9]:
                self.answer = 4
            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 8 not in [self.num1, self.num2, self.num3, self.num4] and 7 not in [self.num1, self.num2, self.num3, self.num4] and 6 not in [self.num1, self.num2, self.num3, self.num4] and 5 not in [self.num1, self.num2, self.num3, self.num4] and 1 not in [self.num1, self.num2, self.num3, self.num4]  and 3 not in [self.num1, self.num2, self.num3, self.num4] and 2 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [4, 9]:
                self.answer = 4
            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 8 not in [self.num1, self.num2, self.num3, self.num4] and 7 not in [self.num1, self.num2, self.num3, self.num4] and 6 not in [self.num1, self.num2, self.num3, self.num4] and 1 not in [self.num1, self.num2, self.num3, self.num4] and 4 not in [self.num1, self.num2, self.num3, self.num4]  and 3 not in [self.num1, self.num2, self.num3, self.num4] and 2 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [5, 9]:
                self.answer = 4
            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 8 not in [self.num1, self.num2, self.num3, self.num4] and 7 not in [self.num1, self.num2, self.num3, self.num4] and 1 not in [self.num1, self.num2, self.num3, self.num4] and 5 not in [self.num1, self.num2, self.num3, self.num4] and 4 not in [self.num1, self.num2, self.num3, self.num4]  and 3 not in [self.num1, self.num2, self.num3, self.num4] and 2 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [6, 9]:
                self.answer = 4
            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 8 not in [self.num1, self.num2, self.num3, self.num4] and 1 not in [self.num1, self.num2, self.num3, self.num4] and 6 not in [self.num1, self.num2, self.num3, self.num4] and 5 not in [self.num1, self.num2, self.num3, self.num4] and 4 not in [self.num1, self.num2, self.num3, self.num4]  and 3 not in [self.num1, self.num2, self.num3, self.num4] and 2 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [7, 9]:
                self.answer = 4
            elif 10 not in [self.num1, self.num2, self.num3, self.num4] and 1 not in [self.num1, self.num2, self.num3, self.num4] and 7 not in [self.num1, self.num2, self.num3, self.num4] and 6 not in [self.num1, self.num2, self.num3, self.num4] and 5 not in [self.num1, self.num2, self.num3, self.num4] and 4 not in [self.num1, self.num2, self.num3, self.num4]  and 3 not in [self.num1, self.num2, self.num3, self.num4] and 2 not in [self.num1, self.num2, self.num3, self.num4] and self.num5 not in [8, 9]:
                self.answer = 4
            
            elif 10 not in [self.num1, self.num2, self.num3] and 8 not in [self.num1, self.num2, self.num3] and 7 not in [self.num1, self.num2, self.num3] and 6 not in [self.num1, self.num2, self.num3] and 5 not in [self.num1, self.num2, self.num3] and 4 not in [self.num1, self.num2, self.num3]  and 3 not in [self.num1, self.num2, self.num3] and 2 not in [self.num1, self.num2, self.num3] and self.num4 not in [1, 9]:
                self.answer = 3
            elif 10 not in [self.num1, self.num2, self.num3] and 8 not in [self.num1, self.num2, self.num3] and 7 not in [self.num1, self.num2, self.num3] and 6 not in [self.num1, self.num2, self.num3] and 5 not in [self.num1, self.num2, self.num3] and 4 not in [self.num1, self.num2, self.num3]  and 3 not in [self.num1, self.num2, self.num3] and 1 not in [self.num1, self.num2, self.num3] and self.num4 not in [2, 9]:
                self.answer = 3
            elif 10 not in [self.num1, self.num2, self.num3] and 8 not in [self.num1, self.num2, self.num3] and 7 not in [self.num1, self.num2, self.num3] and 6 not in [self.num1, self.num2, self.num3] and 5 not in [self.num1, self.num2, self.num3] and 4 not in [self.num1, self.num2, self.num3]  and 1 not in [self.num1, self.num2, self.num3] and 2 not in [self.num1, self.num2, self.num3] and self.num4 not in [3, 9]:
                self.answer = 3
            elif 10 not in [self.num1, self.num2, self.num3] and 8 not in [self.num1, self.num2, self.num3] and 7 not in [self.num1, self.num2, self.num3] and 6 not in [self.num1, self.num2, self.num3] and 5 not in [self.num1, self.num2, self.num3] and 1 not in [self.num1, self.num2, self.num3]  and 3 not in [self.num1, self.num2, self.num3] and 2 not in [self.num1, self.num2, self.num3] and self.num4 not in [4, 9]:
                self.answer = 3
            elif 10 not in [self.num1, self.num2, self.num3] and 8 not in [self.num1, self.num2, self.num3] and 7 not in [self.num1, self.num2, self.num3] and 6 not in [self.num1, self.num2, self.num3] and 1 not in [self.num1, self.num2, self.num3] and 4 not in [self.num1, self.num2, self.num3]  and 3 not in [self.num1, self.num2, self.num3] and 2 not in [self.num1, self.num2, self.num3] and self.num4 not in [5, 9]:
                self.answer = 3
            elif 10 not in [self.num1, self.num2, self.num3] and 8 not in [self.num1, self.num2, self.num3] and 7 not in [self.num1, self.num2, self.num3] and 1 not in [self.num1, self.num2, self.num3] and 5 not in [self.num1, self.num2, self.num3] and 4 not in [self.num1, self.num2, self.num3]  and 3 not in [self.num1, self.num2, self.num3] and 2 not in [self.num1, self.num2, self.num3] and self.num4 not in [6, 9]:
                self.answer = 3
            elif 10 not in [self.num1, self.num2, self.num3] and 8 not in [self.num1, self.num2, self.num3] and 1 not in [self.num1, self.num2, self.num3] and 6 not in [self.num1, self.num2, self.num3] and 5 not in [self.num1, self.num2, self.num3] and 4 not in [self.num1, self.num2, self.num3]  and 3 not in [self.num1, self.num2, self.num3] and 2 not in [self.num1, self.num2, self.num3] and self.num4 not in [7, 9]:
                self.answer = 3
            elif 10 not in [self.num1, self.num2, self.num3] and 1 not in [self.num1, self.num2, self.num3] and 7 not in [self.num1, self.num2, self.num3] and 6 not in [self.num1, self.num2, self.num3] and 5 not in [self.num1, self.num2, self.num3] and 4 not in [self.num1, self.num2, self.num3]  and 3 not in [self.num1, self.num2, self.num3] and 2 not in [self.num1, self.num2, self.num3] and self.num4 not in [8, 9]:
                self.answer = 3

            elif 10 not in [self.num1, self.num2] and 8 not in [self.num1, self.num2] and 7 not in [self.num1, self.num2] and 6 not in [self.num1, self.num2] and 5 not in [self.num1, self.num2] and 4 not in [self.num1, self.num2]  and 3 not in [self.num1, self.num2] and 2 not in [self.num1, self.num2] and self.num3 not in [1, 9]:
                self.answer = 2
            elif 10 not in [self.num1, self.num2] and 8 not in [self.num1, self.num2] and 7 not in [self.num1, self.num2] and 6 not in [self.num1, self.num2] and 5 not in [self.num1, self.num2] and 4 not in [self.num1, self.num2]  and 3 not in [self.num1, self.num2] and 1 not in [self.num1, self.num2] and self.num3 not in [2, 9]:
                self.answer = 2
            elif 10 not in [self.num1, self.num2] and 8 not in [self.num1, self.num2] and 7 not in [self.num1, self.num2] and 6 not in [self.num1, self.num2] and 5 not in [self.num1, self.num2] and 4 not in [self.num1, self.num2]  and 1 not in [self.num1, self.num2] and 2 not in [self.num1, self.num2] and self.num3 not in [3, 9]:
                self.answer = 2
            elif 10 not in [self.num1, self.num2] and 8 not in [self.num1, self.num2] and 7 not in [self.num1, self.num2] and 6 not in [self.num1, self.num2] and 5 not in [self.num1, self.num2] and 1 not in [self.num1, self.num2]  and 3 not in [self.num1, self.num2] and 2 not in [self.num1, self.num2] and self.num3 not in [4, 9]:
                self.answer = 2
            elif 10 not in [self.num1, self.num2] and 8 not in [self.num1, self.num2] and 7 not in [self.num1, self.num2] and 6 not in [self.num1, self.num2] and 1 not in [self.num1, self.num2] and 4 not in [self.num1, self.num2]  and 3 not in [self.num1, self.num2] and 2 not in [self.num1, self.num2] and self.num3 not in [5, 9]:
                self.answer = 2
            elif 10 not in [self.num1, self.num2] and 8 not in [self.num1, self.num2] and 7 not in [self.num1, self.num2] and 1 not in [self.num1, self.num2] and 5 not in [self.num1, self.num2] and 4 not in [self.num1, self.num2]  and 3 not in [self.num1, self.num2] and 2 not in [self.num1, self.num2] and self.num3 not in [6, 9]:
                self.answer = 2
            elif 10 not in [self.num1, self.num2] and 8 not in [self.num1, self.num2] and 1 not in [self.num1, self.num2] and 6 not in [self.num1, self.num2] and 5 not in [self.num1, self.num2] and 4 not in [self.num1, self.num2]  and 3 not in [self.num1, self.num2] and 2 not in [self.num1, self.num2] and self.num3 not in [7, 9]:
                self.answer = 2
            elif 10 not in [self.num1, self.num2] and 1 not in [self.num1, self.num2] and 7 not in [self.num1, self.num2] and 6 not in [self.num1, self.num2] and 5 not in [self.num1, self.num2] and 4 not in [self.num1, self.num2]  and 3 not in [self.num1, self.num2] and 2 not in [self.num1, self.num2] and self.num3 not in [8, 9]:
                self.answer = 2
            
        return self.answer
        
def animate(BG):
    global info_stavka
    x, y = 10, 0
    spin = 1000
    num1 = rd(1, len(img) - 1)
    num2 = rd(1, len(img) - 1)
    num3 = rd(1, len(img) - 1)
    num4 = rd(1, len(img) - 1)
    num5 = rd(1, len(img) - 1)
    num6 = rd(1, len(img) - 1)
    num7 = rd(1, len(img) - 1)
    num8 = rd(1, len(img) - 1)
    num9 = rd(1, len(img) - 1)
    num10 = rd(1, len(img) - 1)
    num11 = rd(1, len(img) - 1)
    num12 = rd(1, len(img) - 1)
    num13 = rd(1, len(img) - 1)
    num14 = rd(1, len(img) - 1)
    num15 = rd(1, len(img) - 1)
    music = pg.mixer.music.load('music/spin.mp3')
    pg.mixer.music.play(0)
    while spin > 0:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        
        screen.blit(BG, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        screen.blit(info_stavka, (1000, 600))
        screen.blit(img_circle, (1030, 500))
        
        # 1 барабан
        surf.blit(img[num1], (x, y))
        surf.blit(img[num2], (x, y - 160))
        surf.blit(img[num3], (x, y - 320))
        surf.blit(img[1], (x, y - 480))
        surf.blit(img[2], (x, y - 640))
        surf.blit(img[9], (x, y - 800))
        surf.blit(img[1], (x, y - 960))
        surf.blit(img[5], (x, y - 1120))
        surf.blit(img[4], (x, y - 1280))
        
        # барабан
        surf.blit(img[num4], (x + 160, y))
        surf.blit(img[num5], (x + 160, y - 160))
        surf.blit(img[num6], (x + 160, y - 320))
        surf.blit(img[3], (x + 160, y - 480))
        surf.blit(img[10], (x + 160, y - 640))
        surf.blit(img[1], (x + 160, y - 800))
        surf.blit(img[1], (x + 160, y - 960))
        surf.blit(img[7], (x + 160, y - 1120))
        surf.blit(img[6], (x + 160, y - 1280))
        # 3 барабан
        surf.blit(img[num7], (x + 320, y))
        surf.blit(img[num8], (x + 320, y - 160))
        surf.blit(img[num9], (x + 320, y - 320))
        surf.blit(img[9], (x + 320, y - 480))
        surf.blit(img[2], (x + 320, y - 640))
        surf.blit(img[2], (x + 320, y - 800))
        surf.blit(img[10], (x + 320, y - 960))
        surf.blit(img[4], (x + 320, y - 1120))
        surf.blit(img[1], (x + 320, y - 1280))
        # 4 барабан
        surf.blit(img[num10], (x + 480, y))
        surf.blit(img[num11], (x + 480, y - 160))
        surf.blit(img[num12], (x + 480, y - 320))
        surf.blit(img[10], (x + 480, y - 480))
        surf.blit(img[6], (x + 480, y - 640))
        surf.blit(img[4], (x + 480, y - 800))
        surf.blit(img[7], (x + 480, y - 960))
        surf.blit(img[9], (x + 480, y - 1120))
        surf.blit(img[1], (x + 480, y - 1280))
        # 5 барабан
        surf.blit(img[num13], (x + 640, y))
        surf.blit(img[num14], (x + 640, y - 160))
        surf.blit(img[num15], (x + 640, y - 320))
        surf.blit(img[4], (x + 640, y - 480))
        surf.blit(img[9], (x + 640, y - 640))
        surf.blit(img[5], (x + 640, y - 800))
        surf.blit(img[10], (x + 640, y - 960))
        surf.blit(img[8], (x + 640, y - 1120))
        surf.blit(img[7], (x + 640, y - 1280))
        y += 20
        spin -= 15
                 
        pg.display.update()
        

def start():
    global num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, winses, img1
    setting = rd(0, 10)
    scaters = 0
    
    if setting != 3:
        num1 = rd(1, len(img) - 2)
        num2 = rd(1, len(img) - 2)
        num3 = rd(1, len(img) - 2)
        num4 = rd(1, len(img) - 2)
        num5 = rd(1, len(img) - 2)
        num6 = rd(1, len(img) - 2)
        num7 = rd(1, len(img) - 2)
        num8 = rd(1, len(img) - 2)
        num9 = rd(1, len(img) - 2)
        num10 = rd(1, len(img) - 2)
        num11 = rd(1, len(img) - 2)
        num12 = rd(1, len(img) - 2)
        num13 = rd(1, len(img) - 2)
        num14 = rd(1, len(img) - 2)
        num15 = rd(1, len(img) - 2)
    elif setting == 1 or setting == 4 or setting == 10:
        num1 = rd(1, len(img) - 1)
        num2 = rd(1, len(img) - 1)
        num3 = rd(1, len(img) - 1)
        num4 = rd(1, len(img) - 1)
        num5 = rd(1, len(img) - 1)
        num6 = rd(1, len(img) - 1)
        num7 = rd(1, len(img) - 1)
        num8 = rd(1, len(img) - 1)
        num9 = rd(1, len(img) - 1)
        num10 = rd(1, len(img) - 1)
        num11 = rd(1, len(img) - 1)
        num12 = rd(1, len(img) - 1)
        num13 = rd(1, len(img) - 1)
        num14 = rd(1, len(img) - 1)
        num15 = rd(1, len(img) - 1)
    
    else:
        num1 = rd(1, len(img))
        num2 = rd(1, len(img))
        num3 = rd(1, len(img))
        num4 = rd(1, len(img))
        num5 = rd(1, len(img))
        num6 = rd(1, len(img))
        num7 = rd(1, len(img))
        num8 = rd(1, len(img))
        num9 = rd(1, len(img))
        num10 = rd(1, len(img))
        num11 = rd(1, len(img))
        num12 = rd(1, len(img))
        num13 = rd(1, len(img))
        num14 = rd(1, len(img))
        num15 = rd(1, len(img))

    img1 = img[num1].convert_alpha()
    img2 = img[num2].convert_alpha()
    img3 = img[num3].convert_alpha()
    img4 = img[num4].convert_alpha()
    img5 = img[num5].convert_alpha()
    img6 = img[num6].convert_alpha()
    img7 = img[num7].convert_alpha()
    img8 = img[num8].convert_alpha()
    img9 = img[num9].convert_alpha()
    img10 = img[num10].convert_alpha()
    img11 = img[num11].convert_alpha()
    img12 = img[num12].convert_alpha()
    img13 = img[num13].convert_alpha()
    img14 = img[num14].convert_alpha()
    img15 = img[num15].convert_alpha()


    surf.blit(img1, (10, 0))
    surf.blit(img2, (10, 150))
    surf.blit(img3, (10, 300))
    surf.blit(img4, (170, 0))
    surf.blit(img5, (170, 150))
    surf.blit(img6, (170, 300))
    surf.blit(img7, (330, 0))
    surf.blit(img8, (330, 150))
    surf.blit(img9, (330, 300))
    surf.blit(img10, (490, 0))
    surf.blit(img11, (490, 150))
    surf.blit(img12, (490, 300))
    surf.blit(img13, (660, 0))
    surf.blit(img14, (660, 150))
    surf.blit(img15, (660, 300))
    
    screen.blit(bg, (0, 0))
    screen.blit(surf, ((W - W1) // 2, (H - H1) // 2))
    scaters = scater(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15)
    
    if scaters == 3:
        winses += st
        info_bonus_game(st, 10)
        bonus_game(10)
        
    elif scaters == 4:
        winses += st * 2
        info_bonus_game(st * 2, 15)
        bonus_game(15)
        
    elif scaters == 5:
        winses += st * 10
        info_bonus_game(st * 10, 20)
        bonus_game(20)
        
    elif scaters == 6:
        winses += st * 15
        info_bonus_game(st * 15, 25)
        bonus_game(25)
        
    elif scaters == 7:
        winses += st * 20
        info_bonus_game(st * 20, 30)
        bonus_game(30)
        
    else:
        score(st)
    
    
    pg.display.flip()
    clock.tick(fps)
   
def first():
    global st

    screen.blit(bg, (0, 0))
    screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
    screen.blit(img_circle, (1300, 500))
    music = pg.mixer.music.load('music/2.mp3')
    pg.mixer.music.play(0)
        
    surf.blit(pg.image.load('img1/lion.png').convert_alpha(), (10, 0))
    surf.blit(pg.image.load('img1/scater.png').convert_alpha(), (10, 150))
    surf.blit(pg.image.load('img1/rabbit.png').convert_alpha(), (10, 300))
    surf.blit(pg.image.load('img1/lion.png').convert_alpha(), (170, 0))
    surf.blit(pg.image.load('img1/V.png').convert_alpha(), (170, 150))
    surf.blit(pg.image.load('img1/rabbit.png').convert_alpha(), (170, 300))
    surf.blit(pg.image.load('img1/lion.png').convert_alpha(), (330, 0))
    surf.blit(pg.image.load('img1/V.png').convert_alpha(), (330, 150))
    surf.blit(pg.image.load('img1/rabbit.png').convert_alpha(), (330, 300))
    surf.blit(pg.image.load('img1/lion.png').convert_alpha(), (490, 0))
    surf.blit(pg.image.load('img1/V.png').convert_alpha(), (490, 150))
    surf.blit(pg.image.load('img1/rabbit.png').convert_alpha(), (490, 300))
    surf.blit(pg.image.load('img1/lion.png').convert_alpha(), (660, 0))
    surf.blit(pg.image.load('img1/scater.png').convert_alpha(), (660, 150))
    surf.blit(pg.image.load('img1/rabbit.png').convert_alpha(), (660, 300))

    main(st)

def show_stavka():
    global st
    X = (0, 0)
    flag = True
    st5 = text.render('5', True, COLOR_TEXT)
    st10 = text.render('10', True, COLOR_TEXT)
    st20 = text.render('20', True, COLOR_TEXT)
    st50 = text.render('50', True, COLOR_TEXT)
    st100 = text.render('100', True, COLOR_TEXT)
    st200 = text.render('200', True, COLOR_TEXT)
    st500 = text.render('500', True, COLOR_TEXT)
    st1000 = text.render('1000', True, COLOR_TEXT)
    while flag:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    X = pg.mouse.get_pos()

        if X[0] > 1090 and X[0] < 1150:
            if X[1] > 310 and X[1] < 340:
                st = 5
                main(st)
            elif X[1] > 350 and X[1] < 390:
                st = 10
                main(st)
            elif X[1] > 390 and X[1] < 430:
                st = 20
                main(st)
            elif X[1] > 430 and X[1] < 470:
                st = 50
                main(st)
            elif X[1] > 470 and X[1] < 510:
                st = 100
                main(st)
            elif X[1] > 510 and X[1] < 550:
                st = 200
                main(st)
            elif X[1] > 550 and X[1] < 590:
                st = 500
                main(st)
            elif X[1] > 590 and X[1] < 630:
                st = 1000
                main(st)

        screen.blit(bg, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        
        screen.blit(st5, (1100, 320))
        screen.blit(st10, (1098, 360))
        screen.blit(st20, (1100, 400))
        screen.blit(st50, (1100, 440))
        screen.blit(st100, (1098, 480))
        screen.blit(st200, (1100, 520))
        screen.blit(st500, (1100, 560))
        screen.blit(st1000, (1098, 600))

        pg.display.update()

def lines():
    global coin, st, money, winses
    winses = 0
    draw_line = []
    wins = []
    line = [[num1, num4, num7, num10, num13], [num2, num5, num8, num11, num14], [num3, num6, num9, num12, num15], [num1, num5, num9, num11, num13], 
            [num3, num5, num7, num11, num15], [num1, num4, num8, num10, num13], [num1, num5, num8, num11, num13], [num2, num4, num7, num10, num14], 
            [num2, num6, num9, num12, num14], [num3, num6, num8, num12, num15], [num3, num5, num8, num11, num15], [num2, num5, num9, num11, num14]]
    
    for i in range(len(line)):
        show = Check(line[i][0], line[i][1], line[i][2], line[i][3], line[i][4])
        if show.check() == 5:
            wins.append(5)
            draw_line.append(i)
            music = pg.mixer.music.load('music/win.mp3')
            pg.mixer.music.play(0)
            if 1 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['10'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 2 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['J'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 3 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['Q'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 4 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['K'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 5 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['A'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 6 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['lion'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 7 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['bear'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 8 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['rabbit'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 9 in [line[i][0], line[i][1], line[i][2], line[i][3], line[i][4]]:
                winses += st * money['V'][5]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
                
        elif show.check() == 4:
            wins.append(4)
            draw_line.append(i)
            music = pg.mixer.music.load('music/win.mp3')
            pg.mixer.music.play(0)
            if 1 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['10'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 2 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['J'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 3 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['Q'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 4 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['K'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 5 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['A'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 6 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['lion'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 7 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['bear'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 8 in [line[i][0], line[i][1], line[i][2], line[i][3]]:
                winses += st * money['rabbit'][4]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            
            
        elif show.check() == 3:
            wins.append(3)
            draw_line.append(i)
            music = pg.mixer.music.load('music/win.mp3')
            pg.mixer.music.play(0)
            if 1 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['10'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 2 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['J'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 3 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['Q'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 4 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['K'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 5 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['A'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 6 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['lion'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 7 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['bear'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            elif 8 in [line[i][0], line[i][1], line[i][2]]:
                winses += st * money['rabbit'][3]
                coin += winses
                
                if winses - st > 3 * st:
                    music = pg.mixer.music.load('music/win2.mp3')
                    pg.mixer.music.play(0)
            
            
        elif show.check() == 2:
            if line[i][0] not in [1, 2, 3, 4, 5, 10] and line[i][1] not in [1, 2, 3, 4, 5, 10]:
                wins.append(2)
                draw_line.append(i)
                music = pg.mixer.music.load('music/win.mp3')
                pg.mixer.music.play(0)
                if 6 in [line[i][0], line[i][1]]:
                    winses += st * money['lion'][2]
                    coin += winses
                    if winses - st > 3 * st:
                        music = pg.mixer.music.load('music/win2.mp3')
                        pg.mixer.music.play(0)
                elif 7 in [line[i][0], line[i][1]]:
                    winses += st * money['bear'][2]
                    coin += winses
                    if winses - st > 3 * st:
                        music = pg.mixer.music.load('music/win2.mp3')
                        pg.mixer.music.play(0)
                elif 8 in [line[i][0], line[i][1]]:
                    winses += st * money['rabbit'][2]
                    coin += winses
                    if winses - st > 3 * st:
                        music = pg.mixer.music.load('music/win2.mp3')
                        pg.mixer.music.play(0)
            

    return (wins, draw_line)

def draw_Lines(x):
    if winses > st * 3 and winses < st * 6:
        win_info = text.render(f'большой выигрыш: {winses}', True, (0, 51, 255))
        win_pos = (450, 600)
    elif winses > st * 6:
        text1 = pg.font.SysFont('arial', 50)
        win_info = text1.render(f'Мега выирыш: {winses}', True, (102, 51, 0))
        win_pos = (400, 590)
    else:
        win_info = text.render(f'Выиграш: {winses}', True, (COLOR_TEXT))
        win_pos = (500, 600)
    
    if x == 0:
        pg.draw.line(screen, (255, 255, 255), (200, 190), (1000, 190), 5)
        screen.blit(win_info, win_pos)
        
    elif x == 1:
        pg.draw.line(screen, (200, 255, 0), (200, 340), (1000, 340), 5)
        screen.blit(win_info, win_pos)
        
    elif x == 2:
        pg.draw.line(screen, (196, 14, 0), (200, 490), (1000, 490), 5)
        screen.blit(win_info, win_pos)
        
    elif x == 3:
        pg.draw.line(screen, (150, 120, 200), (220, 170), (590, 520), 6)
        pg.draw.line(screen, (150, 120, 200), (590, 520), (960, 170), 6)
        screen.blit(win_info, win_pos)
        
    elif x == 4:
        pg.draw.line(screen, (200, 200, 15), (240, 540), (590, 170), 6)
        pg.draw.line(screen, (200, 200, 15), (590, 170), (960, 540), 6)
        screen.blit(win_info, win_pos)
        
    elif x == 5:
        pg.draw.line(screen, (202, 110, 196), (200, 200), (440, 200), 6)
        pg.draw.line(screen, (202, 110, 196), (440, 200), (590, 350), 6)
        pg.draw.line(screen, (202, 110, 196), (590, 350), (740, 200), 6)
        pg.draw.line(screen, (202, 110, 196), (740, 200), (1000, 200), 6)
        screen.blit(win_info, win_pos)
        
    elif x == 6:
        pg.draw.line(screen, (197, 100, 58), (230, 190), (400, 350), 6)
        pg.draw.line(screen, (197, 100, 58), (400, 350), (780, 350), 6)
        pg.draw.line(screen, (197, 100, 58), (780, 350), (950, 190), 6)
        screen.blit(win_info, win_pos)

    elif x == 7:
        pg.draw.line(screen, (205, 0, 200), (260, 350), (430, 210), 6)
        pg.draw.line(screen, (205, 0, 200), (430, 210), (770, 210), 6)
        pg.draw.line(screen, (205, 0, 200), (770, 210), (940, 350), 6)
        screen.blit(win_info, win_pos)
        
    elif x == 8:
        pg.draw.line(screen, (160, 90, 87), (260, 360), (430, 510), 6)
        pg.draw.line(screen, (160, 90, 87), (430, 510), (770, 510), 6)
        pg.draw.line(screen, (160, 90, 87), (770, 510), (940, 360), 6)
        screen.blit(win_info, win_pos)
        
    elif x == 9:
        pg.draw.line(screen, (255, 100, 90), (200, 500), (430, 500), 6)
        pg.draw.line(screen, (255, 100, 90), (430, 500), (590, 350), 6)
        pg.draw.line(screen, (255, 100, 90), (590, 350), (760, 500), 6)
        pg.draw.line(screen, (255, 100, 90), (760, 500), (1000, 500), 6)
        screen.blit(win_info, win_pos)
        
    elif x == 10:
        pg.draw.line(screen, (0, 255, 100), (260, 500), (410, 340), 6)
        pg.draw.line(screen, (0, 255, 100), (410, 340), (780, 340), 6)
        pg.draw.line(screen, (0, 255, 100), (780, 340), (940, 500), 6)
        screen.blit(win_info, win_pos)
        
    elif x == 11:
        pg.draw.line(screen, (15, 200, 255), (200, 350), (420, 350), 6)
        pg.draw.line(screen, (15, 200, 255), (420, 350), (590, 510), 6)
        pg.draw.line(screen, (15, 200, 255), (590, 510), (760, 350), 6)
        pg.draw.line(screen, (15, 200, 255), (760, 350), (1000, 350), 6)
        screen.blit(win_info, win_pos)
            
def score(ST):
    global coin, info_money, info_stavka
    X1 = (0, 0)
    a = lines()
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if coin < st:
                        finish()
                    else:
                        coin -= ST
                        surf.blit(bg1, (0, 0))
                        animate(bg)
                        surf.blit(bg1, (0, 0))
                        start()
                        
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    X1 = pg.mouse.get_pos()         
                        
        
        if X1[0] > 1000 and X1[0] < 1100 and X1[1] < 650 and X1[1] > 600:
               show_stavka()
        elif X1[0] > 1000 and X1[0] < 1150 and X1[1] < 550 and X1[1] > 500:
            if coin < st:
                finish()
            else:
                coin -= ST
                surf.blit(bg1, (0, 0))
                animate(bg)
                surf.blit(bg1, (0, 0))
                start()
                
        info_money = text.render(f'money: {coin}', True, COLOR_TEXT)
        info_stavka = text.render(f'ставка: {st}', True, COLOR_TEXT)
        screen.blit(bg, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        screen.blit(info_stavka, (1000, 600))
        screen.blit(img_circle, (1030, 500))

        for i in a[1]:
            draw_Lines(i)
 
        pg.display.update()
        clock.tick(fps)

def info_bonus_game(win, spin):
    music = pg.mixer.music.load('music/bonus_win.mp3')
    pg.mixer.music.play(0)
    info_win = text.render(f'выигрыш: {win}', True, (COLOR_TEXT))
    info_spin = text.render(f'Поздровляем вы выиграли {spin}, бесплатных вращений', True, (51, 0, 0))
    soft = 400
    while soft > 0:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()  
        
        screen.blit(bg, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        screen.blit(info_stavka, (1000, 600))
        screen.blit(img_circle, (1030, 500))
        screen.blit(info_win, (500, 600))
        screen.blit(info_spin, (190, 80))
        
        pg.display.update()
        clock.tick(fps)
        soft -= 1

def bonus_start(spin, win=0):
    global num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, winses
    setting = rd(0, 30)
    
    if setting != 3:
        num1 = rd(1, len(img) - 2)
        num2 = rd(1, len(img) - 2)
        num3 = rd(1, len(img) - 2)
        num4 = rd(1, len(img) - 2)
        num5 = rd(1, len(img) - 2)
        num6 = rd(1, len(img) - 2)
        num7 = rd(1, len(img) - 2)
        num8 = rd(1, len(img) - 2)
        num9 = rd(1, len(img) - 2)
        num10 = rd(1, len(img) - 2)
        num11 = rd(1, len(img) - 2)
        num12 = rd(1, len(img) - 2)
        num13 = rd(1, len(img) - 2)
        num14 = rd(1, len(img) - 2)
        num15 = rd(1, len(img) - 2)
    elif setting == 1 or setting == 4 or setting == 10:
        num1 = rd(1, len(img) - 1)
        num2 = rd(1, len(img) - 1)
        num3 = rd(1, len(img) - 1)
        num4 = rd(1, len(img) - 1)
        num5 = rd(1, len(img) - 1)
        num6 = rd(1, len(img) - 1)
        num7 = rd(1, len(img) - 1)
        num8 = rd(1, len(img) - 1)
        num9 = rd(1, len(img) - 1)
        num10 = rd(1, len(img) - 1)
        num11 = rd(1, len(img) - 1)
        num12 = rd(1, len(img) - 1)
        num13 = rd(1, len(img) - 1)
        num14 = rd(1, len(img) - 1)
        num15 = rd(1, len(img) - 1)
    
    else:
        num1 = rd(1, len(img))
        num2 = rd(1, len(img))
        num3 = rd(1, len(img))
        num4 = rd(1, len(img))
        num5 = rd(1, len(img))
        num6 = rd(1, len(img))
        num7 = rd(1, len(img))
        num8 = rd(1, len(img))
        num9 = rd(1, len(img))
        num10 = rd(1, len(img))
        num11 = rd(1, len(img))
        num12 = rd(1, len(img))
        num13 = rd(1, len(img))
        num14 = rd(1, len(img))
        num15 = rd(1, len(img))

    img1 = img[num1].convert_alpha()
    img2 = img[num2].convert_alpha()
    img3 = img[num3].convert_alpha()
    img4 = img[num4].convert_alpha()
    img5 = img[num5].convert_alpha()
    img6 = img[num6].convert_alpha()
    img7 = img[num7].convert_alpha()
    img8 = img[num8].convert_alpha()
    img9 = img[num9].convert_alpha()
    img10 = img[num10].convert_alpha()
    img11 = img[num11].convert_alpha()
    img12 = img[num12].convert_alpha()
    img13 = img[num13].convert_alpha()
    img14 = img[num14].convert_alpha()
    img15 = img[num15].convert_alpha()


    surf.blit(img1, (10, 0))
    surf.blit(img2, (10, 150))
    surf.blit(img3, (10, 300))
    surf.blit(img4, (170, 0))
    surf.blit(img5, (170, 150))
    surf.blit(img6, (170, 300))
    surf.blit(img7, (330, 0))
    surf.blit(img8, (330, 150))
    surf.blit(img9, (330, 300))
    surf.blit(img10, (490, 0))
    surf.blit(img11, (490, 150))
    surf.blit(img12, (490, 300))
    surf.blit(img13, (660, 0))
    surf.blit(img14, (660, 150))
    surf.blit(img15, (660, 300))
    

    screen.blit(bg, (0, 0))
    screen.blit(surf, ((W - W1) // 2, (H - H1) // 2))
   
    win += winses
    bonus_score(spin, win)
    pg.display.flip()
    clock.tick(fps)

def bonus_finish(win):
    global coin
    info_win = text.render(f'общий выиграш: {win}', True, (51, 0, 0))
    soft = 200
    while soft != 0:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        screen.blit(bonus_bg, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        screen.blit(info_stavka, (1000, 600))
        screen.blit(img_circle, (1030, 500))
        screen.blit(info_win, (450, 600))
        soft -= 1
        pg.display.update()
        clock.tick(fps)
    
    main(st)


def bonus_score(spin, win):
    global coin, info_money, info_stavka
    X1 = (0, 0)
    a = lines()
    all_win = win
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if spin > 0:
                        spin -= 1
                        surf.blit(bonus_bg1, (0, 0))
                        animate(bonus_bg)
                        surf.blit(bonus_bg1, (0, 0))
                        bonus_start(spin, all_win)
                        
                    else:
                        bonus_finish(all_win)
        
        info_win = text.render(f'Общий выигрыш: {all_win}', True, (COLOR_TEXT))
        info_spin = text.render(f'free spins {spin}', True, (COLOR_TEXT))
        info_money = text.render(f'money: {coin}', True, COLOR_TEXT)
        info_stavka = text.render(f'ставка: {st}', True, COLOR_TEXT)

        screen.blit(bonus_bg, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        screen.blit(info_stavka, (1000, 600))
        screen.blit(img_circle, (1030, 500))
        screen.blit(info_spin, (900, 40))
        screen.blit(info_win, (400, 650))

        for i in a[1]:
            draw_Lines(i)
 
        pg.display.update()
        clock.tick(fps)
    

def bonus_game(spin):
    while spin != 0:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    spin -= 1
                    surf.blit(bonus_bg1, (0, 0))
                    animate(bonus_bg)
                    surf.blit(bonus_bg1, (0, 0))
                    bonus_start(spin)
        
        screen.blit(bonus_bg, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        screen.blit(info_stavka, (1000, 600))
        screen.blit(img_circle, (1030, 500))

        pg.display.update()
        clock.tick(fps)

def main(st):
    global text, info_money, coin, X, info_stavka
    text = pg.font.SysFont('arial', 40)
    X = (500, 1)
   
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if coin < st:
                        finish()
                    else:
                        
                        coin -= st
                        surf.blit(bg1, (0, 0))
                        animate(bg)
                        surf.blit(bg1, (0, 0))
                        start() 
                        
                                  
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    X = pg.mouse.get_pos()
             
        
        if X[0] > 1000 and X[0] < 1100 and X[1] < 650 and X[1] > 600:
            show_stavka()
        elif X[0] > 1040 and X[0] < 1150 and X[1] < 550 and X[1] > 500:
            if coin < st:
                finish()
            else:
                coin -= st
                surf.blit(bg1, (0, 0))
                animate(bg)
                surf.blit(bg1, (0, 0))
                start()

        

        info_money = text.render(f'money: {coin}', True, COLOR_TEXT)
        info_stavka = text.render(f'ставка: {st}', True, COLOR_TEXT)
        

        screen.blit(bg, (0, 0))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        screen.blit(info_money, (30, 600))
        screen.blit(info_stavka, (1000, 600))
        screen.blit(img_circle, (1030, 500))
 
        pg.display.update()
        clock.tick(fps)

def finish():
    
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if coin > 0:
                        main(st)
                    else:
                        finish()
        
        surf1 = pg.Surface((800, 200))
        text1 = pg.font.SysFont('arial', 70)
        info_finish = text1.render('Недостаточно средств', True, COLOR_TEXT)
        
        
        screen.blit(bg, (0, 0))
        surf1.fill((200, 50, 102))
        screen.blit(surf, ((W - W1) / 2, (H - H1) / 2))
        surf1.blit(info_finish, (70, 50))
        screen.blit(surf1, (W / 2 - 400, H / 2 - 100))
        

        pg.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    first()

