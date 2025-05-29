import pygame
import sys
from src.common import CONFIG, Object
from src.ball import Ball
from src.paddle import Paddle
from src.block import Block
from src.stage import Stage


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (CONFIG["screen_width"], CONFIG["screen_height"])
        )
        pygame.display.set_caption("誰が為のブロック崩し")
        self.state = "title"
        self.stage_index = 0
        self.stage = Stage.load_stage()
        self.clock = pygame.time.Clock()
        self.ball = Ball()
        self.paddle = Paddle()
        self.blocks = [
            Block(x * 80 + 10, y * 30 + 10) for x in range(10) for y in range(5)
        ]
        self.score = 0

        self.font = pygame.font.SysFont("Hiragino Maru Gothic Pro", 36)

        self.background_image = pygame.image.load("assets/img/cat.jpg").convert()
        self.background_image = pygame.transform.scale(
            self.background_image, (CONFIG["screen_width"], CONFIG["screen_height"])
        )

    def run(self):
        while True:
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
            if self.state == "title" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_stage(0)
            elif self.state == "clear" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_stage()

    def start_stage(self, index):
        self.stage_index = index
        self.paddle = Paddle()
        self.ball = Ball()
        self.blocks = self.stage[index]
        self.state = "playing"

    def next_stage(self):
        if self.stage_index + 1 < len(self.stage):
            self.start_stage(self.stage_index + 1)
        else:
            self.state = "title"

    def update(self):
        if self.state != "playing":
            return

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

        if not self.blocks:
            self.state = "clear"

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        if self.state == "title":
            self.draw_title()
        elif self.state == "clear":
            self.draw_clear()
        elif self.state == "playing":
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            for b in self.blocks:
                b.draw(self.screen)

            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

    def draw_title(self):
        title = self.font.render("Tagatame No Block Kuzushi", True, (255, 255, 255))
        start = self.font.render("Press 'space' to start", True, (255, 255, 255))
        self.screen.blit(
            title,
            (
                CONFIG["screen_width"] // 2 - title.get_width() // 2,
                CONFIG["screen_height"] // 3,
            ),
        )
        self.screen.blit(
            start,
            (
                CONFIG["screen_width"] // 2 - title.get_width() // 2,
                CONFIG["screen_height"] // 2,
            ),
        )

    def draw_clear(self):
        msg = self.font.render(
            "Clear! (press 'space' to next stage)", True, (255, 255, 0)
        )
        self.screen.blit(
            msg,
            (
                CONFIG["screen_width"] // 2 - msg.get_width() // 2,
                CONFIG["screen_height"] // 2,
            ),
        )
