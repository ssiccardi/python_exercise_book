###########
#  Morse interpreter up to 3 symbols
###########

fathers = [-1,"E","T","I","A","N","M",]
sons = [["E","T"],["I","A"],["N","M"],["S","U"],["R","W"],["D","K"],["G","O"]]

def morse(word):
    pp=[-1]
    if len(word)>3:
        return pp
    w = word.replace(".","")
    w = w.replace("-","")
    w = w.replace("?","")
    if len(w) > 0:
        return pp
    for x in word:
        elem = []
        for p in pp:
            i = fathers.index(p)
            elem.append(sons[i])
        pp = []
        for p in elem:
            if x == '.':
                pp.append(p[0])
            elif x == '-':
                pp.append(p[1])
            else:
                pp.append(p[0])
                pp.append(p[1])
    return pp

print(" %s" % morse(""))
print("a %s" % morse("a"))
print(".-?- %s" % morse(".-?-"))
print(". %s" % morse("."))
print("- %s" % morse("-"))
print("? %s" % morse("?"))
print(".. %s" % morse(".."))
print(".- %s" % morse(".-"))
print(".? %s" % morse(".?"))
print("-. %s" % morse("-."))
print("-- %s" % morse("--"))
print("-? %s" % morse("-?"))
print("?. %s" % morse("?."))
print("?- %s" % morse("?-"))
print("?? %s" % morse("??"))

print("... %s" % morse("..."))
print(".-. %s" % morse(".-."))
print(".?. %s" % morse(".?."))
print("-.. %s" % morse("-.."))
print("--. %s" % morse("--."))
print("-?. %s" % morse("-?."))
print("?.. %s" % morse("?.."))
print("?-. %s" % morse("?-."))
print("??. %s" % morse("??."))

print("..- %s" % morse("..-"))
print(".-- %s" % morse(".--"))
print(".?- %s" % morse(".?-"))
print("-.- %s" % morse("-.-"))
print("--- %s" % morse("---"))
print("-?- %s" % morse("-?-"))
print("?.- %s" % morse("?.-"))
print("?-- %s" % morse("?--"))
print("??- %s" % morse("??-"))

print("..? %s" % morse("..?"))
print(".-? %s" % morse(".-?"))
print(".?? %s" % morse(".??"))
print("-.' %s" % morse("-.?"))
print("--? %s" % morse("--?"))
print("-?? %s" % morse("-??"))
print("?.? %s" % morse("?.?"))
print("?-? %s" % morse("?-?"))
print("??? %s" % morse("???"))
