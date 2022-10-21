# Default text sources: https://github.com/amephraim/nlp/tree/master/texts

filename = "harrypotter1-4.txt" # INCLUDE FILE EXTENTIONS!!!!
validchars = "abcdefghijklmnopqrstuvwxyz"
validatechars = True
# Makes it very much slower, but only allows characters in validchars
# However, if it is false, there may be some blank entries for unknown reason.

from time import sleep as s
from time import time
beginningtime = time()
f = open(filename).read()
print("Loaded file")
s(0.001)
f = f.replace("-\n", "").replace("\n", " ").replace("  ", " ").lower().split(" ")
print("Formatted file")
print("Elapsed time: " + str(time() - beginningtime) + " seconds")
s(0.001)
subframe = len(f)
if validatechars:
    names = []
    k = [char for char in validchars.lower()]
    print("Parsing raw data with " + str(subframe) + " data entries")
    for i in f:
        subframe -= 1
        d = ""
        for o in i:
            if k.count(o):
                d += o
        if d:
            names.append(d)
        if not subframe % 10000:
            print(str(subframe) + " left")
            s(0.001)
    print("Finished names")
    f = None
    print("Set base variable to None to save memory")
finaldata = {}
if validatechars:
    subframe = len(names)
    print("Elapsed time: " + str(time() - beginningtime) + " seconds")
else:
    sunframe = len(f)
print("Start sort with " + str(subframe) + " data entries")
if validatechars:
    while len(names):
        name = names[0]
        if name not in finaldata:
            finaldata[name] = [name, 0]
        finaldata[name][1] += 1
        names.remove(names[0])
        subframe -= 1
        if not subframe % 1000:
            print(str(subframe) + " left")
            s(0.001)
else:
    while len(f):
        name = f[0]
        if not finaldata.has_key(name):
            finaldata[name] = [name, 0]
        finaldata[name][1] += 1
        f.remove(f[0])
        subframe -= 1
        if not subframe % 1000:
            print(str(subframe) + " left")
            s(0.001)
print("Elapsed time: " + str(time() - beginningtime) + " seconds")
print("Parsing output of " + str(len(finaldata)) + " data entries")
s(0.001)
text = ""
subframe = len(finaldata)
for i in range(len(finaldata)):
    q = min(finaldata)
    text += finaldata[q][0] + " : " + str(finaldata[q][1]) + "\n"
    del finaldata[q]
    subframe -= 1
    if not subframe % 100:
        print(str(subframe) + " left")
        s(0.001)
print("Elapsed time: " + str(time() - beginningtime) + " seconds")
print("Writing to file")
s(0.001)
f = open("output.txt", "w")
f.write(text)
f.close()
f = None
print("Finished writing")
print("Total time: " + str(time() - beginningtime) + " seconds")
input()