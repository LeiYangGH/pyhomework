def get_words_from_file(filename = "synthetic.txt"):
    """asdasd"""
    file = open(filename, 'r', encoding="utf-8")
    infile = file.readlines()
    return infile

filename = "synthetic.txt"
words = get_words_from_file(filename)
print(filename, "loaded ok.")
print("{} valid words found.".format(len(words)))
print("Valid word list:")
for word in words:
    print(word)