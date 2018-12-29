import pygame


class Screen_message:
    def __init__(self, pos, size, text, bg_color, fg_color):
        self.pos = pos
        self.size = size
        self.text = text
        self.bgc = bg_color
        self.fgc = fg_color
        self.font = pygame.font.Font('freesansbold.ttf', 24)

    def draw(self, display_surf):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        pygame.draw.rect(display_surf, self.bgc, rect)
        textSurfaceObj = self.font.render(self.text, True, self.bgc, self.fgc)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.midleft = (self.pos[0], self.pos[1] + self.size[1] / 2)
        display_surf.blit(textSurfaceObj, textRectObj)

