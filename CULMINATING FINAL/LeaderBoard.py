# Program Name: Leaderboard Functions
# Programmer: Shrish Luitel, Kshitij Kapoor, Eishan Ashraf
# Date of Completion: 6/16/2023
# Description: These functions take in the times of the single player mode,
# and read from the text file. Afterwards, it recursivly sorts the values
# from best to worse and returns it back to the game. 

# Merge sorting algortithm that lists the time values from worse to best
def merge(listt):

    #Break into two parts
    if (len(listt) > 1):
        n = len(listt) // 2
        left = listt[:n]
        right = listt[n:]

        merge(left)  # breaks list into sub lists holding one element each
        merge(right)

        i = 0
        j = 0
        k = 0

        # takes place every time to sort sub lists,
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                listt[k] = right[j]
                j += 1

            else:
                listt[k] = left[i]
                i += 1

            k += 1

        while i < len(left):
            listt[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            listt[k] = right[j]
            j += 1
            k += 1

    return listt

# Reads time value from file and updates to list
# Sorts list from best time to worse
def leaderboard(track_number):

    # Updating for map 1
    if (track_number == 1):
        # Read file
        list_scores1 = []
        file = open ("time_scores1.txt", "r")

        line = file.readline()

        # Read through each line and append
        while (line):
                
            list_scores1.append (float(line))
            line = file.readline()

        file.close()

        # Sorting and returning
        map1sort = merge(list_scores1)
        return map1sort
        
    # Updating for map 2
    else:
        list_scores2 = []
        file = open ("time_scores2.txt", "r")

        line = file.readline()

        while (line):
                
            list_scores2.append (float(line))
            line = file.readline()

        file.close()

        map2sort = merge(list_scores2)
        return map2sort
        
