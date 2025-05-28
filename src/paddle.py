import pygame
from src.common import Object, CONFIG


class Paddle(Object):
    def __init__(self):
        super().__init__(
            CONFIG["screen_width"] // 2,
            CONFIG["screen_height"] - 20,
            120,
            10,
            (255, 255, 255),
        )
        self.speed = 7

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < CONFIG["screen_width"]:
            self.rect.x += self.speed

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
