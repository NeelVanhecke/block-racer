import pygame
import screen_message
import button

class Stats:
    def __init__(self, pos, size):
        # Everything in local coordinates
        self.pos = pos
        self.size = size
        self.img = pygame.transform.scale(pygame.image.load('textures/stats_32x32.png'), (self.size[0], self.size[1]))
        self.rect = self.img.get_rect()
        self.buttons = []
        self.coins_msg = screen_message.Screen_message(  (self.pos[0] + 20, self.pos[1] + 110), (0, 0), 'Coins: 0', (0, 0, 0), (145, 95, 35))
        self.upgrade_btn = button.Button((115, 260), (115, 50), 'Upgrades', 'upgrade_btn')  # (0, 0, 0), (145, 95, 35)

        self.buttons.append(self.upgrade_btn)

    def draw(self, display):
        rect = pygame.Rect(self.rect[0]+self.pos[0], self.rect[1]+self.pos[1], self.size[0], self.size[1])
        display.blit(self.img, rect)
        self.coins_msg.draw(display)
        self.upgrade_btn.draw(display)