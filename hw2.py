import data

# Write your functions for each part in the space below.
# Part 1
def create_rectangle(first : data.Point, second : data.Point)->data.Rectangle:
    #this if statement checks if the values in point for x and y are the same. If this is true...
    #then the function will flip the y values of the two different point parameters
    if first.x == first.y or second.x == second.y:
        temp = first.y
        first.y = second.y
        second.y = temp
    #creates two objects with the parameters so that the new values can be returned if changed
    top_left = data.Point(first.x,first.y)
    bottom_right = data.Point(second.x,second.y)
    return data.Rectangle(top_left,bottom_right)

# Part 2
def shorter_duration_than(first : data.Duration, second : data.Duration)->bool:
    #first if checks if the minutes of the first duration is shorter, if so returns true
    if first.minutes < second.minutes:
        return True
    #elif checks if the minutes are the same, and then if that is true checks if the seconds...
    #of the first duration is shorter, if so returns true
    elif first.minutes == second.minutes and first.seconds < second.seconds:
        return True
    #returns False for any case that does not include the two above
    else:
        return False
# Part 3
def songs_shorter_than(songs : list[data.Song], length : data.Duration)->list[data.Song]:
    #def a value to use to check songs durations
    minutes = length.minutes
    seconds = length.seconds
    #empty list for return
    shorter_songs = []
    #for each song in list run function
    for i in range(len(songs)):
        #checks if song duration's minutes is less than minute length, or if it is equal, checks if the seconds is less. If so...
        #adds that song to the list of songs shorter than the duration
        if (songs[i].duration.minutes < minutes) or (songs[i].duration.minutes == minutes and songs[i].duration.seconds < seconds):
            shorter_songs.append(songs[i])
    return shorter_songs
# Part 4
def running_time(songs : list[data.Song], playlist : list[int])->data.Duration:
    #creates a counter method so that minutes and seconds from each song can be added up
    minutes = 0
    seconds = 0
    #for each int value in playlist, it will pull the minutes and seconds and add them up to the total
    for i in playlist:
        minutes += songs[i].duration.minutes
        seconds += songs[i].duration.seconds
        #below, makes sure seconds is not greater than 60, and if it is, adds another minute to total
        minutes += seconds // 60
        seconds %= 60
    return data.Duration(minutes,seconds)
# Part 5
def validate_route(city_links : list[list[str]], route : list[str])->bool:
    #empty route or route with only one stop return true because no links
    if len(route) <= 1:
        return True
    #for loop checks if the two cities in route have a link going either way, loop checks for
    #all instances of it, if any do not exist it returns false
    for i in range(len(route)-1):
        city1, city2 = route[i],route[i+1]
        if [city1,city2] not in city_links and [city2,city1] not in city_links:
            return False
    return True
# Part 6
def longest_repetition(list : list[int])->int or None:
    #checks if list is empty
    if len(list) < 1:
        return None
    #creates objects, one for longest length so far, one for the index for the first term of longest length
    longest_rep = 1
    longest_rep_1st_ind = 0
    #these two objects are for the current count of the length of repetition and the index that it starts at
    current_length = 1
    current_index = 0
    #for loop to run through the list
    for i in range(len(list)-1):
        #checks if the first index is equal to the second index, if so adds to the current length
        if list[i] == list[i+1]:
            current_length +=1
        #if the index is not the same checks if the current length is longer then the longest, if this is the case...
        #then the longest length changes, and the longest starting index changes to the first term for that list...
        else:
            if current_length > longest_rep:
                longest_rep = current_length
                longest_rep_1st_ind = current_index
            #resets the current length and current index for next check
            current_length = 1
            current_index = i + 1
    #runs as a final check for the last sequence that exists in the list
    if current_length > longest_rep:
        longest_rep_1st_ind = current_index
    #returns the index of the longest list
    return longest_rep_1st_ind