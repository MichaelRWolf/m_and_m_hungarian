import nltk

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hiya, {name}')  # Press ⌘F8 to toggle the breakpoint.


def wing_it():
    sentence = "This is a sentence."

    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)

    print(tagged)


# Output: [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('sentence', 'NN'), ('.', '.')]

# TODO: Research different parsers and dictionaries.

def friends_romans():
    sentence = "Friends, romans, countrymen, \nlend me your ears.\n"

    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)

    print(tagged)

    for word, part_of_speech in tagged:
        # print(word, part_of_speech)
        combined_string = "{}.{} ".format(part_of_speech, word)
        print(combined_string, end='')


def whole_speech_from_file(filename):
    with open(filename, encoding="utf-8") as file:
        text = file.read()

    print(text)

    tokens = nltk.wordpunct_tokenize(text)
    tagged = nltk.pos_tag(tokens)

    for word, part_of_speech in tagged:
        if part_of_speech[0].isalpha():
            combined_string = " {}{}".format(part_of_speech.lower(), word.capitalize())
        else:
            combined_string = "{}".format(word)

        print(combined_string, end='')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # wing_it()
    # friends_romans()
    whole_speech_from_file('speech.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
