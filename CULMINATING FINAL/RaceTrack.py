# Program Name: RaceTrack Class
# Programmer: Shrish Luitel, Kshitij Kapoor, Eishan Ashraf
# Date of Completion: 6/16/2023
# Description: This is the RaceTrack class, and is responsible
# for updating which map is being played on. Depending on the map
# the coresponding starting position, collision detection, and lap completion
# is updated. 


# Imports
import pygame
import math
import random

from LuckyBlock import *

# Map Class
class RaceTrack():

    # Initialize the 2 maps
    def __init__(self, map_num):
        self.map1 = pygame.image.load('track1.png')
        self.map1 = pygame.transform.scale(self.map1, (800, 800))

        self.map2 = pygame.image.load ('space_map.png')
        self.map2 = pygame.transform.scale(self.map2, (1000, 800))

        self.num = map_num
        self.lucky_list = []

    # Return back which track is being used
    # Update luckyblock and car starting positions
    def get_map(self, car, car_two, car_rect, car_two_rect, car1, car2):
        
        if self.num == 1:
            # Update luckyblock
            luckyloot = LuckyBlock()
            self.luckyblock1 = luckyloot.get_lucky_block (350, 55)
            self.luckyblock2 = luckyloot.get_lucky_block (720, 350)
            self.luckyblock3 = luckyloot.get_lucky_block (350, 725)

            self.lucky_list = [self.luckyblock1, self.luckyblock2,
                               self.luckyblock3]

            car_rect.center = (45, 380)
            car_two_rect.center = (90, 380)
            
            return self.map1

        else:
            # Update window
            luckyloot = LuckyBlock()   
            WINDOW = pygame.display.set_mode((1000, 800))

            # Set default car position
            car = pygame.transform.scale(car, (20, 25))
            car_two = pygame.transform.scale(car_two, (20, 25))

            car1.angle = -90
            car2.angle = -90
           
            car_rect.center = (410, 720)
            car_two_rect.center = (410, 770)

            # Update lucky block
            self.luckyblock1 = luckyloot.get_lucky_block (350, 75)
            self.luckyblock2 = luckyloot.get_lucky_block (690, 270)
            self.luckyblock3 = luckyloot.get_lucky_block (350, 525)

            self.lucky_list = [self.luckyblock1, self.luckyblock2,
                               self.luckyblock3]           
           
            return self.map2


    def collision_detection(self, car_rect):
        # All position collision detection for map one
        # Return true, and freeze in the respective x or y position
        if (self.num == 1) :

            if (car_rect.x > 750) :
                car_rect.x = 750
                return True

            if (car_rect.x < 30) :
                car_rect.x = 30
                return True

            if (car_rect.y < 30) :
                car_rect.y = 30
                return True

            if (car_rect.y > 750) :
                car_rect.y = 750
                return True

            if ((car_rect.y > 115) and (car_rect.y > 380) and
                    (car_rect.x < 110) and (car_rect.y < 390)) :
                car_rect.y = 380
                return True

            if ((car_rect.x > 102) and (car_rect.x < 110) and
                    (car_rect.y > 115) and (car_rect.y < 665)) :
                car_rect.x = 102
                return True

            if ((car_rect.x > 105) and (car_rect.x < 680) and
                    (car_rect.y > 115) and (car_rect.y < 125)) :
                car_rect.y = 115
                return True

            if ((car_rect.x < 685) and (car_rect.x > 675) and
                    (car_rect.y > 115) and (car_rect.y < 660)) :
                car_rect.x = 685
                return True

            if ((car_rect.x < 685) and (car_rect.x > 105) and
                    (car_rect.y > 655) and (car_rect.y < 665)) :
                car_rect.y = 665
                return True

            else:
                return False

        # Map 2
        else:
            if (car_rect.y > 760):
                car_rect.y = 760
                return True

            if (car_rect.x > 930):
                car_rect.x = 930
                return True

            if (car_rect.y < 55):
                car_rect.y = 55
                return True

            if (car_rect.x < 75):
                car_rect.x = 75
                return True

            if (car_rect.y < 690 and car_rect.y > 680 and
                150 < car_rect.x < 850):
                
                car_rect.y = 690
                return True

            if (car_rect.x < 860 and car_rect.x > 850 and
                310 < car_rect.y < 700):
                
                car_rect.x = 860
                return True

            if (car_rect.x < 660 and car_rect.x > 650 and car_rect.y < 310 and
                car_rect.y > 140):
                
                car_rect.x = 660
                return True

            if (car_rect.x < 860 and car_rect.x > 650 and
                305 < car_rect.y < 315):
                car_rect.y = 305
                return True

            if (140 < car_rect.y < 210 and car_rect.x < 860 and
                car_rect.x > 850):
                
                car_rect.x = 860
                return True

            if (car_rect.x < 860 and car_rect.x > 730 and
                220 < car_rect.y < 225):
                
                car_rect.y = 225
                return True

            if (730 < car_rect.x < 860 and car_rect.y > 120 and
                car_rect.y < 125):
                
                car_rect.y = 120
                return True

            if (140 < car_rect.y < 210 and car_rect.x > 720 and
                car_rect.x < 725):
                
                car_rect.x = 720
                return True

            if (175 < car_rect.x < 660 and 125 < car_rect.y < 135):
                car_rect.y = 125
                return True

            if (125 < car_rect.y < 230 and 145 < car_rect.x < 155):
                car_rect.x = 145
                return True

            if (0 < car_rect.x < 425 and 345 < car_rect.y < 355):
                car_rect.y = 345
                return True

            if (145 < car_rect.x < 555 and 230 < car_rect.y < 240):
                car_rect.y = 240
                return True

            if (535 < car_rect.x < 545 and 230 < car_rect.y < 540):
                car_rect.x = 535
                return True

            if (150 < car_rect.x < 555 and 525 < car_rect.y < 535):
                car_rect.y = 525
                return True

            if (350 < car_rect.y < 420 and 430 < car_rect.x < 440):
                car_rect.x = 440
                return True

            if (0 < car_rect.x < 420 and 430 < car_rect.y < 440):
                car_rect.y = 440
                return True

            if (535 < car_rect.y < 690 and 140 < car_rect.x < 150):
               car_rect.x = 140
               return True

            if (385 < car_rect.x < 395 and 670 < car_rect.y < 800):
                car_rect.x = 395
                return True

    #Check for lap completion        
    def lap(self, car_rect, vel, angle):
        if (self.num == 1):
            # Check if car is by finish line
            if (car_rect.y < 404 and car_rect.y > 397 and car_rect.x > 30 and
                car_rect.x < 110):

                # If car is trying to stop at finish line or glitch through
                # Force them through it
                if (vel >= 0):
                    vel = 8

                else:
                    vel = -8

                # Update the position of car
                car_rect.x -= vel * math.sin(math.radians(angle))
                car_rect.y -= vel * math.sin(math.radians(90 - angle))

                # Reset the despawned luckyblocks and random position in map
                if (self.luckyblock1.x == 1000):
                    self.luckyblock1.x = random.randint(200, 600)
                    self.luckyblock1.y = 55

                if (self.luckyblock2.x == 1000):
                    self.luckyblock2.x = 700
                    self.luckyblock2.y = random.randint (200, 600)

                if (self.luckyblock3.x == 1000):
                    self.luckyblock3.x = random.randint(200, 600)
                    self.luckyblock3.y = 700

                # Update that map was crossed
                return True

        # Same concept for map 2
        else:
            if (670 < car_rect.y < 800 and 383 < car_rect.x < 390):
                if (vel >= 0):
                    vel = 8

                else:
                    vel = -8

                car_rect.x -= vel * math.sin(math.radians(angle))
                car_rect.y -= vel * math.sin(math.radians(90 - angle))

                if (self.luckyblock1.x == 1000):
                    self.luckyblock1.x = random.randint(350, 750)
                    self.luckyblock1.y = 75

                if (self.luckyblock2.x == 1000):
                    self.luckyblock2.y = 270
                    self.luckyblock2.x = random.randint (630, 800)

                if (self.luckyblock3.x == 1000):
                    self.luckyblock3.x = random.randint(200, 420)
                    self.luckyblock3.y = 505

                return True
