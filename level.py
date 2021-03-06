import pygame
import tile


class Level:
    def __init__(self, file, center):
        self.file = file
        self.tile_grid = []
        self.tile_grid_dimensions = (0, 0)
        self.tile_size = 0
        self.center = (center[0]/2, center[1]/2)
        self.camera_modes = {0: 'centered_on_car', 1: 'static'}
        self.camera_mode = ''
        self.nCheckpoints = 0
        self.autoblocks = []
        self.char_grid = []
        self.dim_x = 0
        self.dim_y = 0

    def load(self):
        # Reads text file with characters which are converted into tiles from the Tile class
        f = open(self.file, 'r')
        file = f.read()

        # Read settings
        reading_word = True
        reading_value = False
        reading_map = False
        word = ''
        value = ''
        char_grid = []
        for c in file:
            if reading_word:
                if c != ':':
                    word += c
                else:
                    reading_word = False
                    reading_value = True
            elif reading_value:
                if c != '\n':
                    value += c
                else:
                    if word == 'tile_size':
                        self.tile_size = int(value)
                        word = ''
                        value = ''
                        reading_word = True
                        reading_value = False
                    elif word == 'tile_grid_dimension_x':
                        self.dim_x = int(value)
                        word = ''
                        value = ''
                        reading_word = True
                        reading_value = False
                    elif word == 'tile_grid_dimension_y':
                        self.dim_y = int(value)
                        word = ''
                        value = ''
                        reading_word = True
                        reading_value = False
                    elif word == 'camera_mode':
                        self.camera_mode = value
                        word = ''
                        value = ''
                        reading_word = True
                        reading_value = False
                    elif word == 'number_of_checkpoints':
                        self.nCheckpoints = int(value)
                        word = ''
                        value = ''
                        reading_word = True
                        reading_value = False
                    if '---' in word:
                        reading_word = False
                        reading_value = False
                        reading_map = True
                        word = ''
            elif reading_map:
                if c != ',' and c != '\n':
                    word += c
                else:
                    char_grid.append(word)
                    word = ''
        f.close()
        return char_grid

    def create(self, char_grid):
        # Make map with Tiles
        self.tile_grid_dimensions = (self.dim_x, self.dim_y)
        x, y = (self.tile_size/2, self.tile_size/2)
        for c in char_grid:
            self.tile_grid.append(tile.Tile(c, (x, y), self.tile_size))
            if self.tile_grid[-1].type == 'start':                                          # search for start tile
                self.startTile = self.tile_grid[-1]
            x += self.tile_size
            if int((x-self.tile_size/2)/self.tile_size) == self.tile_grid_dimensions[0]:
                x = self.tile_size/2
                y += self.tile_size

    def center_map(self):
        dx, dy = (self.center[0]-self.startTile.center[0], self.center[1]-self.startTile.center[1])
        for t in self.tile_grid:
            t.move(-dx, -dy)
            # t.center = (t.center[0] + dx, t.center[1] + dy)
            # t.upperleft = (t.upperleft[0] + dx, t.upperleft[1] + dy)

    def draw(self, display_surf):
        for t in self.tile_grid:
            t.draw(display_surf)

    def move(self, player_block):
        dx, dy = (0, 0)
        if player_block.up:
            dy = -player_block.speed
        if player_block.down:
            dy = player_block.speed
        if player_block.left:
            dx = -player_block.speed
        if player_block.right:
            dx = player_block.speed

        # move the level
        for t in self.tile_grid:
            t.move(dx, dy)
        # move the autoblocks

        # check for collisions
        if player_block.is_colliding(self):
            for t in self.tile_grid:
                t.move(-dx, -dy)
        else:
            for b in self.autoblocks:
                b.move(dx, dy)

    def resize(self, d):
        # Resize level
        for t in self.tile_grid:
            t.tile_size += d
            tmp = []
            for img in t.img:
                img2 = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                tmp.append(img2)
            t.img = tmp
            self.create(self.char_grid)
        # Resize blocks
        for a in self.autoblocks:
            a.size += d
