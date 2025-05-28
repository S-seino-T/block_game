from src.ball import Ball
from src.block import Block
from src.paddle import Paddle
import pygame
import sys
from src.common import CONFIG


def init():
    pygame.init()
    screen = pygame.display.set_mode((CONFIG["screen_width"], CONFIG["screen_height"]))
    pygame.display.set_caption("誰が為のブロック崩し")
    clock = pygame.time.Clock()
    return screen, clock


def main():
    screen, clock = init()
    ball = Ball()
    paddle = Paddle()
    blocks = [Block(x * 80 + 10, y * 30 + 10) for x in range(10) for y in range(5)]

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        paddle.move(keys)
        ball.move()

        if ball.rect.colliderect(paddle.rect):
            ball.bounce()

        is_hit = ball.rect.collidelist([b.rect for b in blocks])
        if is_hit != -1:
            blocks.pop(is_hit)
            ball.bounce()

        if ball.rect.bottom >= CONFIG["screen_height"]:
            pygame.quit()
            sys.exit()

        ball.draw(screen)
        paddle.draw(screen)
        for block in blocks:
            block.draw(screen)

        pygame.display.flip()
        clock.tick(CONFIG["fps"])


if __name__ == "__main__":
    main()
