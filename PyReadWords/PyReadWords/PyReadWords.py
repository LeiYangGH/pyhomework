def get_words_from_file(filename="synthetic.txt"):
    file = open(filename, 'r', encoding="utf-8")
    alltxt = file.read()
    words = alltxt.split()
    stripwords = [w.strip(r'\n"-:\';,.') for w in words]
    alphawords = [w for w in stripwords if all(c.isalpha() for c in w)]
    lowerwords = [w.lower() for w in alphawords]
    return lowerwords

filename = "synthetic.txt"
words = get_words_from_file(filename)
print(filename, "loaded ok.")
print("{} valid words found.".format(len(words)))
print("Valid word list:")
for word in words:
    print(word)