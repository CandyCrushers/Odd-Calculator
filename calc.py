theinput = int(input("Enter your first number"))
theinput2 = int(input("Enter your second number!"))

print("Here are your options for what you can do, addition, multiply, or substract")
choose = input("What would you like to do to that number?")
choice = ["addition", "multiply", "subtract", "divide"]

while choose not in choice: 
    print("That is not a valid input")
    choose = input("Enter Again")

print("Valid input")

def addition():
    return theinput + theinput2
    
def subtract():
    return theinput - theinput2

def multiply():
    return theinput * theinput2

def divide(): 
    return theinput / theinput2

if choose == 'multiply': 
    print(multiply())
elif choose == 'divide':
    print(divide())
elif choose == 'subtract': 
    print(subtract()) 
else: 
    print(addition())