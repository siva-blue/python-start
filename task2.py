
# a=2000
# a/=4

# print("Value of a after division by 4:", a)

# b=1000
# b*=2
# print("Value of b after multiplication by 2:", b)



print(" basic arithmetic operations calculator")       
print("================================")

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

print("\nSelect operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Floor Division")
print("5. Exponentiation")
print("6. Modulus")

choice = int(input("Enter your choice : "))
 
match choice:
    case 1: 
        print("Addition:", a + b)
    case 2:
        print("Subtraction:", a - b)
    case 3:
        print("Multiplication:", a * b)
    case 4:
        print("Floor Division:", a // b)
    case 5:
        print("Exponentiation:", a ** b)
    case 6:
        print("Modulus:", a % b)
        
        
        
