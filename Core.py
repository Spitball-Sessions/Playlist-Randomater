# I'd like to create a class for these?
def create_csv(list):
    '''
    This creates a new CSV file with the name Randomater_Main.csv and is where all the songs will be stored for future use.

    :param list: The list of songs and file locations.
    '''
    with open("Randomater_Main.csv","w",encoding='utf-8') as csvfile:
        songs = csv.writer(csvfile, delimiter = "\n")
        songs.writerows([song_list])
    print("Files added...")

def open_csv(song_list):
    '''
    This opens the Randomizer_Main.csv and converts it back to a useable list
    :param song_list: imports empty song list
    :return: full song list
    '''
    with open("Randomater_Main.csv","r", encoding = "utf8") as csvfile:
        filereader = csv.reader(csvfile)
        for row in filereader:
            song_list.append(row)
    return song_list


def find_files():
    '''
    This function creates a list of song files and their locations.
    Can search up to 3 levels inside a music directory (in case music is stored by musician & album)
    If the user has multiple music directories, it will then prompt them to add another one.
    :return: returns the list of song files and their locations, as well as all directories the user asked to check.
    '''
    # method initialization stuff:
    is_last_directory = False
    still_adding = "yes"
    song_list, info_list,music_dir_list = ([] for i in range(3))

    #finds songs and adds them to list
    while is_last_directory == False:
        music_dir = input("Where is your music directory located?\n")
        os.chdir(music_dir)
        check_dir = os.getcwd()
        print("Currently looking inside {}".format(check_dir))
        for song_name in glob.iglob(check_dir + "\**\*.mp3", recursive=True):
            song_list.append(song_name)

           ''' Maybe this is the solution if I can weed out songs that aren't Google supported:
            **info_list.append(mutagen.File(song_name))** '''

        print(info_list)

        # checks whether user wants to add more directories, otherwise builds and exports list
        while still_adding != "no" or "n":
            still_adding = input("Do you have any other directories you'd like to add? ").lower().strip()
            if still_adding == "yes" or still_adding == "y":
                music_dir_list.append(music_dir)
                break
            elif still_adding == "no" or still_adding == "n":
                final_song_list = [i + "\n" for i in song_list]
                if music_dir_list == []:
                    return final_song_list, music_dir
                else:
                    music_dir_list.append(music_dir)
                    return final_song_list,music_dir_list
            else:
                print("Please try that again. ")
                continue


def get_abs_path_files():
    pass

'''
def get_file_metadata(csv_dir):
    # This doesn't work right now.  I'm not sure I can figure out why it's breaking, so I don't know if I can fix it.

    #1 import the CSV as a itemized list
    os.chdir(csv_dir)
    title_dict = []
    with open("Randomater_Main.csv","r", encoding = "utf8") as csvfile:
        filereader = csv.reader(csvfile, delimiter = "\n")
        for row in filereader:
            title_dict.append(row)


    2 Then feed items from list back to mutagen - this is the problem part.  
    Mutagen can only use the file name once pointed to the directory.  Not sure how to strip the strings properly while still keeping them
    

    for items in title_dict:
        mutagen.mp3.MPEGInfo(items)
    

    #3 Use mutagen to find song titles

    #4 Save titles and file name to dictionary.

'''


def pick_random_set_of_songs(csv_dir):
    '''
    Creates a random playlist of user-requested # of songs.
    At some point, it would be nice to do this by playlist time length
    :return: randomized playlist
    '''

    # method initialization stuff:
    os.chdir(csv_dir)
    song_list, playlist, playlist2 = ([] for i in range(3))

    # creates a usable list.
    song_list = open_csv(song_list)

    playlist_length = input("How many songs would you like in your playlist? ")

    # There has to be a better solution for this.
    # Right now, this creates the playlist as an array, then converts the array to a list of strings, then removes the \n from each string in the list.
    for i in range(int(playlist_length)):
        playlist.append(random.choice(song_list))
    for i in range(int(playlist_length)):
        playlist2.append(playlist[i-1][0])
    playlist.clear()
    for i in range(int(playlist_length)):
        playlist.append(playlist2[i].rstrip())


    print(playlist)
    return playlist

def make_playlist():

    pass


def save_playlist():
    pass


def move_songs_in_playlist():
    # copy all the songs on a playlist to an "upload" folder
    pass


def print_list():
    pass


if __name__ == "__main__":
    # initialization stuff:
    import os, glob, csv, random
    import mutagen.mp3, mutagen.id3
    acceptable_responses = ["yes","y","no","n"]


    first_time = input("Is this your first time using Playlist Randomater? ").lower().strip()
    while first_time != False:
        # saved_override flips to True once there's an existing Randomater_Main file and the program knows where it is.
        saved_Override = False
        if first_time in acceptable_responses:
            # if this is the user's first time, or if they lost their Randomater_Main file, this builds it.
            while first_time == "yes" or first_time == "y":

                # csv_dir is where the Randomater file is stored
                csv_dir = os.getcwd()
                song_list, root_dir = find_files()
                print("Adding to list...")
                os.chdir(csv_dir)
                print(root_dir)
                create_csv(song_list)
                first_time = "no"
                saved_Override = True
                break
            # This verifies whether they have a Randomater Main and where it is.  If they do, flips saved_override to True, and kicks up to next function.
            while first_time == "no" or first_time == "n":
                if saved_Override == False:
                    saved = input("Did you save your previous Randomater_Main file? ").lower().strip()
                    if saved == "no" or saved == "n":
                        first_time = "yes"
                        break
                    if saved == "yes" or saved == "y":
                        csv_dir = input("Where did you save the Randomater_Main file? ")
                        saved_Override = True
                        continue
                # Once there's a file, this builds the playlists and does all the rest of that.
                elif saved_Override == True:
                    # get_file_metadata(csv_dir)
                    my_playlist = pick_random_set_of_songs(csv_dir)
                    quit("That's all folks")


            else:
                first_time = input("What was that? ")
