file = open('mbox-short.txt')
dick = dict()
# Make dictonary with second word in the lines as keys
# Count howmany times word is in the file
for line in file:
    if not line.startswith('From '): continue
    words = line.split()
    #for word in words:
    dick[words[1]] = dick.get(words[1],0) + 1

bigword = None
bigcount = None
for word, count in dick.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)
print(dick)
