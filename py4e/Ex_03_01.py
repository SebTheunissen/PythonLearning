hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Rate per hour:")
r = float(rte)
r2 = r * 1.5
h2 = h - 40
gross = h * r
gr2 = h2 - r2

if h > 40:
    gross = 40.0 * r
    gr2 = h2 * r2
    gross = gross + gr2
    print(gross)
else:
	print(gross)
