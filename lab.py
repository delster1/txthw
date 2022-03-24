# TODO : add main method, make code functional, cleanup dict and parsing inside of it
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
og = "i need to work on my english assignments next friday"

toParseToDate = []
# random arrays
nums = ['1','2','3','4','5','6','7','8','9','0'] #parsing nums out of input
times = ["oclock",":","pm","am"] #parsing times
dates = ["/","-"] 
weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
otherDays = ["tomorrow","today"]
months = ["january","febuary","march","april","may","june","july","august","september","october","november","december"]
verbs = ["do","work","finish","start","try","work on","watch","read","study"]
res = []
weekDaysDict = {6:"sunday", 0:"monday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday"}

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
        output['date'] = currentx`['date'] + 7
        nextLocation = toParse.index("next")

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
            caught = False
            findingDay = False
            weekDayCounter = 0
            currentDay = current['weekday']
            objective = toParse[nextLocation +1]
            print("Current", currentDay, "\n", "objective", objective)
            while caught == False:
                for o in weekDays:
                    # print("FindingDay: ",  findingDay)
                    if (o == currentDay and findingDay == False):
                        findingDay = True
                    print("o in loop: ", o, "findingday: ", findingDay)
                    if findingDay == True and o != currentDay:
                        weekDayCounter+=1
                    if(o==objective and findingDay == True):
                        caught = True
                        break
            print("counter ", weekDayCounter, "object: ", o)
                
    elif(toParse in months):
        output['month']=month[months.index(month)]
    elif toParse in weekDays:
        output['weekday'] = weekDays[weekDays.index(toParse)]
    print(output)
    

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
        if o in weekDays and inp[i-1] != "next" and o not in otherDays:
            given['days']=o
            out.remove(o)
        elif o == "next" and inp[i+1] in weekDays and o not in otherDays:
            toAppend = o + " " + inp[i+1]
            toParseToDate.append(toAppend)
            # print(out)
            out.remove(o)
            out.remove(inp[i+1])
        elif o in otherDays:
            toParseToDate.append(o)
            out.remove(o)
        elif o in verbs:
            out.remove(o)
            dict['verbs'][o] = i
        elif ":" in o or "/" in o or "-" in o:
            if ":" in o:
                toParseToDate.append(o)
            elif "/" in o or "-" in o:
                toParseToDate.append(o)
        elif o in nums:
            toAppend = inp[i-1] + " " + o + " " + inp[i+1]
            if(inp[i-1] or inp[i+1]) in times:
                toParseToDate.append(toAppend)
            elif (inp[i-1] or inp[i+1]) in months:
                toParseToDate.append(toAppend)

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
    print(out)
    print(dict)
    # To parse to date is an array of arguments either of strings or words for formatting date from input
    for i,o in enumerate(toParseToDate):
        parseToDate(o)
        print(o)

def main():    
    getCurrent()
    parseFromInp()

if __name__ == "__main__":
    main()

