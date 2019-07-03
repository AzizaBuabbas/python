num1 = input ("Enter the first number:")
num2 = input ("Enter the second number:")
operation = input ("Choose the operation (+, -, /, *):")

if num1.isdigit() and num2.isdigit() :
	if operation == "+":
		total = int(num1) + int (num2)
		print( "The answer is %s " % total )
	elif operation == "-":
		total = int(num1) - int(num2)
		print("The answer is %s " % total )

	elif operation == "*":
		total = int(num1) * int(num2)
		print("The answer is %s " % total )
	elif operation == "/":
		total = int(num1)/ int(num2)
		print("The answer is %s " % total )
	else : 
		print ("The numbers were invalid.")
