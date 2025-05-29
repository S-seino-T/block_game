import pygame
import sys
from src.common import CONFIG, Object
from src.ball import Ball
from src.paddle import Paddle
from src.block import Block


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (CONFIG["screen_width"], CONFIG["screen_height"])
        )
        pygame.display.set_caption("誰が為のブロック崩し")
        self.clock = pygame.time.Clock()
        self.ball = Ball()
        self.paddle = Paddle()
        self.blocks = [
            Block(x * 80 + 10, y * 30 + 10) for x in range(10) for y in range(5)
        ]
        self.score = 0

        self.font = pygame.font.Font(None, 36)

        self.background_image = pygame.image.load("assets/img/cat.jpg").convert()
        self.background_image = pygame.transform.scale(
            self.background_image, (CONFIG["screen_width"], CONFIG["screen_height"])
        )

    def run(self):
        while True:
            self.screen.blit(self.background_image, (0, 0))
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(CONFIG["fps"])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.paddle.move(keys)
        self.ball.move()

        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.bounce()

        is_hit = self.ball.rect.collidelist([b.rect for b in self.blocks])
        if is_hit != -1:
            hit_block = self.blocks.pop(is_hit)
            # self.ball.bounce()
            self.ball.bounce_block(hit_block.rect)
            self.score += 10

        if self.ball.rect.bottom >= CONFIG["screen_height"]:
            pygame.quit()
            sys.exit()

    def draw(self):
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for b in self.blocks:
            b.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
