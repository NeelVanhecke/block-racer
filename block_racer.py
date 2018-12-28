import pygame
import sys
import level
import block
from pygame.locals import *


class BlockRacer:
    def __init__(self, dimensions, title):
        self.display = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(title)
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        self.level = level.Level('testlevel.txt', (dimensions[0], dimensions[1]))
        self.level.load()
        self.player = block.Block((dimensions[0]/2, dimensions[1]/2), self.level.tile_size/5, False)

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

            # Update
            if self.level.camera_mode == self.level.camera_modes[0]:        # centered on car
                self.player.move(self.level)
            elif self.level.camera_mode == self.level.camera_modes[1]:      # static
                self.level.move(self.player)

            # Draw
            self.display.fill((37, 126, 43))
            self.level.draw(self.display)
            self.player.draw(self.display)
            pygame.display.update()
            self.fpsClock.tick(self.fps)
            loops += 1


            # Sandbox
            print(self.level.tile_grid[0].rect)
            # print('Loops passed: %s' % loops)
