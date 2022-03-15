dict = {'verbs': {}, 'weekdays': {}, 'months' : {}, 'nums' : {}}
def find_assignment(inp):
    print(inp)

# og = input("text your work here \n")
nums = ['1','2','3','4','5','6','7','8','9','0']
og = "i gotta watch math vid by 2 oclock on wednesday"

times = ["oclock",":","pm","am"]
dates = ["/","-"]
weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
verbs = ["do","work","finish","start","try","work on","watch","read","study"]
ignore = ["at","for","with","before","by","until","i","have to", "must", "to", "gotta","got","after","have","my","me","on"]
res = []
inp = og.split(' ')
out = inp.copy()

def toDate():
    pass

for i,o in enumerate(inp):
    if o == "next" and inp[i+1] in weekdays:
        str = o + " " + inp[i+1]
        dict['weekdays'][str] = i
        print(out)
        out.remove(o)
        out.remove(inp[i+1])
    if o in weekdays and inp[i-1] != "next":
        dict['weekdays'][o] = i
        out.remove(o)
    elif o in verbs:
        out.remove(o)
        dict['verbs'][o] = i
    elif o in ignore:
        out.remove(o)
    elif o in nums:
        dict['nums'][o] = i

if len(times) == 0:
    pass
else:
    i = []
    i.append(o for o in dict if len(o) > 0)
    print(i)
    toDate()
print(len(dict['nums']))

print(out)
print(dict)

