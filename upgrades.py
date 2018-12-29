import pygame
import button
import screen_message

class Upgrades:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.img = pygame.transform.scale(pygame.image.load('textures/upgrade_panel_32x32.png'), (self.size[0], self.size[1]))
        self.rect = self.img.get_rect()
        self.buy_block_btn = button.Button((self.pos[0]+65, self.pos[1]+50), (200, 50), 'Buy block racer', 'buy_block')
        self.show = False

        self.buttons = []
        self.buttons.append(self.buy_block_btn)

    def draw(self, display):
        if self.show:
            rect = pygame.Rect(self.rect[0] + self.pos[0], self.rect[1] + self.pos[1], self.size[0], self.size[1])
            display.blit(self.img, rect)
            self.buy_block_btn.draw(display)
