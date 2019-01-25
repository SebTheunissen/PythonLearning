fname = input("Enter file name: ")
fh = open(fname)
for a in fh:
    a = a.strip()
    a = a.upper()
    print(a)
