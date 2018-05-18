# xzy1
#!/usr/bin/env python3
import sys
try:
	Total = int(sys.argv[1])
	tax1 = Total - 3500
	if tax1 <= 1500:
		rate = 0.03
		number = 0
	elif tax1 > 1500 and tax1 <= 4500:
		rate = 0.1
		number = 105
	elif tax1 > 4500 and tax1 <= 9000:
		rate = 0.2
		number = 555
	elif tax1 > 9000 and tax1 <=35000:
		rate = 0.25
		number = 1005
	elif tax1 > 35000 and tax1 <= 55000:
		rate = 0.3
		number = 2755
	elif tax1 > 55000 and tax1 <=80000:
		rate = 0.35
		number = 5505
	elif tax1 > 80000:
		rate = 0.45
		number = 13505
	tax = tax1 * rate - number
	print("The tax you need to pay is: {:6.2f}".format(tax))
except ValueError:
	print("Parameter Error")
