file = open('mbox-short.txt')
dic = dict()

for line in file:
    if not line.startswith('From '): continue
    words = line.split()
    #split 6th word in line on ':'
    time = words[5]
    hour = time.split(':')
    #make key of first variable in splitted list
    #make dict() of this variable and count
    dic[hour[0]] = dic.get(hour[0],0) + 1
#for key and value in tuple print them out sorted
for k,v in sorted(dic.items()):
    print(k,v)
#print(sorted(dic.items()))
