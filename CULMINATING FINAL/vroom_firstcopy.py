# Program Name: VroomVroomGame
# Programmer: Shrish Luitel, Kshitij Kapoor, Eishan Ashraf
# Date of Completion: 6/16/2023
# Description: This is the main game execution area, where
# all the classes are processed. It receives inputs from the home screen
# and updates the variables accordingly. Subsequently, it distributes the
# updated variables to each class and runs the entire game.

# Imports
import pygame
import math
import random
from pygame import mixer
import time

from LuckyBlock import *
from BananaClass import *
from PlayerClass import *
from LeaderBoard import *

#Background and FPS
BLACK = (0, 0, 0)
FPS = 60

# Car 1:
car = pygame.image.load('green_car.png')
car = pygame.transform.scale(car, (20, 30))
car_rect = car.get_rect()
car_rect.center = (45, 380)

# Car 2:
car_two = pygame.image.load('red_car.png')
car_two = pygame.transform.scale(car_two, (20, 30))
car_two_rect = car_two.get_rect()
car_two_rect.center = (90, 380)

#Banana and Block Image
main_banana = pygame.image.load('banana.png')
main_banana = pygame.transform.scale(main_banana, (35, 35))

main_block = pygame.image.load("luckyblock_p.png")
main_block = pygame.transform.scale(main_block, (50, 50))

# Draw the updated sprites
def draw_window():
    # Blit the track and first car
    WINDOW.fill(BLACK)

    WINDOW.blit(current_track, (0, 0))

    rotated_car = pygame.transform.rotate(car, car1.angle)
    WINDOW.blit(rotated_car, (car1.car_rect.x, car1.car_rect.y))

    # Blit second car, existing bananas, and lucky block
    if (amountofplayer == 2):
        rotated_car_2 = pygame.transform.rotate(car_two, car2.angle)
        WINDOW.blit(rotated_car_2, (car2.car_rect.x, car2.car_rect.y))

        WINDOW.blit(main_block, (tracker.luckyblock1.x, tracker.luckyblock1.y))
        WINDOW.blit(main_block, (tracker.luckyblock2.x, tracker.luckyblock2.y))
        WINDOW.blit(main_block, (tracker.luckyblock3.x, tracker.luckyblock3.y))

        # For loop through each banana
        for bans_1 in (car1.banana_list):
            WINDOW.blit(main_banana, (bans_1.x, bans_1.y))

        for bans_2 in (car2.banana_list):
            WINDOW.blit(main_banana, (bans_2.x, bans_2.y))


# Main game
def run_game(track_number, players, player_one, player_two):
    #Globalilize Variables
    global car1, car2, current_track, tracker, amountofplayer, WINDOW, best_times, current_time, winner

    # Create the game window
    WIDTH, HEIGHT = 800, 800
    winner = " "

    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Car Game")

    # Check the number of players in lobby
    amountofplayer = players

    pygame.init()

    # Set clock for pygame and start game
    clock = pygame.time.Clock()
    run = True

    # Keybinds
    up = pygame.K_UP
    left = pygame.K_LEFT
    right = pygame.K_RIGHT
    down = pygame.K_DOWN
    shift = pygame.K_p

    up2 = pygame.K_w
    left2 = pygame.K_a
    right2 = pygame.K_d
    down2 = pygame.K_s
    shift2 = pygame.K_LSHIFT

    # Player Names
    player1_name = player_one
    player2_name = player_two

    # Car Objects
    car1 = Player(up, down, left, right, shift, car_rect, player1_name)
    car2 = Player(up2, down2, left2, right2, shift2, car_two_rect, player2_name)

    # Winner Variables:
    player_one_win = False
    player_two_win = False

    # Call the RaceTrack class, and the map that is selected is based off homescreen
    tracker = RaceTrack(track_number)
    current_track = tracker.get_map(car, car_two, car_rect, car_two_rect, car1, car2)

    # Sound Audio
    mixer.init()

    pygame.time.delay(100)

    # Coundown Music
    mixer.music.load('321.mp3')
    print("music started playing....")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # Freeze game as countdown playing
    while mixer.music.get_busy():
        draw_window()
        pygame.display.flip()

    # Fade out to main music
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load('blossom.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play(100)
    pygame.mixer.music.rewind

    # Start the timer
    start_time = time.time()
    font = pygame.font.Font("freesansbold.ttf", 14)
    time_font = pygame.font.Font("freesansbold.ttf", 20)

    # Music for banana slip
    slip_music = pygame.mixer.Sound("skid.mp3")
    slip_music.set_volume(0.2)

    while (run):
        clock.tick(FPS)

        # Running pygame game
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

        # TWO PLAYER
        if (amountofplayer == 2):
            # Get keys
            key1 = pygame.key.get_pressed()
            key2 = pygame.key.get_pressed()

            # Check for power ups
            draw_window()
            car1.power_up(key1, tracker)
            car2.power_up(key2, tracker)

            # Loop through every oposing banana of current car
            for bans2 in car2.banana_list:

                # If collision, start music and spin player for given time
                if (car1.car_rect.colliderect(bans2)):
                    slip_music.play(fade_ms=1)

                    for i in range(40):
                        car1.angle += 15
                        draw_window()
                        pygame.display.flip()

                        bans2.x = 1000
                        bans2.y = 1000

            # Same for opposing banana
            for bans1 in car1.banana_list:

                if car2.car_rect.colliderect(bans1):
                    slip_music.play(fade_ms=1)

                    for i in range(40):
                        car2.angle += 15
                        draw_window()
                        pygame.display.flip()

                        bans1.x = 1000
                        bans1.y = 1000

            # Update the player move
            car1.player_move(key1, tracker)
            car2.player_move(key2, tracker)

            # Lap count output string
            car_one_lap = str("|" + car1.playername + " Lap: " +
                              str(car1.lap_count) + " || Current Power: "
                              + car1.current_power + "|" + " Press P")
            
            car_two_lap = str("|" + car2.playername + " Lap: " +
                              str(car2.lap_count) + " || Current Power: " +
                              car2.current_power + "|" + " Press L_SHIFT")

            car_one_text = font.render(car_one_lap, True, 'white')
            car_two_text = font.render(car_two_lap, True, 'white')

            # Display the time and current power based off map
            if track_number == 1:
                WINDOW.blit(car_one_text, (150, 160))
                WINDOW.blit(car_two_text, (150, 630))

            else:
                WINDOW.blit(car_one_text, (200, 580))
                WINDOW.blit(car_two_text, (200, 660))

            # Check for winner
            if (car1.lap_count == 5):
                round_time = round(current_time, 2)
                score_keep_time = (car1.playername + ": " + str(round_time))
                player_one_win = True
                run = False

            if (car2.lap_count == 5):
                round_time = round(current_time, 2)
                score_keep_time = (car1.playername + ": " + str(round_time))
                player_two_win = True
                run = False

        # SINGLE PLAYER
        else:
            # Get input, and move player
            draw_window()
            key1 = pygame.key.get_pressed()
            car1.player_move(key1, tracker)

            # Output text
            single_car_one_lap = str(car1.playername + " Lap: " + str(car1.lap_count))
            single_car_one_text = font.render(single_car_one_lap, True, 'white')

            # Check which map to output too
            if (track_number == 2):
                WINDOW.blit(single_car_one_text, (300, 580))

            else:
                WINDOW.blit(single_car_one_text, (360, 160))

            # End game when player reaches the laps
            if (car1.lap_count == 3):
                output_time = "\n" + (str(current_round))
                run = False

        # Get current time
        current_time = time.time() - start_time
        current_round = round(current_time, 2)
        stringtime = str(current_round)
        time_text = time_font.render(stringtime, True, 'white')

        # Time output location based off map
        if track_number == 1:
            WINDOW.blit(time_text, (385, 390))

        else:
            WINDOW.blit(time_text, (920, 70))

        # Update screen
        pygame.display.flip()

    # End game
    pygame.quit()

    # Display Winner for 2 Player Mode
    if amountofplayer == 2:
        if player_one_win:
            winner = player1_name
            print("YES")
            print(player1_name)
        else:
            winner = player2_name
    print(winner)
    print("hi")

    # Update best times for one player mode
    if amountofplayer == 1:
        if track_number == 1:
            # Write to file of times for map 1
            file = open("time_scores1.txt", "a")
            file.write(output_time)
            file.close()
            leaderboard(track_number)

        else:
            # Write to file of times for map 2
            file = open("time_scores2.txt", "a")
            file.write(output_time)
            file.close()
            leaderboard(track_number)

        # Obtain best times
        best_times = leaderboard(track_number)
        print(best_times)


