list = []
persons = ["Person1", "Person2", "Person3", "Person4"]

for index in persons:
    discount = float(input("enter the discount amount: "))
    price = int(input("Enter the tshirt amount: "))
    delivery = int(input("Enter the delivery price: "))

    person1 = price + delivery
    person2 = price + delivery
    person3 = price - discount + delivery
    person4 = price + delivery

    

    list.append( person1)
    list.append( person2)
    list.append( person3)
    list.append( person4)

print(list)




print("===========")
print("siva :",person1)
print("thiru :",person2)
print("moorthy :",person3)
print("bala:",person4)
