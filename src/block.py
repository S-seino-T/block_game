import pygame
from src.common import Object, CONFIG


class Block(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 70, 20, (255, 0, 0))

    def move(self, keys=None):
        pass

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
