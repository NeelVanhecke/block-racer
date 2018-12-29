import pygame
import block

class Button:
    def __init__(self, pos, size, text, type, bg_color_std = (145, 95, 35), bg_color_hl = (255, 167, 62), fg_color = (0, 0, 0)):
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.pos = pos
        self.size = size
        self.text = text
        self.bg_color_std = bg_color_std
        self.bg_color_hl = bg_color_hl
        self.fg_color = fg_color
        self.highlighted = False
        self.is_clicked = False
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.type = type

    def draw(self, display):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        textSurfaceObj = self.font.render(self.text, True, self.fg_color)
        if not self.highlighted:
            pygame.draw.rect(display, self.bg_color_std, rect)
        else:
            pygame.draw.rect(display, self.bg_color_hl, rect)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.midleft = (self.pos[0], self.pos[1]+self.size[1] / 2)
        display.blit(textSurfaceObj, textRectObj)

    def clicked(self, game):
        if self.type == 'upgrade_btn':
            game.upgrades.show = True
        elif self.type == 'buy_block':
            for tile in game.level.tile_grid:
                if tile.type == 'start':
                    x = tile.center[0]
                    y = tile.center[1]
                    game.level.autoblocks.append(block.Block((x, y), 100,  (255, 0, 0)))
                    game.level.autoblocks[-1].up = True


