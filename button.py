import pygame


class Button:
    BG_COLOR = (237, 198, 177)
    FONT_COLOR = (20, 108, 148)
    BORDER_COLOR = (183, 183, 183)
    SELECTED_BUTTON_COLOR = (191, 204, 181)

    BUTTON_WIDTH = 80
    BUTTON_HEIGHT = 40
    PADDING = 1
    BORDER_WIDTH = 2

    def __init__(self, pattern, text, pos):
        self.pattern = pattern
        self.text = text
        self.x, self.y = pos
        self.font = pygame.font.SysFont('Arial', 18)
        self.surface = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.surface.fill(self.BG_COLOR)
        self.label = self.font.render(text, True, self.FONT_COLOR)
        self.label_x = (self.surface.get_width() - self.label.get_width()) // 2
        self.label_y = (self.surface.get_height() - self.label.get_height()) // 2
        self.surface.blit(self.label, (self.label_x, self.label_y))
        self.is_clicked = False

    def draw(self, screen):
        if self.is_clicked:
            bg_color = self.SELECTED_BUTTON_COLOR
        else:
            bg_color = self.BG_COLOR

        self.surface.fill(bg_color)
        self.surface.blit(self.label, (self.label_x, self.label_y))
        pygame.draw.rect(screen, self.BORDER_COLOR,
                         (self.x, self.y, self.surface.get_width(), self.surface.get_height()), self.BORDER_WIDTH)
        screen.blit(self.surface, (self.x, self.y))

    def is_button_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.surface.get_width() and \
            self.y <= pos[1] <= self.y + self.surface.get_height()

    def set_is_clicked(self, is_clicked):
        self.is_clicked = is_clicked
