import re

file = open('regex_sum_data.txt')

lst = list()

for line in file:
    a = re.findall('[0-9]+' , line)
    if a == 0: continue
    for finding in a:
        finding = int(finding)
        lst.append(finding)
        b = sum(lst)

print(b)
