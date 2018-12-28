import pygame
import block_racer


if __name__ == '__main__':
    pygame.init()
    block_racer = block_racer.BlockRacer((1600, 900), 'Block Racer')
    block_racer.run()
