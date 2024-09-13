# Program Name: LuckBlock Class
# Programmer: Shrish Luitel, Kshitij Kapoor, Eishan Ashraf
# Date of Completion: 6/16/2023
# Description: This class is responsible for creating the object for the
# lucky block. This will allow for an infinite amount of luckyblock
# objects to be created.

# Imports
import pygame

# LuckyBlock Class
class LuckyBlock():
    
    # Gets the lucky block and returns the x and y positions
    def get_lucky_block(self, x, y):
        
        lucky_block = pygame.image.load("luckyblock_p.png")
        lucky_block = pygame.transform.scale(lucky_block, (50, 50))
        lucky_block_rect = lucky_block.get_rect()
        lucky_block_rect.center = (x, y)
        
        return lucky_block_rect
