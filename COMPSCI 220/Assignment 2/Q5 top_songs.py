"""
Pinghang Fan,
top_Songs.py
This is a program that sorts a mp3 player in the following order: run length, name, composer.
"""
import sys

def collect_songs(len_list, total_list, seperator):
    """Searching for matching running length in the total list"""
    """Adding them to the corresponding runing time in the len_list, and return the reverse"""
    for song in total_list:
        len = int(song[song.rfind(seperator)+1:].rstrip("\n"))
        if len in len_list:
            index = len_list.index(len)
            len_list[index] = song

    """Return reverse of len_list in order to get largest to smallest"""
    return len_list.reverse()

def check_dup(listlist):
    """Check if given list contains any duplicates"""
    if len(listlist) == len(set(listlist)):
        return False
    else:
        return True

def sort_by_name_compo(n_list, seperator):
    temp_list = list()
    count = 0
    index = 0
    while count < len(n_list)-1:
        temp_list = list()
        inner_count = 0
        inner_index = index
        song_len = int(n_list[index][n_list[index].rfind(seperator)+1:]) #run time of current song
        next_song_len = int(n_list[index+1][n_list[index+1].rfind(seperator)+1:]) # run time of next song

        """While running times of the next song is the same, add to a temporal list"""
        """inner_count counts the number of element being sorted"""
        while song_len == next_song_len and inner_index <= len(n_list)-1:
            if inner_count == 0:
                temp_list.append(n_list[inner_index])
            temp_list.append(n_list[inner_index+1])
            inner_index = inner_index + 1
            if inner_index == len(n_list)-1:
                break
            next_song_len = int(n_list[inner_index+1][n_list[inner_index+1].rfind(seperator)+1:]) # run time of next song
            inner_count = inner_count + 1 #counting the numbers of songs the whiel loop need to skip

        """sort the temp list lexigraphicaly"""
        temp_list.sort()

        """Skip numbers of iterartions based on how many songs were sorted """
        if inner_count == 0:
            index = index + 1
            count = count + 1
        else:
            for n in range(len(temp_list)):
                n_list[index+n] = temp_list[n]
            count = count + inner_count + 1
            index = index + inner_count + 1

def main():
    total_list = list()
    len_list = list()
    count = 0
    n_songs = 0

    """Getting inputs"""
    for line in sys.stdin:

        """Checking for new line characters(Blank lines to skip)"""
        if line == '\n':
            continue
        if line == None or line == "None\n":
            break
        if count == 0:
            n_songs = int(line)
        if count == 1:
            seperator = str(line.rstrip("\n"))

        if count > 1:
            total_list.append(line.rstrip("\n"))
            x = line.rfind(seperator)
            len_list.append(int(line[x+1:].rstrip("\n")))
        count += 1

    """Sort total_list into lexigraphical order and len_list into numerical order"""
    len_list.sort()
    total_list.sort()

    """Slicing K songs from the running time len_list"""
    n_list = len_list[-n_songs:len(len_list)]


    """Condition to sort songs if there is a duplicate of running time"""
    if check_dup(n_list) == True:
        collect_songs(n_list, total_list, seperator)
        sort_by_name_compo(n_list, seperator)
    else:
        collect_songs(n_list, total_list, seperator)


    """printing sorted k outputs"""
    for sog in n_list:
        print(sog.strip())

main()