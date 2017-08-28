# put your code here.
def get_word_count(filename):

    f = open(filename)

    word_count = {}

    text = f.read().split()

    for word in text:
        word_count[word] = word_count.get(word, 0) + 1

    f.close()

    return word_count


def print_word_count(dictionary):

    for key, value in dictionary.iteritems():
        print key, value


word_count = get_word_count("twain.txt")
print_word_count(word_count)