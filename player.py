import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            "assets/characters/happy_boo/square_ref.png"
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

        self.x = 0
        self.y = 0

    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x = -5
        elif key[pygame.K_RIGHT]:
            self.x = 5
        else:
            self.x = 0

        if key[pygame.K_UP]:
            self.y = -5
        elif key[pygame.K_DOWN]:
            self.y = 5
        else:
            self.y = 0

        self.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
