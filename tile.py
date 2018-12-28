import pygame


class Tile:
    types_dict = dict(grass=pygame.transform.rotate(pygame.image.load('textures/grass_32x32.png'), -0),
                      bend1=pygame.transform.rotate(pygame.image.load('textures/bend_32x32.png'), -0),
                      bend2=pygame.transform.rotate(pygame.image.load('textures/bend_32x32.png'), -90),
                      bend3=pygame.transform.rotate(pygame.image.load('textures/bend_32x32.png'), -180),
                      bend4=pygame.transform.rotate(pygame.image.load('textures/bend_32x32.png'), -270),
                      vertical=pygame.transform.rotate(pygame.image.load('textures/straight_32x32.png'), -0),
                      horizontal=pygame.transform.rotate(pygame.image.load('textures/straight_32x32.png'), -90),
                      crossroads=pygame.image.load('textures/crossroads_32x32.png'),
                      start=pygame.image.load('textures/finish_32x32.png'),
                      checkpoint=pygame.image.load('textures/checkpoint_32x32.png'))
    png_size = 32

    def __init__(self, char_code, center, tile_size):
        self.tile_size = tile_size
        self.center = center
        self.upperleft = (self.center[0]-self.tile_size/2, self.center[1]-self.tile_size/2)
        self.rect = pygame.Rect(self.upperleft[0], self.upperleft[1], self.tile_size, self.tile_size)
        self.forbidden = [pygame.Rect(0, 0, 0, 0)]
        # self.upperleft = level_pos
        # self.size = tile_size
        # self.center = (self.upperleft[0] + self.size[0], self.upperleft[1] + self.size[1])
        # self.prohibited = [pygame.Rect(0, 0, 0, 0)]

        # Define tile type and which texture to assign to it
        if char_code == '0':
            self.type = 'grass'
            self.img = [pygame.transform.scale(Tile.types_dict['grass'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, self.tile_size, self.tile_size)]
        elif char_code == 'b1':
            self.type = 'bend1'
            self.img = [pygame.transform.scale(Tile.types_dict['bend1'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, self.tile_size, int(self.tile_size*5/32)),
                                    (self.tile_size-int(self.tile_size*5/32), 0, int(self.tile_size*5/32), self.tile_size),
                                    (0, self.tile_size-int(self.tile_size*5/32), int(self.tile_size*5/32), int(self.tile_size*5/32))]
        elif char_code == 'b2':
            self.type = 'bend2'
            self.img = [pygame.transform.scale(Tile.types_dict['bend2'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, self.tile_size-int(self.tile_size*5/32), self.tile_size, int(self.tile_size*5/32)),
                                    (self.tile_size-int(self.tile_size*5/32), 0, int(self.tile_size*5/32), self.tile_size),
                                    (0, 0, int(self.tile_size*5/32), int(self.tile_size*5/32))]
        elif char_code == 'b3':
            self.type = 'bend3'
            self.img = [pygame.transform.scale(Tile.types_dict['bend3'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, self.tile_size-int(self.tile_size*5/32), self.tile_size, int(self.tile_size*5/32)),
                                    (0, 0, int(self.tile_size*5/32), self.tile_size),
                                    (self.tile_size-int(self.tile_size*5/32), 0, int(self.tile_size*5/32), int(self.tile_size*5/32))]
        elif char_code == 'b4':
            self.type = 'bend4'
            self.img = [pygame.transform.scale(Tile.types_dict['bend4'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, self.tile_size, int(self.tile_size*5/32)),
                                    (0, 0, int(self.tile_size*5/32), self.tile_size),
                                    (self.tile_size-int(self.tile_size*5/32), self.tile_size-int(self.tile_size*5/32), int(self.tile_size*5/32), int(self.tile_size*5/32))]
        elif char_code == 'sv':
            self.type = 'vertical'
            self.img = [pygame.transform.scale(Tile.types_dict['vertical'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, int(self.tile_size*5/32), self.tile_size),
                                    (self.tile_size-int(self.tile_size*5/32), 0, int(self.tile_size*5/32), self.tile_size)]
        elif char_code == 'sh':
            self.type = 'horizontal'
            self.img = [pygame.transform.scale(Tile.types_dict['horizontal'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, self.tile_size, int(self.tile_size*5/32)),
                                    (0, self.tile_size-int(self.tile_size*5/32), self.tile_size, int(self.tile_size*5/32))]
        elif char_code == 'c':
            self.type = 'crossroads'
            self.img = [pygame.transform.scale(Tile.types_dict['crossroads'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, int(self.tile_size*5/32), int(self.tile_size*5/32)),
                                    (self.tile_size-int(self.tile_size*5/32), 0, int(self.tile_size*5/32), int(self.tile_size*5/32)),
                                    (0, self.tile_size - int(self.tile_size*5/32), int(self.tile_size*5/32),int(self.tile_size*5/32)),
                                    (self.tile_size - int(self.tile_size * 5/32), self.tile_size - int(self.tile_size * 5/32), int(self.tile_size * 5/32), int(self.tile_size * 5/32))]
        elif char_code == 's':
            self.type = 'start'
            self.img = [pygame.transform.scale(Tile.types_dict['vertical'], (self.tile_size, self.tile_size)),
                        pygame.transform.scale(Tile.types_dict['start'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, int(self.tile_size * 5/32), self.tile_size),
                                    (self.tile_size - int(self.tile_size * 5/32), 0, int(self.tile_size * 5/32),
                                     self.tile_size)]
        elif char_code == 'p':
            self.type = 'checkpoint'
            self.img = [pygame.transform.scale(Tile.types_dict['vertical'], (self.tile_size, self.tile_size)),
                        pygame.transform.scale(Tile.types_dict['checkpoint'], (self.tile_size, self.tile_size))]
            self.forbidden_local = [(0, 0, int(self.tile_size * 5/32), self.tile_size),
                                    (self.tile_size - int(self.tile_size * 5/32), 0, int(self.tile_size * 5/32),
                                     self.tile_size)]
        if self.type == Tile.types_dict['grass']:
            self.drivable = False
        else:
            self.drivable = True

    def draw(self, display_surf):
        for img in self.img:
            self.rect = (self.upperleft[0], self.upperleft[1], self.tile_size, self.tile_size)
            display_surf.blit(img, self.rect)
            for i in self.forbidden:
                pygame.draw.rect(display_surf, (255, 0, 0), i)

    def move(self, dx, dy):
        self.upperleft = (self.upperleft[0]-dx, self.upperleft[1]-dy)
        self.center = (self.center[0]-dx, self.center[1]-dy)
        self.forbidden = []
        for i in self.forbidden_local:
            self.forbidden.append(pygame.Rect(self.upperleft[0]+i[0]-dx, self.upperleft[1]+i[1]-dy, i[2], i[3]))
        # self.forbidden = pygame.Rect(self.upperleft[0], self.upperleft[1], self.tile_size, self.tile_size)