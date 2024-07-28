#basic welcome to the code

print("hey wanderer, welcome to the calculator program! This program is made to calculate any operation available in the basic calculator for you. Just make sure to not give a big number as ultimately, the operation won't be executed successfully.")
print("Keep in mind this is an elementary calculator which can take only two numbers at once.")
print("XXXXXXXXXXXXXXXXX------------------------------------------------------------------------------------------------------------------------------XXXXXXXXXXXXXXXXXXXX")

#user input for desired numbers

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

#user input for desired operation

z = input("Select 'add' for addition\n'subtract' for subtraction\n'divide' for division\n'multiply' for multiplication:\n")
print("Please choose operation as instructed otherwise ERROR message will be displayed!") 
print("your chosen operation is:",z,"Press 'Yes' to confirm.\nIf you think this is a mistake, press 'No' to exit")

#confirming user input

w = input()
if w == 'Yes':
    print("Processing...")
elif w == 'No':
    break
    
print("ERROR DETECTED!")
    
#loop section for calculation processing

#addition

print("Verifying your entries...Calculating...Proceeding towards final answer...")
if z == 'add':
    print('Your required calculation is:',x+y)

#subtraction

elif z == 'subtract':
    print('Your required calculation is:',x-y)

#division

elif z == 'divide':
    print('Your required calculation is:',x/y)

#multiplication

elif z == 'multiply':
    print('Your required calculation is:',x*y)

else:
    print("ERROR! REASON: WRONG INPUT or manually instructed to exit directly due to unwanted input!")
#exit message

print("THANK YOU! VISIT AGAIN!")
