customer='Arun'
product='Laptop'
price=50000.00
quantity=2


customer=input("Enter Customer Name :")
product=input("Enter Product Name :")
price=float(input("Enter Price:"))
quantity=int(input("Enter Quantity :"))

total=price*quantity

print('\n YOUR ORDER')
print('==========')
print("Customer Name :",customer)
print("Product Details :",product)
print("Price:", price)
print("Quantity :", quantity)
print("FInal Bill:",total)
