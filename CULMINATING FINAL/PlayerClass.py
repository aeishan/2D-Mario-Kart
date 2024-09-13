# Program Name: Player Class
# Programmer: Shrish Luitel, Kshitij Kapoor, Eishan Ashraf
# Date of Completion: 6/16/2023
# Description: This is the main class responsible for player movement,
# handling position updates for each car object. The class takes inputs
# and updates power-ups, movement, and collision detection based on the
# current situation.


#Imports
import pygame
import math
import random

from BananaClass import *
from RaceTrack import *

# Player Class
class Player () :

    # Initialize main variables that will be updated or used
    def __init__ (self, up, down, left, right, shifty, car, player_name):

        # Key binds
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.car_rect = car
        self.shift = shifty

        # Default physics
        self.angle = 0
        self.vel = 0
        self.lap_count = 0
        self.lap_check = False

        # Power ups
        self.power = False
        self.is_banana = False
        self.boost = False

        self.timer = 0
        self.banana_list = []

        self.power_option = ["Slip", "Boost"]
        self.current_power = "Nothing"

        # Banana
        self.b_x = 0
        self.b_y = 0

        # Name
        self.playername = player_name

    # Update power up on collision of lucky box
    def power_up (self, key, tracker):
        banana_class = Banana ()

        # Loop through all lucky box, and see if car collide
        # Update power up at random
        for lucky in (tracker.lucky_list) :
            if self.car_rect.colliderect (lucky) :

                # Change position, and remove luckyblock
                lucky.x = 1000
                lucky.y = 1000

                self.num = random.randint (0, 1)
                self.current_power = self.power_option [self.num]
                self.power = True
                self.timer = 0

        if (self.power == True) :

            # Slip Power Up
            if (self.current_power == "Slip") :

                if (key [self.shift]) :

                    self.boost = False

                    # Update banana position to car, and place
                    self.b_x =  self.car_rect.x
                    self.b_y = self.car_rect.y

                    self.new_banana = banana_class.get_banana (self.b_x, self.b_y)
                    self.banana_list.append (self.new_banana)

                    self.power = False
                    self.current_power = "Nothing"

            else:

                if (key [self.shift]) :

                    self.boost = True

                    # Setting timer to the amount of frames
                    # And increasing the velocity to a max for boost
                    if (self.timer <= 0.7) :
                        self.vel += 0.2

                        if (self.vel > 7) :
                            self.vel = 7

                    # Once timer is over get rid of boosting
                    else:
                        self.vel -= 0.1
                        self.boost = False
                        self.power = False
                        self.current_power = "Nothing"
                        self.timer = 0

                        if (self.vel < 3) :
                            self.vel = 3

                    self.timer += 0.01

                    # Update angle
                    if (key [self.left]) :
                        self.angle += 3

                    if (key [self.right]) :
                        self.angle -= 3

                    # Update position
                    self.car_rect.x -= self.vel * math.sin(math.radians (self.angle))
                    self.car_rect.y -= self.vel * math.sin(math.radians (90 - self.angle))

                # Slow down when not boosting/when boosting over
                if (not key [self.shift]) :

                    if (self.boost == True) :
                        if self.timer <= 0.7:
                            self.timer += 0.01

                            self.vel -= 0.1

                            if (self.vel < 3) :
                                self.vel = 3

                        else:
                            self.boost = False
                            self.power = False
                            self.current_power = "Nothing"

                        if (key [self.left]) :
                            self.angle += 3

                        if (key [self.right]) :
                            self.angle -= 3

                        self.car_rect.x -= self.vel * math.sin (math.radians(self.angle))
                        self.car_rect.y -= self.vel * math.sin (math.radians(90 - self.angle))


    # Update player position code
    def player_move (self, key, tracker) :

        # Check wall collision
        wall = tracker.collision_detection (self.car_rect)

        # If both keys pressed, stop the car
        if ((key [self.up]) and (key [self.down])) :
            if (self.vel > 0) :
                self.vel -= 0.5

            if (self.vel < 0) :
                self.vel += 0.5

            # Update position
            self.car_rect.x -= self.vel * math.sin (math.radians(self.angle))
            self.car_rect.y -= self.vel * math.cos (math.radians(self.angle))

        else:

            if (self.boost == False) :
                # Move forward
                if (key [self.up]) :

                    # Slow down when hitting wall
                    if (wall == True) :
                        self.vel = 0.1

                    # Accelerate
                    else:
                        self.vel += 0.05

                        if self.vel > 0:
                            self.vel += 0.05

                    # Reach max velocity
                    if (self.vel >= 3) :
                        self.vel = 3

                    # Update car position based off ratio
                    self.car_rect.x -= self.vel * math.sin (math.radians(self.angle))
                    self.car_rect.y -= self.vel * math.cos (math.radians(self.angle))

                    # Rotate angle
                    if (key [self.left]) :
                        self.angle += 3

                    if (key [self.right]) :
                        self.angle -= 3
                        
                # Moving down, same concept but decelration/moving back
                if (key [self.down]) :

                    if (wall == True) :
                        self.vel = 0.1

                    else:
                        self.vel -= 0.05

                    if (self.vel <= -3) :
                        self.vel = -3

                    self.car_rect.x -= self.vel * math.sin (math.radians(self.angle))
                    self.car_rect.y -= self.vel * math.cos (math.radians(self.angle))

                    if (key [self.left]) :
                        self.angle += 3

                    if (key [self.right]) :
                        self.angle -= 3

                # When neither keys pressed, decelerate back to zero velocity
                if ((not key [self.up]) and (not key [self.down])) :


                    if (self.vel >= 0) :
                        self.vel -= 0.05

                        if (self.vel <= 0) :
                            self.vel = 0

                    if (self.vel <= 0) :
                        self.vel += 0.05

                        if (self.vel >= 0) :
                            self.vel = 0

                    self.car_rect.x -= self.vel * math.sin (math.radians(self.angle))
                    self.car_rect.y -= self.vel * math.cos (math.radians(self.angle))

            # Update angle back to 360
            if ((self.angle == 360) or (self.angle == -360)) :
                self.angle = 0

        # Check if lap was complete
        self.lap_check = tracker.lap (self.car_rect, self.vel, self.angle)

        if (self.lap_check == True) :
            self.lap_count += 1
