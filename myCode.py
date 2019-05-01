import string

def process_file(filename):
    hist = dict()
    fp = open(filename,encoding="utf8")
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        
        hist[word] = hist.get(word, 0) + 1
        

hist = process_file('alice.txt')
# for key in hist:
#      print(("The word '" + key + "' occurs  " + str(hist[key]) + "  times!!!"))
values=list(hist.values())
words=list(hist.keys())
last_words=list(zip(values,words))
last_words.sort()
for i in range(len(last_words)-1,len(last_words)-20,-1):
  print(last_words[i])
