import pygame


class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/trees/pine_tree.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

        self.x = 0
        self.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
