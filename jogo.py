import pygame, sys
import random

class Sneak:
    def __init__(self, body, size):
        self.body = body
        self.size = size

    def move(self, up, down, left, right, grow):
        # Cobra anda automaticamente
        if up:
            self.body.insert(0, [self.body[0][0], self.body[0][1] - self.size])
            if grow == False:
                self.body.pop()
        if down:
            self.body.insert(0, [self.body[0][0], self.body[0][1] + self.size])
            if grow == False:
                self.body.pop()
        if left:
            self.body.insert(0, [self.body[0][0] - self.size, self.body[0][1]])
            if grow == False:
                self.body.pop()
        if right:
            self.body.insert(0, [self.body[0][0] + self.size, self.body[0][1]])
            if grow == False:
                self.body.pop()

class Food:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def update_place(self):
        bigger_randint = int(board_size / small_square)
        self.x = self.y = white_space + small_square/2 + (small_square)*random.randint(1, bigger_randint-2)

pygame.init()

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_size = 400

display_surf = pygame.display.set_mode((display_size, display_size))

display_surf.fill(white) 

pygame.display.set_caption('Jogo da Cobrinha')

board_size = display_size - 100
white_space = (display_size - board_size)/2
small_square = 20
board_center = (display_size / 2)

snake = Sneak([[board_center, board_center]], small_square)

bigger_randint = int(board_size / small_square)
food_position = white_space + small_square/2 + (small_square)*random.randint(0, bigger_randint-2)
food = Food(food_position, food_position, small_square/2)

clock = pygame.time.Clock()
FPS = 90

up = False
down = False
left = True
right = False
bloqueado = 'right'

clock = pygame.time.Clock()

score = 0
pygame.font.init()
score_source = pygame.font.SysFont("Arial", 20, False, False)

# e aqui nós entramos no loop do game
while True:
    display_surf.fill((255, 255, 255))
    text_score = score_source.render(f"Score: {score}", 1, (0, 0, 0))
    display_surf.blit(text_score, (0, 0))

    clock.tick(5)
#                                                         X            Y      TAMANHO X   TAMANHO Y
    grow = False
    pygame.draw.rect(display_surf, black, pygame.Rect(white_space, white_space, board_size, board_size),  1)
    pygame.draw.rect(display_surf, white, pygame.Rect(white_space+1, white_space+1, board_size-2, board_size-2))
    # Food
    pygame.draw.rect(display_surf, black, pygame.Rect(food.x, food.y, food.size, food.size))
    # Snake
    for parte in snake.body:
        pygame.draw.rect(display_surf, red, pygame.Rect(parte[0], parte[1], snake.size, snake.size))

    # Detecta teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and bloqueado != 'up':
        up = True
        down = False
        left = False
        right = False
        bloqueado = 'down'
    if keys[pygame.K_DOWN] and bloqueado != 'down':
        up = False
        down = True
        left = False
        right = False
        bloqueado = 'up'
    if keys[pygame.K_LEFT] and bloqueado != 'left':
        up = False
        down = False
        left = True
        right = False
        bloqueado = 'right'
    if keys[pygame.K_RIGHT] and bloqueado != 'right':
        up = False
        down = False
        left = False
        right = True
        bloqueado = 'left'
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # Logica de vitoria


    # Logica de derrota
    if snake.body[0][0] < white_space or snake.body[0][0] >= white_space + board_size - snake.size + 1:
        pygame.quit()
    if snake.body[0][1] < white_space or snake.body[0][1] >= white_space + board_size - snake.size + 1:
        pygame.quit()
    # A cabeça encontrou o proprio corpo
    for i in range(1, len(snake.body)):
        if snake.body[0] == snake.body[i]:
            pygame.quit()

    # Cobra comer comida
    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        score = score + 100
        grow = True
        food.update_place()


    # monitoramos os eventos
    for evento in pygame.event.get():
        # se o evento foi um pedido para sair
        if evento.type == pygame.QUIT:
            # fechamos a tela do jogo 
            pygame.quit()
            # e saimos do programa
            sys.exit()

    # redesenha a tela continuamente 
    snake.move(up, down, left, right, grow)
    pygame.display.update()