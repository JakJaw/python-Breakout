import pygame
from paddle import Paddle
from PILA import Ball
from brick import Brick

pygame.init()

Pila = (255, 153, 153)
PLAYER = (192, 108, 132)
Text = (246, 114, 128)

Last_row = (82, 37, 70)
Seconnd_row = (136, 48, 78)
First_row = (226, 62, 87)

Background = (49, 29, 63)

score = 0
lives = 5

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("JakJaw's Breakout")

paddle = Paddle(PLAYER, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

PILA = Ball(Pila, 10, 10)
PILA.rect.x = 345
PILA.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle)
all_sprites_list.add(PILA)

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(First_row, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(Seconnd_row, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(Last_row, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

Is_on = True
clock = pygame.time.Clock()

while Is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Is_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                Is_on = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(10)

    all_sprites_list.update()

    if PILA.rect.x >= 790:
        PILA.velocity[0] = -PILA.velocity[0]
    if PILA.rect.x <= 0:
        PILA.velocity[0] = -PILA.velocity[0]
    if PILA.rect.y > 590:
        PILA.velocity[1] = -PILA.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", True, First_row)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(1000)
            Is_on = False
    if PILA.rect.y < 40:
        PILA.velocity[1] = -PILA.velocity[1]

    if pygame.sprite.collide_mask(PILA, paddle):
        PILA.rect.x -= PILA.velocity[0]
        PILA.rect.y -= PILA.velocity[1]
        PILA.bounce()

    brick_collision_list = pygame.sprite.spritecollide(PILA, all_bricks, False)
    for brick in brick_collision_list:
        PILA.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", True, First_row)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(1000)
            Is_on = False

    screen.fill(Background)
    pygame.draw.line(screen, Text, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), True, Text)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), True, Text)
    screen.blit(text, (650, 10))

    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
