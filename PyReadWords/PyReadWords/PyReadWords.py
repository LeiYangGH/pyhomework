def get_words_from_file(filename="synthetic.txt"):
    file = open(filename, 'r', encoding="utf-8")
    alltxt = file.read()
    words = alltxt.split()
    stripwords = [w.strip(r'"-:\';,.') for w in words]
    nonemptywords = [w for w in stripwords if len(w) > 0]
    alphawords = [w for w in nonemptywords if all(c.isalpha() for c in w)]
    lowerwords = [w.lower() for w in alphawords]
    return lowerwords

#filename = "synthetic.txt"
filename = "pg84.txt"
words = get_words_from_file(filename)
print(filename, "loaded ok.")
print("{} valid words found.".format(len(words)))
print("Valid word list:")
#for word in words:
#    print(word)