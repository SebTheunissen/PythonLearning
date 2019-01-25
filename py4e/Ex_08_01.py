file = open('romeo.txt')
lst = list()

for line in file:
    line.rstrip()
    clst = line.split()
    for word in clst:
        if word in lst : continue
        lst.append(word)

lst.sort()
print(lst)
