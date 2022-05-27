# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as file:
        content = file.read()
        return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.split()
    word_count = {}
    for word in text:
        word = word.lower()
        if word not in word_count:
            word_count[word] = 1
        word_count[word] = word_count[word] + 1

    return word_count
