
def open_list():
    pass

def find_files():
    is_last_directory = False
    still_adding = "yes"

    while is_last_directory == False:
        music_dir = input("Where is your music directory located?\n")
        os.chdir(music_dir)
        check_dir = os.getcwd()
        print("Currently looking inside {}".format(check_dir))
        for song_name in glob.iglob(".\**\*.mp3", recursive=True):
            print(song_name)
        while still_adding != "no" or "n":
            still_adding = input("Do you have any other directories you'd like to add? ")
            if still_adding == "yes" or still_adding == "y":
                break
            elif still_adding == "no" or still_adding == "n":
                is_last_directory = True
                break
            else:
                print("Please try that again. ")
                continue



def get_file_metadata():
    # optional
    pass


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
    import os, glob


    find_files()
