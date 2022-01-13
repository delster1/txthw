dict = {'verbs': {}, 'weekdays': {}, 'months' : {}, }
def find_assignment(inp):
    print(inp)

og = input("text your work here \n")
# og = "i have to do my math hw by friday"
weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
verbs = ["do","work","finish","start","try","work on"]
ignore = ["at","for","with","before","by","until","i","have to", "must", "to", "gotta","got","after","have","my","me"]
res = []
inp = og.split(' ')
out = inp.copy()
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


print(out)
print(dict)

