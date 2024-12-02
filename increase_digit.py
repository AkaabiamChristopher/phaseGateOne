"""
Ask digit three times 
collect
store each of them as first_digit, second_digit,third_digit
if first_digit < second_digit and second_digit < third_digit
display first_digit,second_digit,third_digit
if first_digit > second_digit and first_digit < third_digit
display second_digit,first_digit,third_digit
if first_digit < second_digit and first_digit > third_digit
display third_digit,first_digit,second_digit
if first_digit == second_digit and first_digit == third_digit
display third_digit,first_digit,second_digit
if first_digit > second_digit and second_digit > third_digit
display third_digit,second_digit,first_digit

"""





first_digit = int(input("Enter first number:"))
second_digit = int(input("Enter second number:"))
third_digit = int(input("Enter third number:"))

if first_digit < second_digit and second_digit < third_digit:
	print(f"{first_digit},{second_digit},{third_digit}")

if first_digit > second_digit and first_digit < third_digit:
	print(f"{second_digit},{first_digit},{third_digit}")

if first_digit < second_digit and first_digit > third_digit:
	print(f"{third_digit},{first_digit},{second_digit}")

if first_digit == second_digit and first_number == third_number:
	print(f"{third_number},{first_number},{second_number}")

if first_digit > second_digit and second_digit > third_digit:
	print(f"{third_digit},{second_digit},{first_digit}")
