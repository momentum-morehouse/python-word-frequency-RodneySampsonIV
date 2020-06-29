STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


def flatten_lol(lol):
    flat_list = []
    for sublist in lol:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def print_word_freq(file):
    d = dict()
    # string  = ("*")
    """Read in `file` and print out the frequency of words in that file."""
    # Your code will go here. You can write additional functions if you want, and call them inside this function.
    # first open the file
    with open(file) as f:
        lyrics = f.readlines()
        for line in lyrics:
            #word_list = [line.split() for line in lyrics]
            #word_list = flatten_lol(word_list)
            line = line.strip()
            line = line.lower()
            words = line.split(" ")
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                elif not word in STOP_WORDS:
                    d[word] = 1
        for key in list(d.keys()):
            print(key,":", d[key])
                #word_list[word] = word.get(word, 0) + 1

    #print('/n.join' (['%s,%s' % (k, v)]))


# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
