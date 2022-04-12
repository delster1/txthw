# TODO : aadd google calendae
import datetime
import re
from gcal import createEvent

# dictionaries for current time and time info given via inut
given = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str}
current = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str}
output = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str}


# stuff for parsing out of input 
dict = {'verbs': {}, 'nums' : {}}
# def find_assignment(inp):
    # print(inp)

og = input("text your work here \n")
# og = "i need to watch a discrete math video by sunday 10:00 pm"

toParseToDate = []
toParseToTime = []
# random arrays
otherWords = ["I","need","must","my","we","have to","i","to","a","by","before","this","on","do"]
nums = ['1','2','3','4','5','6','7','8','9','0','11','12'] #parsing nums out of input
times = ["oclock",":","pm","am"] #parsing times
timeNums = ["1","2","3","4","5","7","8","9","10","11","12"]
dates = ["/","-"] 
weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
otherDays = ["tomorrow","today"]
months = ["january","febuary","march","april","may","june","july","august","september","october","november","december"]
verbs = ["do","finish","start","try","work on","watch","read","study","watch"]
res = []
weekDaysDict = {6:"sunday", 0:"monday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday"}


def daysUntil(toParse):
    
    
    # parsing input of months without "next"
    
    if(toParse in months):
            output['month']=month[months.index(month)]
         # parsing input of weekdays without "next"
    elif toParse in weekDays:
            output['weekday']=weekDays.index(toParse)
            dayToAdd = output['weekday']
            o = output['weekday']
            i = 0
            
            # loop for finding how many days until given day when given weekday
            caught = False
            findingDay = False
            weekDayCounter = 0
            currentDay = current['weekday']
            objective = weekDaysDict[dayToAdd]
            output['weekday'] = weekDays[weekDays.index(toParse)]
            while caught == False:
                for o in weekDays:
                    if (o == currentDay and findingDay == False):
                        findingDay = True
                    if findingDay == True and o != currentDay:
                        weekDayCounter+=1
                    if(o==objective and findingDay == True):
                        caught = True
                        break
            
            output['date']=current['date']+weekDayCounter

            return weekDayCounter


# code to turn input into workable array split by spaces
inp = og.split(' ')
out = inp.copy()

# take month from code (this could be a oneliner)
def dateFromMonth(month):
    # print(months[month -1])

    return months[month-1]

# function to turn words like "tomorrow" and "next blah" into proper date output(out dict) - BIG FUNCTION
def parseToDate(toParseToDate):
    toParse = toParseToDate.split(" ")

    if ("december" not in toParse):
        output['year'] = current['year']
    # code for detecting when "next" is in the given input
    if("next" in toParse):
        output['month'] = current['month']
        output['date'] = current['date'] + 7
        nextLocation = toParse.index("next")
        withoutNext = toParse[nextLocation+1]
        # parsing input of months without "next"
        

            
        # output["date"]=current["date"]+7+weekDayCounter
        # checking word after next for months
        if toParse[nextLocation+1] in months:     
            output['month']=months.index(toParse[nextLocation+1])

        # checking word after next for weekdays
        elif toParse[nextLocation+1] in weekDays:     
            output['weekday']=weekDays.index(toParse[nextLocation+1])
            dayToAdd = output['weekday']
            o = output['weekday']
            i = 0
            
            # loop for finding how many days until given day when given weekday
            weekDayCounter = daysUntil(toParse[nextLocation+1])

            output['date'] += 7
            
#   next not in toparse
    else:
        output['month'] = current['month']

        toParse = toParse[0]
        if toParse in weekDays:
            weekDayCounter = daysUntil(toParse)

            # output["date"]=current["date"]+7+weekDayCounter
    # parsing input of months without "next"
    
# function for parsing to time
def parseToTime(inp):
    daytime = False
    d = {1:"01", 2:"02", 3:"03", 4:"04", 5:"05", 6:"06", 7:"07", 8:"08", 9:"09"}
    if "am" in inp :
        daytime = True
    if "pm" in inp:
        daytime = False
    timeNum = int(''.join(filter(str.isdigit, inp))) # removes all letters from inp
    # for working with date with imperfect format
    if ":" not in inp:
        # sort between day and night 4 l8r
        
        daytime = False # default night ig
         # takes everything out input xcept for nums
        # changing to 24h time
        if int(timeNum) <= 12 and not daytime:
            timeNum += 12
            daytime = None

        out = str(timeNum) + ":" + "00" #makes time when given hour to 24h formatted
        
    # given near perfect format j need to check and organize stuff 
    else:
        # checks if the input is formatted w two digits in front of each colon and fixes if not
        splittedByColon = inp.split(":")
        #removes letters from thing
        for i,o in enumerate(splittedByColon):
            o = ''.join(filter(str.isdigit, o)) 
            splittedByColon[i] = o
            
        #makes sure everything has correct string format
        if(len(inp)!= 2):
            if(len(splittedByColon[0]) != 2):
                splittedByColon[0] = "0" + splittedByColon[0]
            if(len(splittedByColon[1]) != 2):
                splittedByColon[0] = "00"
        # changing numbers to 24h 
        if(int(splittedByColon[0]) < 12 and not daytime):
            num = 12 + int(splittedByColon[0])
            splittedByColon[0] = str(num)
            daytime = None
        out = splittedByColon[0] + ":" + splittedByColon[1]
        
    output['time'] = out



# code for finding current date
def getCurrent():
    dtt = str(datetime.datetime.now()).split(" ")[1]
    dt = str(datetime.datetime.now()).split(" ")[0].split("-")
    # print(dt)
    currentMonth = dateFromMonth(int(dt[1]))

    current['month']= int(dt[1])
    current['date'] = int(dt[2])
    current['year'] = int(dt[0])
    current['weekday'] = weekDaysDict[datetime.datetime.today().weekday()]
    current['time'] = dtt[::8]

    # print(current)



def parseFromInp():
    for i,o in enumerate(inp):
        # if o is a weekday without next
        if o in weekDays and inp[i-1] != "next" and o not in otherDays:
            toParseToDate.append(o)
            out.remove(o)
        # if of is a weekday with next
        elif o == "next" and inp[i+1] in weekDays and o not in otherDays:
            toAppend = o + " " + inp[i+1]
            toParseToDate.append(toAppend)
            # print(out)
            out.remove(o)
            out.remove(inp[i+1])
        # checking for words like tomorrow etc
        elif o in otherDays:
            toParseToDate.append(o)
            out.remove(o)
        # removing random words from input
        elif o in verbs:
            out.remove(o)
            dict['verbs'][o] = i
        # sorting for : and / for dates and times
        elif "/" in o or "-" in o:
            if "/" in o or "-" in o:
                toParseToDate.append(o)
                out.remove(o)
        # checks words around a number for a month or smth like o'clock to determine to parse to date or time
        elif o in nums or ":" in o or o in times:
            if(inp[i-1]) in times :
                temp = o + inp[i-1] 
                toParseToTime.append(temp) 
                out.remove(o)
            elif(i != len(inp)-1): 
                if inp[i+1] in times :
                    temp = o + inp[i+1] 
                    toParseToTime.append(temp) 
                    out.remove(o)
                    
            elif (inp[i-1] or inp[i+1]) in months: 
                toParseToDate.append(temp)
                out.remove(o)
            elif (o in times):
                toParseToDate.append(o)
                out.remove(o)
        
        elif o in otherWords:
            out.remove(o)
        elif o in timeNums:
            toParseToDate.append(o)
            out.remove(o)
        for l in times:
            if l in o and o in out:
                toParseToTime.append(o)
                out.remove(o)
        for o in out:
            if o in toParseToDate or o in toParseToTime:
                out.remove(o)
        
        
    # print(out)
    # print("to parse to date: ", toParseToDate)
    # print("to parse to time: ", toParseToTime)

    if(len(toParseToDate) == 0):
        output['date'] = current['date'] 
        output['month'] = current['month']
        output['year'] = current['year']
        output['weekday'] = current['weekday']

    if(len(toParseToTime) == 0):
        output['time'] = "24:00"       

    t = out.copy()
    n = dict['verbs']
    # print(n.items())

    if len(times) == 0:
        pass
    else:
        i = []
        i.append(o for o in dict if len(o) > 0)
        # print(i)
    # print(len(dict['nums']))

    # To parse to date is an array of arguments either of strings or words for formatting date from input
    for i,o in enumerate(toParseToDate):
        parseToDate(o)
    
    for i,o in enumerate(toParseToTime):
        parseToTime(o)

def main():    
    getCurrent()
    parseFromInp()
    outstr = " ".join(out)
    print(outstr)
    print(output)
    createEvent(output,outstr)
    

if __name__ == "__main__":
    main()