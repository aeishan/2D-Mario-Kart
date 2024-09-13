# Program Name: Main Home Screen
# Programmer: Shrish Luitel, Kshitij Kapoor, Eishan Ashraf
# Date of Completion: 6/16/2023
# Description: This is where the player gets to decide which game mode they
# want to play. They have the option to play between single player or local
# multiplayer. Afterwards they have the option between two maps, and the ability
# to put in their name. After submitting, the player will be relocated to the
# main game. 

# Imports
import tkinter
import vroom_firstcopy

# Single Player Map 1
def start_single_easy():
    #Destroy window, set variables to according mode
    #Call the game function, and winner afterwards
    window.destroy()
    amountofplayer = 1
    track_number = 1
    vroom_firstcopy.run_game(track_number, amountofplayer,
                             player_one_name, player_two_name)
    create_winner_page(amountofplayer, track_number)


# Multiplayer Map 1
def start_multi_easy():
    #Destroy window, set variables to according mode
    #Call the game function, and winner afterwards
    window.destroy()
    amountofplayer = 2
    track_number = 1
    vroom_firstcopy.run_game(track_number, amountofplayer,
                             player_one_name, player_two_name)
    create_winner_page(amountofplayer, track_number)

# Single Player Map 2
def start_single_hard():
    #Destroy window, set variables to according mode
    #Call the game function, and winner afterwards
    window.destroy()
    amountofplayer = 1
    track_number = 2
    vroom_firstcopy.run_game(track_number, amountofplayer,
                             player_one_name, player_two_name)
    create_winner_page(amountofplayer, track_number)

# Multiplayer Map 2
def start_multi_hard():
    #Destroy window, set variables to according mode
    #Call the game function, and winner afterwards
    window.destroy()
    amountofplayer = 2
    track_number = 2
    vroom_firstcopy.run_game(track_number, amountofplayer,
                             player_one_name, player_two_name)
    create_winner_page(amountofplayer, track_number)

# Select to single mode
def single_select():
    single = True
    create_select_page(single)

# Set off single
def double_select():
    single = False
    create_select_page(single)

# Submit in name and create label
def name_submit():
    player_one_name = player_one_inp.get()
    try:
        player_two_name = player_two_inp.get()
    except:
        pass
    submit_label = tkinter.Label(select_page, bg="purple4", text="Thank You")
    submit_label.place(x=400, y=203, anchor="center")

# Home Screen
def create_home():
    global home_page

    # Background
    home_page = tkinter.Frame(window, bg="purple4", height=800, width=800)
    home_page.place(x=0, y=0)

    # Title
    name_label = tkinter.Label(home_page, text="VROOM VROOM\n CAR RACER",
                               bg="purple4", font=('roboto', 48, "bold"))
    name_label.place(x=400, y=300, anchor="center")

    # All the buttons
    single_but = tkinter.Button(home_page, text="SINGLE PLAYER",
                                font=('roboto', 24, 'bold'), width=30,
                                bg='yellow', command=single_select)
    single_but.place(x=400, y=450, anchor="center")

    multi_but = tkinter.Button(home_page, text="LOCAL MULTIPLAYER",
                               font=('roboto', 24, 'bold'), width=30,
                               bg='yellow', command=double_select)
    multi_but.place(x=400, y=520, anchor="center")


# Select Page
def create_select_page(single):
    global player_one_inp
    global player_two_inp
    global player_one_name
    global player_two_name
    global select_page

    # Destroy first page, and open current
    home_page.destroy()
    player_one_name = "Player One"
    player_two_name = "Player Two"

    # Scale page
    select_page = tkinter.Frame(window, bg="purple4", height=800, width=800)
    select_page.place(x=0, y=0)

    # Submit button for name
    submit_name = tkinter.Button(select_page, text="Submit",
                                 command=name_submit)
    
    submit_name.place(x=400, y=180, anchor="center")

    # Map select buttons
    select_map_label = tkinter.Label(select_page, text="SELECT MAP",
                                     bg="purple4", font=('roboto', 40, "bold"))
    select_map_label.place(x=400, y=250, anchor="center")

    # Select buttons for single player
    # Set the location of button, and load in game accordingly
    if (single == True):
        name_inp_label = tkinter.Label(select_page, text="Player Name:",
                                       bg="purple4", font=('roboto', 25,
                                                           "bold"))
        
        name_inp_label.place(x=400, y=100, anchor="center")
        
        player_one_inp = tkinter.Entry(select_page, justify="center", width=40)
        
        player_one_inp.place(x=400, y=150, anchor="center")
        
        map_one_button = tkinter.Button(select_page, text="PINEAPPLE GREEN",
                                        width=40, height=18, bg="light green",
                                        command=start_single_easy)
        
        map_one_button.place(x=200, y=480, anchor="center")
        
        map_two_button = tkinter.Button(select_page, text="SPACE JAM",
                                        width=40, height=18, bg="red",
                                        command=start_single_hard)
        
        map_two_button.place(x=600, y=480, anchor="center")

    # Select buttons for Multiplayer
    # Set the location of button, and load in game accordingly
    else:
        name_inp_label = tkinter.Label(select_page, text="Player One Name:",
                                       bg="purple4", font=('roboto', 25,
                                                           "bold"))
        
        name_inp_label.place(x=200, y=100, anchor="center")
        
        player_one_inp = tkinter.Entry(select_page,
                                       justify="center", width=40)
        
        player_one_inp.place(x=200, y=150, anchor="center")
        name_inp_label_two = tkinter.Label(select_page,
                                           text="Player Two Name:",
                                           bg="purple4",
                                           font=('roboto', 25, "bold"))
        
        name_inp_label_two.place(x=600, y=100, anchor="center")
        player_two_inp = tkinter.Entry(select_page, justify="center", width=40)
        player_two_inp.place(x=600, y=150, anchor="center")
        
        map_one_button = tkinter.Button(select_page, text="PINEAPPLE GREEN",
                                        width=40, height=18, bg="light green",
                                        command=start_multi_easy)
        
        map_one_button.place(x=200, y=480, anchor="center")
        
        map_two_button = tkinter.Button(select_page, text="SPACE JAM",
                                        width=40, height=18, bg="red",
                                        command=start_multi_hard)
        
        map_two_button.place(x=600, y=480, anchor="center")

# Winning Page/Restart
def create_winner_page(amountofplayer, track_number):
    global window_two

    # Create new window
    window_two = tkinter.Tk()
    window_two.title("Winner")
    window_two.geometry("600x600")
    winner_frame = tkinter.Frame(window_two, bg="purple4", height=800, width=800)
    winner_frame.place(x=0, y=0)

    # Check which map
    if (track_number == 1):
        track_name = "PINEAPPLE GREEN"
    else:
        track_name = "SPACE JAM"

    # Check 1 Player for Best times
    # Update for the best 5 records ever played on the computer
    # Upload to window
    if (amountofplayer == 1):
        leader_label = tkinter.Label(winner_frame, text="BEST TIMES",
                                     font=('roboto', 20, "bold"), bg="purple4")
        
        leader_label.place(x=300, y=150, anchor="center")
        for i in range(5):
            board_label = tkinter.Label(winner_frame,
                                        text=vroom_firstcopy.best_times[i],
                                        font=('roboto', 15, "bold"), bg="purple4")
            
            board_label.place(x=300, y=200+25*i, anchor="center")
            
        time_label = tkinter.Label(winner_frame, bg="purple4",
                                   text="Your time was:" + str(round(vroom_firstcopy.current_time, 2)),
                                   font=('roboto', 15, "bold"))
        
        time_label.place(x=300, y=340, anchor="center")

    # Check 2 Player for who is winner
    # Update winner, and ask to play again
    else:
        winner_label = tkinter.Label(winner_frame,
                                     text="THE WINNER OF THE RACE IS",
                                     font=('roboto', 30, "bold"), bg="purple4")
        
        winner_label.place(x=300, y=250, anchor="center")
        
        winner_label = tkinter.Label(winner_frame, text=vroom_firstcopy.winner,
                                     font=('roboto', 30, "bold"), bg="purple4")
        
        winner_label.place(x=300, y=300, anchor="center")
        
    again = tkinter.Button(winner_frame, text="PLAY AGAIN",
                           bg="yellow", font=('roboto', 30, "bold"),
                           command=play_again)
    
    again.place(x=300, y=400, anchor="center")

# Destroy window, and go back to home
def play_again():
    window_two.destroy()
    main()

# Main function
def main():
    global window

    #Create window, and create home screen
    window = tkinter.Tk()
    window.title("VROOM VROOM CAR RACER")
    window.geometry("800x800")

    create_home()

    window.mainloop()

# Call main
main()
