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
        **info_list.append(mutagen.File(song_name))** 
        print(info_list)'''

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

    # method initialization:
    os.chdir(csv_dir)
    song_list, playlist, playlist2 = ([] for i in range(3))

    song_list = open_csv(song_list) # Creates a mem-stored list from the CSV file.

    playlist_length = input("How many songs would you like in your playlist? ")

    # This creates the playlist as an array, then converts the array to a list of strings, then removes the \n from each string in the list.
    # There's definitely a better solution for this.
    while playlist2 == []:
        for songs in range(int(playlist_length)):
            playlist.append(random.choice(song_list))
        for songs in range(int(playlist_length)):
            playlist2.append(playlist[songs][0])
        playlist.clear()
        for songs in range(int(playlist_length)):
            playlist.append(playlist2[songs].rstrip())
        song_names_in_playlist(playlist)

    return playlist

def song_names_in_playlist(playlist):
    '''
    This tells the user what songs are going to be put onto the playlist.
    :param playlist: This is the randomly generated playlist
    :return: returns no value.
    '''
    # Method Initialization:
    song_id3, song_names = ([] for i in range(2))

    for songs in range(len(playlist)):
        # Gets all the tags for a song and adds them to a dict - 1 dict/song
        song_id3.append(mutagen.File(playlist[songs]).tags)
        # If the song has a title, adds it.  Otherwise, adds the song's filename.  At some point, I should regex to rem: \\'s
        try:
            v = song_id3[songs].get("TIT2")
            if v == None:
                song_names.append(str(playlist[songs]).lstrip("f:\\*\\*\\"))
            else:
                song_names.append(str(song_id3[songs].get("TIT2")))
        except AttributeError:
            song_names.append(playlist[songs])

    print("This playlist will have the following songs:")
    for x in range(len(song_names)):
        print(str(x + 1) + " " + str(song_names[x]))

    ''' I would, at some point, like this to let the user remove songs from the proposed playlist and have new ones add
        at random.  For now, this will have to suffice.'''

    return

def folder_empty(folder):
    '''
    This clears the "To Copy" folder so that new songs can be added.
    :param folder: currently, the "To Copy" folder.  Eventually, may be user definable.
    :return: no variable returned.
    '''
    song_del = []  # initialization
    for i in glob.iglob(folder + "\*.mp3", recursive=True):
        song_del.append(i)
    for i in glob.iglob(folder + "\*.m3u", recursive=True):
        song_del.append(i)
    for i in song_del:
        os.remove(i)
    return

def move_songs_to_folder(playlist):
    '''
    Copies songs from their original location to the "To Copy" file inside program folder to ensure they're easy to copy.
    :param playlist: This is the playlist which we want to copy the files of.
    :return: No variable returned
    '''

    copy_folder = make_playlist_directory()
    x = input("Would you like to empty the existing folder? ").lower().rstrip()
    if x == "y" or x == "yes":
        folder_empty(copy_folder)
    else:
        archive()
        folder_empty(copy_folder) # Relocate inside Archive command?
    for i in range(len(playlist)):
        shutil.copy2(playlist[i],copy_folder)
    os.chdir(copy_folder)
    save_playlist()

def save_playlist():
    '''
    Takes files in the "To Copy" folder, and adds them to the .m3u folder by their relative path.
    :return:
    '''
    m3u = []
    for i in glob.iglob(os.getcwd() + "\*.mp3", recursive=True):
        m3u.append(".\\" + str(i.lstrip("E:\\Programming\\Playlist Randomator\\Playlist Folder")))
    a = input("What would you like to call your playlist? ")
    if a == "":
        playlist_name = "playlist.m3u"
    else:
        playlist_name = (a + ".m3u")
    with open(playlist_name,"w",encoding='utf-8') as m3u_file:
        for i in range(len(m3u)):
            m3u_file.write(m3u[i]+"\n")


    print("Playlist saved...")

def archive():
    '''
    This will copy files already in the "To Copy" folder to the "Archive" folder, so the user may create multiple playlists.
    :return: No Variable Returned
    '''
    cwd = os.getcwd()
    archive_folder = (cwd + "\\" + "Archive")
    if os.path.exists(archive_folder):
        os.chdir(archive_folder)
    else:
        os.makedirs(archive_folder)
        os.chdir(archive_folder)
    for i in glob.iglob(cwd + "\*.mp3", recursive=True):
        shutil.copy2(i, archive_folder)
    for i in glob.iglob(cwd + "\*.m3u", recursive=True):
        shutil.copy2(i, archive_folder)
    os.chdir(cwd)
    return

def make_playlist_directory():
    '''
    Makes a folder to move the playlist files to.
    :return: folder path
    '''
    cwd = os.getcwd()
    m3u_folder = (cwd + "\\" + "To Copy")
    if os.path.exists(m3u_folder):
        os.chdir(m3u_folder)
    else:
        os.makedirs(m3u_folder)
        os.chdir(m3u_folder)
    return m3u_folder


if __name__ == "__main__":
    # initialization stuff:
    import os, glob, csv, random,shutil
    import mutagen.mp3, mutagen.id3

    acceptable_responses = ["yes","y","no","n"]

    first_time = input("Is this your first time using Playlist Randomater? ").lower().strip()

    while first_time:
        # saved_override flips to True once there's an existing Randomater_Main file and the program knows where it is.
        saved_Override = False
        if first_time in acceptable_responses:
            # if this is the user's first time, or if they lost their Randomater_Main file, this builds it.
            while first_time == "yes" or first_time == "y":
                csv_dir = os.getcwd() # this ensures everything goes back into the Randomater folder
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
                if not saved_Override:
                    saved = input("Did you save your previous Randomater_Main file? ").lower().strip()
                    if saved == "no" or saved == "n":
                        first_time = "yes"
                        break
                    if saved == "yes" or saved == "y":
                            csv_dir = input("Where did you save the Randomater_Main file? ")
                            if os.path.exists(csv_dir +"\\" + "Randomater_Main.csv") == True:
                                saved_Override = True
                                continue
                            else:
                                print("Not Found.")
                                continue
                # Once there's a file, this builds the playlists and does all the rest of that.
                elif saved_Override:
                    my_playlist = pick_random_set_of_songs(csv_dir)
                    move_songs_to_folder(my_playlist)


                    quit("You Ain't Nothing")


            else:
                first_time = input("What was that? ")
