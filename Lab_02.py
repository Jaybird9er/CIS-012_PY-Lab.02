## -Input and print strings

##name = input("Enter Employee Name ")
##salary = input("Enter salary ")
##company = input("Enter Comapany name ")
##test = input("Test", "It's just a test.")
##
##print("\n")
##print("Printing Employee Details")
##print("Name", "Salary", "Company")
##print(name, salary, company)

## -Find variable type

##number = input("Enter number ")
##name = input("Enter name ")
##
##print("\n")
##print("Priting type of input value")
##print("type of number", type(number))
##print("type of name", type(name))

## -Input and sum interger variables

##first_num = int(input("Enter first number "))
##second_num = int(input("Enter second number "))
##
##print("\n")
##print("First Number: ", first_num)
##print("Second Number: ", second_num)
##sum = first_num + second_num
##print("Sum of the numbers is: ", sum)

## -Input float variables

##float_num = float(input("Enter a float "))
##print("\n")
##print("Float is: ", float_num)
##print("Type is: ", type(float_num))

## -Accept multiple input variables on single line

##name, age, phone = input("Enter your name, age, phone number (put one space between each): ").split()
##print("\n")
##print("User Details: ", name, age, phone)

## -Accept multiline input

##MultiLine = []
##print("Tell me about yourself")
##while True:
##    line = input()
##    if line:
##        MultiLine.append(line)
##    else:
##        break
##finalText = '\n'.join(MultiLine)
##print("\n")
##print("Final text input")
##print(finalText)

## -Formatting: str.format()

##print('FirstName - {0}, LastName - {1}'.format('Ault', 'Kelly'))

##firstName = input("Enter your first name: ")
##lastName = input("Enter your last name: ")
##organization = input("Enter the organization name: ")
##print("\n")
##print("{0}, {1} works at {2}".format(firstName, lastName, organization))
##print('{1}, {0} works at {2}'.format(firstName, lastName, organization))
##print('FirstName {0}, LastName {1} works at {2}'.format(firstName, lastName, organization))
##print('{0}, {1} {0}, {1} works at {2}'.format(firstName, lastName, organization))

## -Accessing output string arguments by variable name

##name = input("Enter name ")
##marks = input("Enter marks ")
##print("\n")
##print("Student: Name: {firstName}, Marks: {percentage}%".format(firstName=name, percentage=marks))

## -Output text alignment specifying width

##text = input("Enter some text ")
##print("\n")
### > left aligned
##print("{:<25}".format(text))
### > right aligned
##print('{:>25}'.format(text))
### > center aligned
##print("{:^25}".format(text))

## -Specifying a sign while displaying output numbers

##pos_num = float(input("Enter a positive number "))
##neg_num = float(input("Enter a negative number "))
##print("\n")
### > sign '+' is for both positive and negative number
##print("{:+f}; {:+f}".format(pos_num, neg_num))
### sign '-' is only for negative number
##print('{:f}; {:-f}'.format(pos_num, neg_num))

## -Display output numbers in various format types

##number = int(input("Enter a number "))
##print("\n")
### > 'd' is for integer number formatting
##print("The number is: {:d}".format(number))
### > 'o' is for octal number formatting, binary and hexadecimal format
##print("Output number in octal format: {:o}".format(number))
### > 'b' is for binary number formatting
##print("Output number in binary format: {:b}".format(number))
### > 'x' is for hexadecimal format
##print("Output number in hexadecimal format: {:x}".format(number))
### > 'X' is for hexadecimal format
##print('Output number in HEXADECIMAL: {0:X}'.format(number))

## -Display numbers in floating-point format

##number = float(input("Enter a float number: "))
##print("\n")
### > 'f' is for float number arguments
##print("This is type float: {:f}".format(number))
### > padding for float numbers
##print("Padding for float numbers: {:5.2f}".format(number))
### > 'e' is for Exponent notation
##print("Output exponent notation: {:e}".format(number))
### > 'E' is for Exponent notation in UPPER CASE
##print("Output UPPERCASE exponent notation: {:E}".format(number))

## -Output string justification

##text = input("Enter a string: ")
##print("\n")
##print("Left justified: ", text.ljust(60, "*"))
##print("Right justified: ", text.rjust(60, "*"))
##print("Center justified: ", text.center(60, "*"))

## -
