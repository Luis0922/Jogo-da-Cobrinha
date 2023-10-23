import pygame, sys

class Cobra:
    def __init__(self, corpo, size):
        self.corpo = corpo
        self.size = size
        
    def move(self, up, down, left, right):
        # Cobra anda automaticamente
        if up:
            self.corpo.insert(0, [self.corpo[0][0], self.corpo[0][1] - self.size])
            self.corpo.pop()
        if down:
            self.corpo.insert(0, [self.corpo[0][0], self.corpo[0][1] + self.size])
            self.corpo.pop()
        if left:
            self.corpo.insert(0, [self.corpo[0][0] - self.size, self.corpo[0][1]])
            self.corpo.pop()
        if right:
            self.corpo.insert(0, [self.corpo[0][0] + self.size, self.corpo[0][1]])
            self.corpo.pop()

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
board_center = (display_size / 2) - (small_square / 2)

cobra = Cobra([[board_center, board_center], [board_center+small_square-2, board_center], [board_center+2*(small_square-2), board_center], [board_center+4*(small_square-2), board_center]], small_square-2)

clock = pygame.time.Clock()
FPS = 90

up = False
down = False
left = True
right = False

clock = pygame.time.Clock()

# e aqui nós entramos no loop do game
while True:
    clock.tick(7)
#                                                         X            Y      TAMANHO X   TAMANHO Y
    pygame.draw.rect(display_surf, black, pygame.Rect(white_space, white_space, board_size, board_size),  1)
    pygame.draw.rect(display_surf, white, pygame.Rect(white_space+1, white_space+1, board_size-2, board_size-2))
    for parte in cobra.corpo:
        pygame.draw.rect(display_surf, red, pygame.Rect(parte[0], parte[1], cobra.size, cobra.size))

    # Detecta teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        up = True
        down = False
        left = False
        right = False
    if keys[pygame.K_DOWN]:
        up = False
        down = True
        left = False
        right = False
    if keys[pygame.K_LEFT]:
        up = False
        down = False
        left = True
        right = False
    if keys[pygame.K_RIGHT]:
        up = False
        down = False
        left = False
        right = True
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # Logica de derrota
    if cobra.corpo[0][0] < white_space or cobra.corpo[0][0] >= white_space + board_size - cobra.size + 1:
        pygame.quit()
    if cobra.corpo[0][1] < white_space or cobra.corpo[0][1] >= white_space + board_size - cobra.size + 1:
        pygame.quit()

    # monitoramos os eventos
    for evento in pygame.event.get():
        # se o evento foi um pedido para sair
        if evento.type == pygame.QUIT:
            # fechamos a tela do jogo 
            pygame.quit()
            # e saimos do programa
            sys.exit()

    # redesenha a tela continuamente 
    cobra.move(up, down, left, right)
    pygame.display.update()