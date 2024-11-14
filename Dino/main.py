import pygame
import random
import os

pygame.init()

# глобальные переменные
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# изображения динозавра
RUNNING = [pygame.image.load(os.path.join('images/dino', 'DinoRun1.png')), pygame.image.load(os.path.join('images/dino', 'DinoRun2.png'))]

JUMPING = pygame.image.load(os.path.join('images/dino', 'DinoJump.png'))

DUCKING = [pygame.image.load(os.path.join('images/dino', 'DinoDuck1.png')), pygame.image.load(os.path.join('images/dino', 'DinoDuck2.png'))]

DEAD = [pygame.image.load(os.path.join('images/dino', 'DinoDead (1).png')), pygame.image.load(os.path.join('images/dino', 'DinoDead.png'))]

START = pygame.image.load(os.path.join('images/dino', 'DinoStart.png'))

# остольные изображения
LARGE_CACTUS = [pygame.image.load(os.path.join('images/cactus', 'LargeCactus1.png')), pygame.image.load(os.path.join('images/cactus', 'LargeCactus2.png')), 
                pygame.image.load(os.path.join('images/cactus', 'LargeCactus3.png'))]

SMALL_CACTUS = [pygame.image.load(os.path.join('images/cactus', 'SmallCactus1.png')), pygame.image.load(os.path.join('images/cactus', 'SmallCactus2.png')), 
                pygame.image.load(os.path.join('images/cactus', 'SmallCactus3.png'))]

BIRDS = [pygame.image.load(os.path.join('images/birds', 'Bird1.png')), pygame.image.load(os.path.join('images/birds', 'Bird2.png'))]

CLOUD = pygame.image.load(os.path.join('images/other', 'Cloud.png'))

GAME_OVER = pygame.image.load(os.path.join('images/other', 'GameOver.png'))

RESET = pygame.image.load(os.path.join('images/other', 'Reset.png'))

BG = pygame.image.load(os.path.join('images/other', 'Track.png'))

# основная игра
class Dinosaur:

    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.duck_img = DUCKING

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.index_step = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userinput):
        if self.dino_duck:
            self.duck()
        
        if self.dino_run:
            self.run()

        if self.dino_jump:
            self.jump()

        if self.index_step >= 10:
            self.index_step = 0
        
        if userinput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_jump = True
            self.dino_run = False

        elif userinput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True

        elif not (self.dino_jump or userinput[pygame.K_DOWN]):
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True

    
    def run(self):
        self.image = self.run_img[self.index_step // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.index_step += 1

    def jump(self):
        self.image = self.jump_img
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
        

    def duck(self):
        self.image = self.duck_img[self.index_step // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.index_step += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class other:

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class LargeCactus(other):
    
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class SmallCactus(other):
    
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class Bird(other):
    
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1


def main():

    global game_speed, obstacles, x_pos_bg, y_pos_bg, points

    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 14
    obstacles = []
    x_pos_bg = 0
    y_pos_bg = 380
    death_count = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)


    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render('Очки: ' + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        SCREEN.blit(text, text_rect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (x_pos_bg + image_width, y_pos_bg))
        if x_pos_bg < - image_width:
            SCREEN.blit(BG, (x_pos_bg + image_width, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        SCREEN.fill((255, 255, 255))
        userinput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userinput)

        cloud.draw(SCREEN)
        cloud.update()

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRDS))

        for el in obstacles:
            el.draw(SCREEN)
            el.update()
            if player.dino_rect.colliderect(el.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(GAME_OVER, death_count)

        
        background()
        score()
        clock.tick(30)
        pygame.display.update()
        

def menu(image, death_count):
    global points
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            elif event.type == pygame.KEYDOWN:
                main()

        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 20)
        image1 = DEAD[1]
        image1_rect = image1.get_rect()

        if death_count == 0:
            text = font.render('Нажмите любую кнопку для начала игры', True, (0, 0, 0))
            image = START
        
        elif death_count > 0:
            text = font.render('Нажмите любую кнопку для начала игры', True, (0, 0, 0))
            score = font.render('Вашы очки: ' + str(points), True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            image1 = DEAD[0]
            image1_rect = image1.get_rect()
            image1_rect.center = (SCREEN_WIDTH   // 2, SCREEN_HEIGHT // 2 - 170)
            SCREEN.blit(score, score_rect)
            
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        image_rect = image.get_rect()
        image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 70)
        if image1 == DEAD[0]:
            SCREEN.blit(image1, image1_rect)
            SCREEN.blit(text, text_rect)
            SCREEN.blit(image, image_rect)
        else:
            SCREEN.blit(text, text_rect)
            SCREEN.blit(image, image_rect)
        pygame.display.update()

    main()


menu(START, death_count=0)