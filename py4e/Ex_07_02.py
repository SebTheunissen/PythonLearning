fname = input("Enter file name: ")
file = open(fname)

count = 0
countavg = 0
for line in file:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    svalue = line[21:]
    fvalue = float(svalue)
    countavg = countavg + fvalue
    count = count + 1
spamavg = countavg / count
print("Average spam confindence:" , spamavg)
