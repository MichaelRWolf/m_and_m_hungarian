# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hiya, {name}')  # Press ⌘F8 to toggle the breakpoint.



import nltk

def wing_it():
    sentence = "This is a sentence."

    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)

    print(tagged)
# Output: [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('sentence', 'NN'), ('.', '.')]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    wing_it()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
