file = open('mbox-short.txt')
count = 0
for line in file:
    if not line.startswith('From '): continue
    clst = line.split()
    count = count + 1
    print(clst[1])

print("There were", count, "lines in the file with From as the first word")

#First try, same result
#for line in file:
    #if line.startswith('From '):
        #clst = line.split()
        #count = count + 1
        #print(clst[1])
    #Else:
        #continue
#print("There were", count, "lines in the file with From as the first word")
