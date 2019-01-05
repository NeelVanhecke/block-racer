import pygame
import sys
import level
import button
import block
import stats
import upgrades
from pygame.locals import *


class BlockRacer:
    def __init__(self, dimensions, title):
        self.display = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(title)
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        self.level = level.Level('testlevel.txt', (dimensions[0], dimensions[1]))
        (self.level.create(self.level.load()))
        self.level.center_map()
        self.player = block.Block((dimensions[0]/2, dimensions[1]/2), self.level.tile_size/5, (0, 0, 255), False)
        self.stats = stats.Stats((10, 10), (320, 320))
        self.upgrades = upgrades.Upgrades((10, 360), (320, 480))
        self.zoom_in = button.Button((1400, 10), (50, 50), '+', 'zoom_in')
        self.zoom_out= button.Button((1460, 10), (50, 50), '-', 'zoom_out')
        self.buttons_to_draw = [self.zoom_in, self.zoom_out]
        self.buttons = self.stats.buttons+self.upgrades.buttons + [self.zoom_in, self.zoom_out]

    def run(self):
        loops = 0
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.player.up = True
                    if event.key == K_DOWN:
                        self.player.down = True
                    if event.key == K_LEFT:
                        self.player.left = True
                    if event.key == K_RIGHT:
                        self.player.right = True
                if event.type == KEYUP:
                    if event.key == K_UP:
                        self.player.up = False
                    if event.key == K_DOWN:
                        self.player.down = False
                    if event.key == K_LEFT:
                        self.player.left = False
                    if event.key == K_RIGHT:
                        self.player.right = False
                if event.type == MOUSEMOTION:
                    (mouse_x, mouse_y) = event.pos
                    for b in self.buttons:
                        if mouse_x > b.pos[0] and mouse_x < b.pos[0]+b.size[0] and mouse_y > b.pos[1] and mouse_y < b.pos[1]+b.size[1]:
                            b.highlighted = True
                        else:
                            b.highlighted = False
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = event.pos
                    for b in self.buttons:
                        if mouse_x > b.pos[0] and mouse_x < b.pos[0]+b.size[0] and mouse_y > b.pos[1] and mouse_y < b.pos[1]+b.size[1]:
                            b.clicked(self)

            # Update
            if self.level.camera_mode == self.level.camera_modes[0]:        # centered on car
                self.player.move(self.level)
            elif self.level.camera_mode == self.level.camera_modes[1]:      # static
                self.level.move(self.player)
            self.player.update_status(self.level, self.stats)

            for autoblock in self.level.autoblocks:
                autoblock.auto_move(self.level)
                autoblock.update_status(self.level, self.stats)
            # Draw
            self.display.fill((37, 126, 43))
            self.level.draw(self.display)
            self.player.draw(self.display)
            for autoblock in self.level.autoblocks:
                autoblock.draw(self.display)
            for b in self.buttons_to_draw:
                b.draw(self.display)
            self.stats.draw(self.display)
            self.upgrades.draw(self.display)
            pygame.display.update()
            self.fpsClock.tick(self.fps)
            loops += 1


            # Sandbox
            # print(self.upgrades.buttons[0].highlighted)
            # if self.level.autoblocks:
            #     print(self.level.autoblocks[0].auto)
            # print('Loops passed: %s' % loops)
            # print(self.level.tile_size)
            # print(self.level.tile_grid[0].rect)
