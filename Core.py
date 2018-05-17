
def create_csv(list):
    with open("Randomater_Main.csv","w",encoding='utf-8') as csvfile:
        songs = csv.writer(csvfile, delimiter = "\n")
        songs.writerows([song_list])
    print("Files added...")


def find_files():
    is_last_directory = False
    still_adding = "yes"
    song_list = []
    music_dir_list = []

    while is_last_directory == False:
        music_dir = input("Where is your music directory located?\n")
        os.chdir(music_dir)
        check_dir = os.getcwd()
        print("Currently looking inside {}".format(check_dir))
        for song_name in glob.iglob(check_dir + "\**\*.mp3", recursive=True):
            song_list.append(song_name)

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

def get_file_metadata(csv_dir):
    # This doesn't work right now.  I'm not sure I can figure out why it's breaking, so I don't know if I can fix it.
    os.chdir(csv_dir)
    title_dict = []
    with open("Randomater_Main.csv","r", encoding = "utf8") as csvfile:
        filereader = csv.reader(csvfile, delimiter = "\n")




def pick_random_set_of_songs():
    # possibly use multiple criteria
    pass


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
    import os, glob, csv
    import mutagen.mp3, mutagen.id3
    acceptable_responses = ["yes","y","no","n"]


    first_time = input("Is this your first time using Playlist Randomater? ").lower().strip()
    while first_time != False:
        saved_Override = False
        if first_time in acceptable_responses:
            while first_time == "yes" or first_time == "y":

                csv_dir = os.getcwd()
                song_list, root_dir = find_files()
                print("Adding to list...")
                os.chdir(csv_dir)
                print(root_dir)
                create_csv(song_list)
                first_time = "no"
                saved_Override = True
                break

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
                elif saved_Override == True:
                    # get_file_metadata(csv_dir)



            else:
                first_time = input("What was that? ")
