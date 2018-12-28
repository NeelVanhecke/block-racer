import pygame
import tile

class Block:
    def __init__(self, center, size, auto=True):
        # Geometry
        self.center = center
        self.size = size
        self.upperleft = (self.center[0]-self.size/2, self.center[1]-self.size/2)
        self.rect = pygame.Rect(self.upperleft[0], self.upperleft[1], self.size, self.size)
        self.color = (0, 0, 255)
        # Type
        self.auto = auto
        # States
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.on_tiles = []
        self.checkpoints_cleared = []
        # Settings
        self.MAX_SPEED = 10
        self.speed = 5

    def center_to_upperleft(self):
        return (self.center[0]-self.size, self.center[1]-self.size)

    def draw(self, display_surf):
        # self.upperleft = self.center_to_upperleft()
        pygame.draw.rect(display_surf, self.color, pygame.Rect(self.upperleft[0], self.upperleft[1], self.size, self.size))

    def is_colliding(self, level):
        for t in level.tile_grid:
            for f in t.forbidden:
                if f.colliderect(self.rect):
                    return True
        return False

    def is_on_tiles(self, level):
        self.on_tiles = []
        for t in level.tile_grid:
            if t.rect.colliderect(self.rect):
                self.on_tiles.append(t)

    def update_status(self, level):
        self.is_on_tiles(level)
        for t in self.on_tiles:
            if t.type == 'checkpoint':
                for r in t.roi:
                    if self.rect.colliderect(r):
                        print('checkpoint')
            elif t.type == 'start':
                for r in t.roi:
                    if self.rect.colliderect(r):
                        print('start')


    def move_manually(self, level):
        x, y = self.center
        x_old, y_old = (x, y)
        if self.up:
            y -= self.speed
        if self.down:
            y += self.speed
        if self.left:
            x -= self.speed
        if self.right:
            x += self.speed
        # self.center = (x, y)
        if not self.is_colliding(level):
            self.center = (x, y)

        #     # Check if driving through finish -> did we cross all checkpoints?
        #     if t.type == tile.Tile.types_dict['start']:
        #         for c in level.checkpoints_cleared:
        #             if c == False:
        #                 level.finish = False
        #                 break
        #             level.finish = True
        #             self.money += 1
        #             level.reset()
        #     # Check if driving through checkpoint -> which checkpoint?
        #     if t.type == tile.Tile.types_dict['checkpoint']:
        #         for c in range(0, len(level.checkpoints)):
        #             if t == level.checkpoints[c]:
        #                 level.checkpoints_cleared[c] = True

    def move(self, level):
        if not self.auto:
            self.move_manually(level)
        # else:
        #     self.move_automatically(level)
