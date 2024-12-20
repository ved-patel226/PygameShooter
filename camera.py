import pygame


def lerp(start, end, amount):
    return start + (end - start) * amount


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.target_x = 0
        self.target_y = 0
        self.smoothing = (
            0.1  # Adjust this value between 0 and 1 to change smoothing amount
        )

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Calculate target position
        self.target_x = -target.rect.centerx + int(self.width / 2)
        self.target_y = -target.rect.centery + int(self.height / 2)

        # Smoothly move camera toward target
        current_x = self.camera.x
        current_y = self.camera.y

        new_x = lerp(current_x, self.target_x, self.smoothing)
        new_y = lerp(current_y, self.target_y, self.smoothing)

        # Clamp values
        new_x = min(0, new_x)
        new_y = min(0, new_y)

        self.camera = pygame.Rect(new_x, new_y, self.width, self.height)
