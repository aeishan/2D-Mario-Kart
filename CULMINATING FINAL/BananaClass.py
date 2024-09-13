# Program Name: Banana Class
# Programmer: Shrish Luitel, Kshitij Kapoor, Eishan Ashraf
# Date of Completion: 6/16/2023
# Description: This class is responsible for creating the object for
# the Bananas. This will allow for an infinite amount of bananaa objects
# to be created.

# Imports
import pygame

# Banana Class
class Banana():

    #Initialize and load up image
    def __init__(self):
        self.banana = pygame.image.load('banana.png')
        self.banana = pygame.transform.scale(self.banana, (35, 35))
        self.banana_rect = self.banana.get_rect()

    # Returns the banana as rectangle
    def get_banana(self, x, y):
        self.banana_rect.center = (x, y)
        return self.banana_rect

    # Returns regular image
    def get_reg_banana(self):
        return self.banana
