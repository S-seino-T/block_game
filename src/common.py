from abc import ABC, abstractmethod
import pygame

CONFIG = {
    "screen_width": 800,
    "screen_height": 600,
    "fps": 60,
}


class Object(ABC):
    def __init__(
        self, x: int, y: int, width: int, height: int, color: tuple[int, int, int]
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    @abstractmethod
    def move(self, keys):
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass
