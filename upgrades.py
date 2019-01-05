import pygame
import button
import screen_message

class Upgrades:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.img = pygame.transform.scale(pygame.image.load('textures/upgrade_panel_32x32.png'), (self.size[0], self.size[1]))
        self.rect = self.img.get_rect()
        self.buy_block_btn = button.Button((self.pos[0]+55, self.pos[1]+75), (200, 50), 'Buy block racer (1)', 'buy_block')
        self.upgrade_speed_btn = button.Button((self.pos[0]+55, self.pos[1]+135), (200, 50), 'Buy speed upgrade (10)', 'buy_speed')
        self.show = False

        self.buttons = []
        self.buttons.append(self.buy_block_btn)
        self.buttons.append(self.upgrade_speed_btn)

    def draw(self, display):
        if self.show:
            rect = pygame.Rect(self.rect[0] + self.pos[0], self.rect[1] + self.pos[1], self.size[0], self.size[1])
            display.blit(self.img, rect)

            for button in self.buttons:
                button.draw(display)
