import pygame
import tile

class Block:
    def __init__(self, center, size, color=(0, 0, 255), auto=True):
        # Geometry
        self.center = center
        self.size = size
        self.upperleft = (self.center[0]-self.size/2, self.center[1]-self.size/2)
        self.rect = pygame.Rect(self.upperleft[0], self.upperleft[1], self.size, self.size)
        self.color = color
        # Type
        self.auto = auto
        # States
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.on_tiles = []
        self.checkpoints_cleared = []
        self.all_checkpoints_cleared = False
        # Settings
        self.MAX_SPEED = 10
        self.speed = 10

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
        on_tiles = []
        for t in level.tile_grid:
            if t.rect.colliderect(self.rect):
                on_tiles.append(t)
        return on_tiles
                # print('---')
                # print(self.color)
                # print(self.on_tiles)

    def update_status(self, level, stats):
        self.on_tiles = self.is_on_tiles(level)

        for t in self.on_tiles:
            # Check if passed through checkpoint
            if t.type == 'checkpoint':
                for r in t.roi:
                    if self.rect.colliderect(r) and t not in self.checkpoints_cleared:
                        self.checkpoints_cleared.append(t)
                        if len(self.checkpoints_cleared) == level.nCheckpoints:
                            self.all_checkpoints_cleared = True
            # Check if passed through finish
            elif t.type == 'start':
                for r in t.roi:
                    if self.rect.colliderect(r):
                        if self.all_checkpoints_cleared:
                            self.checkpoints_cleared = []
                            self.all_checkpoints_cleared = False
                            stats.money += 1
                            stats.coins_msg.text = 'Coins: %s' % stats.money
                            print('finished')


    def move(self, dx, dy):
        x = self.center[0] - dx
        y = self.center[1] - dy
        self.center = (x, y)
        x = self.upperleft[0] - dx
        y = self.upperleft[1] - dy
        self.upperleft = (x, y)
        self.rect = pygame.Rect(self.upperleft[0], self.upperleft[1], self.size, self.size)

    def on_one_tile(self):
        if len(self.on_tiles) == 1:
            on_one_tile = True
        else:
            on_one_tile = False
        return on_one_tile

    def auto_move(self, level):
        x, y = self.center
        dx, dy = (0, 0)
        if self.up:
            dy = -self.speed
        if self.down:
            dy = self.speed
        if self.left:
            dx = -self.speed
        if self.right:
            dx = self.speed

        self.on_tiles = self.is_on_tiles(level)
        self.move(-dx, -dy)
        if self.on_one_tile():
            tmp_tile = self.on_tiles[0]
            if tmp_tile.type == 'bend1':
                if self.right == True:
                    if self.center[0] > tmp_tile.upperleft[0] + level.tile_size/2:
                        self.right = False
                        self.down = True
                if self.up == True:
                    if self.center[1] < tmp_tile.upperleft[1] + level.tile_size/2:
                        self.up = False
                        self.left = True
            if tmp_tile.type == 'bend2':
                if self.right == True:
                    if self.center[0] > tmp_tile.upperleft[0] + level.tile_size/2:
                        self.right = False
                        self.up = True
                if self.down == True:
                    if self.center[1] > tmp_tile.upperleft[1] + level.tile_size/2:
                        self.down = False
                        self.left = True
            if tmp_tile.type == 'bend3':
                if self.left == True:
                    if self.center[0] < tmp_tile.upperleft[0] + level.tile_size/2:
                        self.left = False
                        self.up = True
                if self.down == True:
                    if self.center[1] > tmp_tile.upperleft[1] + level.tile_size/2:
                        self.down = False
                        self.right = True
            if tmp_tile.type == 'bend4':
                if self.up == True:
                    if self.center[1] < tmp_tile.upperleft[1] + level.tile_size/2:
                        self.up = False
                        self.right = True
                if self.left == True:
                    if self.center[0] < tmp_tile.upperleft[0] + level.tile_size/2:
                        self.left = False
                        self.down = True


        # for t in self.on_tiles:
        #     # Check if driving off road -> prohibit movement
        #     if t.type == tile.Tile.types_dict['grass']:
        #         self.center = (x_old, y_old)
        #     # Check if driving through finish -> did we cross all checkpoints?
        #     if t.type == tile.Tile.types_dict['start']:
        #         print('start')
        #         for c in level.checkpoints_cleared:
        #             if c == False:
        #                 level.finish = False
        #                 break
        #             level.finish = True
        #             self.money += 1
        #             level.reset()
        #             print('finished')
        #     # Check if driving through checkpoint -> which checkpoint?
        #     if t.type == tile.Tile.types_dict['checkpoint']:
        #         for c in range(0, len(level.checkpoints)):
        #             if t == level.checkpoints[c]:
        #                 level.checkpoints_cleared[c] = True
        #                 print('checkpoint cleared')