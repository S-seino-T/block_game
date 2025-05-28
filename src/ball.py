import pygame
from src.common import Object, CONFIG


class Ball(Object):
    def __init__(self):
        super().__init__(
            CONFIG["screen_width"] // 2,
            CONFIG["screen_height"] // 2,
            10,
            10,
            (255, 255, 255),
        )
        self.speed = [5, -5]

    def move(self, keys=None):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.left <= 0 or self.rect.right >= CONFIG["screen_width"]:
            self.speed[0] *= -1
        if self.rect.top <= 0:
            self.speed[1] *= -1

    def bounce(self):
        self.speed[1] *= -1

    def draw(self, screen: pygame.Surface):
        pygame.draw.ellipse(screen, self.color, self.rect)
