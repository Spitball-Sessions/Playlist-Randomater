
def create_csv(list):
    with open("Song List.csv","w",encoding='utf-8') as csvfile:
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

def get_file_metadata():




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

    init_cwd = os.getcwd()
    song_list,root_dir = find_files()
    print("Adding to list...")
    os.chdir(init_cwd)
    print(root_dir)
    create_csv(song_list)

