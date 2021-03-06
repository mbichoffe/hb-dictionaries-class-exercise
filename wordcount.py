# put your code here.
import sys

def get_word_count(filename):

    f = open(filename)

    word_count = {}

    text = f.read().split()

    for word in text:
        word = word.strip(' \' !*&#;:,.-+_? " ').lower()
        word_count[word] = word_count.get(word, 0) + 1

    f.close()

    return word_count


def print_word_count(dictionary):

    for key, value in dictionary.iteritems():
        print key, value


word_count = get_word_count(sys.argv[1])
print_word_count(word_count)