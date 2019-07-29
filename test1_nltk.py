import nltk
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()

#from nltk.tag import StanfordPOSTagger
#st = StanfordPOSTagger('english-bidirectional-distsim.tagger')

# see here for all tags https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
# for better pos_taggers: https://stackoverflow.com/questions/30821188/python-nltk-pos-tag-not-returning-the-correct-part-of-speech-tag
# export CLASSPATH="/home/openerp/Scrivania/ricerca_lavoro/nltk_prodnames/stanford-postagger-2018-10-16"

def divide_name(s0):

# first: check for typos (this should be made automatically)
    wrong=[("T Shirt","Tshirt")]
    for ss in wrong:
        s0=s0.replace(ss[0],ss[1])

# second get the single words
    s1=tknzr.tokenize(s0)

# third tag the parts of speech: basically nouns will be the end marks of splitted parts
    s2 = nltk.pos_tag(s1)    # standard nltk tagger
#    s2 = st.tag(s1)     # stanford tagger
    last = 'None'
    out = ""

    connectors = ["%",","] # this is just to avoid extra spaces before some symbols

# fourth change tags that either are inappropriate (e.g. "big" tagged as a noun) or do not fit our purposes (e.g. "women" is a noun but here likely means "for women" so it is a kind of adjective)

    #exceptions = ["%",",","painting","quality","household"]  # test for stanford
    exceptions = ["%",",","painting","quality","household","canvas","art","nude","beige","sexy","34-46","fashion","round","sports","classic", \
        "men","mixed","toe","dog","nest","adornment","articles","motorcycle","pants","moto","protective","riding","touring","motorbike","summer","print","women","iron","winter","pointed","low","lady","boots","fur","wool"]
    exc_tags = [":",":","NN","JJ","JJ","NN","NN","JJ","JJ","JJ","NN","NN","JJ","JJ","JJ","JJ","JJ","NN","JJ","NN","JJ","NN","JJ","NN","JJ","JJ","JJ","JJ","JJ","JJ","JJ","JJ","JJ","JJ","JJ","JJ","JJ","NN","JJ","JJ"]

# fifth compute parts putting together words that aren't nouns + 1 noun, or just 2 nouns
    i=0
    for sx in s2:
        if sx[0].lower() in exceptions:
            ss = sx[0].lower()
            s2[i] = (sx[0],exc_tags[exceptions.index(ss)])
            i = i + 1
            continue
        if sx[1][:2] == 'NN':
            tmp = nltk.pos_tag(sx[0].lower())
            s2[i] = (sx[0],tmp[0][1])
        i=i+1
#    print(s2) # to check assigned tags
    for sx in s2:
        if last in ('None', 'JJ', 'JJR', 'JJS', 'CD', 'RB', 'RBR', 'RBS', ':', 'NNP', 'VB', 'VBG','VBN','DT','POS','PDT','IN','CC','SYM'):
            if not out:
                cx = 1
                out = sx[0]
            else:
                cx = cx + 1
                if not sx in connectors:
                    out = out + ' '
                out = out + sx[0]
        elif last in ('NN','NNS'):
            if sx[1] in (':','CC','IN'):
                if not sx in connectors:
                    out = out + ' '
                out = out + sx[0]
                cx = cx + 1
            elif cx == 1:
                out = out + ' ' + sx[0]
                cx = cx + 1
            else:
                out = out + ' / ' + sx[0]
                cx = 1
        last = sx[1]
    return out

s0 = "100% hand-painted canvas oil painting high quality Household adornment art flower pictures DM-15072306"
print(s0)
print(divide_name(s0))
s0 = "MORAZORA Big Size 34-46 2019 New Fashion high heels women pumps thin heel classic white red nude beige sexy ladies wedding shoes"
print(s0)
print(divide_name(s0))
s0 = "Luxury Woman Elegant Flats Solid Vintage Genuine Leather Sexy Pointed Toe Classic Low Heels Casual Office Lady Mules P16"
print(s0)
print(divide_name(s0))
s0 = "RELKA Classic Men Fashion Casual Shoes Luxury Flying Round Toe Comfortable Heel Shoes Mixed Color Soft Basic Sports Shoes P95"
print(s0)
print(divide_name(s0))
s0 = "MORAZORA Russia 2019 Genuine leather boots wool fur fashion knee high boots women warm wool boots round toe winter snow boots"
print(s0)
print(divide_name(s0))
s0 = "Pet Dog Bed Warming Dog House Soft Material Nest Dog Baskets Fall and Winter Warm Kennel For Cat Puppy Plus size Drop shipping"
print(s0)
print(divide_name(s0))
s0 = "Ceramic little monk Buddha Statues tea pet creative home furnishing articles small adornment home decor ornament landscape"
print(s0)
print(divide_name(s0))
s0 = "2018 New Motorcycle Pants Men Moto Jeans Protective Gear Riding Touring Motorbike Trousers Motocross Pants Pantalon Moto Pants"
print(s0)
print(divide_name(s0))
s0 = "Women's Summer Print Jumpsuit Shorts Casual Loose Short Sleeve V-neck Jumpsuit 10 color"
print(s0)
print(divide_name(s0))
s0 = "New 2019 Women Tshirt Batman Spiderman Iron Man Captain America Winter Soldier Marvel T Shirt Avengers Costume Comics Superhero"
print(s0)
print(divide_name(s0))
