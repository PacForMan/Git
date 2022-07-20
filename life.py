import pygame
from random import randint
from copy import deepcopy



#Размер поля
RES = WIDTH, HEIGHT = 1280, 720
#Размер клетки
TILE = 10
W, H = WIDTH // TILE, HEIGHT // TILE
#Частота обновления
FPS = 60

#class Background(pygame.sprite.Sprite):
#    def __init__(self, image_file, location):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.image.load(image_file)
#        self.rect = self.image.get_rect()
#        self.rect.left, self.rect.top = location

#BackGround = Background('photo_2022-07-12_21-16-59.jpg', [0,0])

#pygame.mixer.init()

#pygame.mixer.music.load("Sound_15648.mp3")
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play()


next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j%H][i%W] == 1:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:

    surface.fill('Black')
    #surface.blit(BackGround.image, BackGround.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #[pygame.draw.line(surface, pygame.Color(''), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE) ]
    #[pygame.draw.line(surface, pygame.Color(''), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE) ]

    for x in range(1, W -1):
        for y in range(1, H -1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('pink'), (x * TILE + 2, y * TILE + 2, TILE -2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)

    pygame.display.flip()
    clock.tick(FPS)