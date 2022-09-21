import nltk, datetime, re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

#format dictionaries
weekDaysDict = {6:"sunday", 0:"monday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday"}
monthsDict = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
nums = [0,1,2,3,4,5,6,7,8,9,0]

given = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str} #dictionary for datetime given
current = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str} #dictionary for current datetime



def removeExtras(text):
    for word in text: #removes specific filler words from input
        if word in stop_words:
            text.remove(word)

    topop = []
    text = nltk.pos_tag(text)
    print("text: ", text)
    ct = 0

    for index,obj in enumerate(text):
        print(obj, ", ", index)
        for n in obj:
            if n[0] == "V"  or n[0] =="P":
                topop.append(index)
                index -=1

    for index,obj in enumerate(topop):
        text.pop(obj-index)
    
    return text
def getCurrent(): #adds current date+time to current dict
    dtt = str(datetime.datetime.now()).split(" ")[1]
    dt = str(datetime.datetime.now()).split(" ")[0].split("-")
    # print(dt)
    

    current['month']= int(dt[1])
    current['date'] = int(dt[2])
    current['year'] = int(dt[0])
    current['weekday'] = weekDaysDict[datetime.datetime.today().weekday()]
    current['time'] = dtt[::8]

    print(current)



getCurrent()

ogtext = "I need to work on my math homework before the twenty-first"
text = word_tokenize(ogtext)
text = removeExtras(text)

grammar = "NP: {<NN>?}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(text)
tree = str(tree)
tree = tree[1:]
print(tree)
out = re.search("(^.*)$", tree)

print(out)
# print(text)

