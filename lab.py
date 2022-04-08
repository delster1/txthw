# TODO : add main method, make code functional, cleanup dict and parsing inside of it add parsing date
import datetime

# dictionaries for current time and time info given via inut
given = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str}
current = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str}
output = {'date': int, 'month': int, 'year':int , "weekday": str, "time": str}


# stuff for parsing out of input 
dict = {'verbs': {}, 'nums' : {}}
def find_assignment(inp):
    print(inp)

# og = input("text your work here \n")
og = "i need to work on my english assignments by 12 am"

toParseToDate = []
toParseToTime = []
# random arrays
nums = ['1','2','3','4','5','6','7','8','9','0','11','12'] #parsing nums out of input
times = ["oclock",":","pm","am"] #parsing times
dates = ["/","-"] 
weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
otherDays = ["tomorrow","today"]
months = ["january","febuary","march","april","may","june","july","august","september","october","november","december"]
verbs = ["do","work","finish","start","try","work on","watch","read","study"]
res = []
weekDaysDict = {6:"sunday", 0:"monday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday"}


def daysUntil(toParse):
    
    print("daysUntil(", toParse, ")")
    
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
            print("Current", currentDay, "\n", "objective", objective)
            output['weekday'] = weekDays[weekDays.index(toParse)]
            while caught == False:
                for o in weekDays:
                    # print("FindingDay: ",  findingDay)
                    if (o == currentDay and findingDay == False):
                        findingDay = True
                    print("o in loop: ", o, "findingday: ", findingDay, "objective: ", objective)
                    if findingDay == True and o != currentDay:
                        weekDayCounter+=1
                    if(o==objective and findingDay == True):
                        caught = True
                        break
            
            print("counter ", weekDayCounter, "; object: ", o)
            output['date']=current['date']+weekDayCounter

            return weekDayCounter
    print(output)


# code to turn input into workable array split by spaces
inp = og.split(' ')
out = inp.copy()

# take month from code (this could be a oneliner)
def dateFromMonth(month):
    # print(months[month -1])

    return months[month-1]

# function to turn words like "tomorrow" and "next blah" into proper date output(out dict) - BIG FUNCTION
def parseToDate(toParseToDate):
    print()
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
            
            print("toparse: ", toParse, "counter: ", weekDayCounter, "; object: ", o)
    else:
        toParse = toParse[0]
        if toParse in weekDays:
            print("toParse in weekdays")
            weekDayCounter = daysUntil(toParse)

            # output["date"]=current["date"]+7+weekDayCounter
    # parsing input of months without "next"
    print(output)
    
# function for parsing to time
def parseToTime(inp):
    d = {1:"01", 2:"02", 3:"03", 4:"04", 5:"05", 6:"06", 7:"07", 8:"08", 9:"09"}
    # for working with date with imperfect format
    if ":" not in inp:
        if "am" in toParseToTime :
            daytime = True
        if "pm" in toParseToTime:
            dayTime = False
        daytime = False
        timeNum = [int(i) for i in inp.split() if i.isdigit()]
        if timeNum <= 12 and not daytime:
            timeNum += 12

    out = str(timenum) + ":" + 00

    else:
    
    
    print(daytime)
    out['time']


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
        elif ":" in o or "/" in o or "-" in o:
            if ":" in o:
                toParseToTime.append(o)
                out.remove(o)
            elif "/" in o or "-" in o:
                toParseToDate.append(o)
                out.remove(o)
        # checks words around a number for a month or smth like o'clock to determine to parse to date or time
        elif o in nums:
            print("temp")
            toAppend = inp[i-1] + " " + o + " " + inp[i+1]
            if(inp[i-1]) in times :
                temp = o + inp[i-1] 
                toParseToTime.append(temp) 
                out.remove(o)
            elif(inp[i+1]) in times :
                temp = o + inp[i+1] 
                toParseToTime.append(temp) 
                out.remove(o)
                 
            elif (inp[i-1] or inp[i+1]) in months: 
                toParseToDate.append(temp)
                out.remove(o)
        
        print(out)

    print(toParseToDate)
    print(toParseToTime)
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
    print("to parse to date", toParseToDate)

    # To parse to date is an array of arguments either of strings or words for formatting date from input
    for i,o in enumerate(toParseToDate):
        parseToDate(o)
        print(o)
    
    for i,o in enumerate(toParseToTime):
        parseToTime(o)

def main():    
    getCurrent()
    parseFromInp()

if __name__ == "__main__":
    main()

