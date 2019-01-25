#ask for user input
#give back largest & smallest number
#error check and stop
#use if in a while loop
#use if and elif in a try

largest = None
smallest = None

while True:
    snum = input("Enter a number: ")
    if snum == "done" : 
        break
    try:
        inum = int(snum)
        if smallest is None:
            smallest = inum
            largest = inum
        elif inum < smallest:
            smallest = inum
        elif inum > largest:
            largest = inum
    except:
        print('Invalid Input')
        continue
    
print("Maximum is ", largest)
print("Minimum is ", smallest)