# number=int(input("Enter your mark: "))

# if number<35:
# print("number is less grade c")
# elif number>35 and number<70:
# print("number is greater than grade b")
# else:
# print("number is greater than grade a")



number=int(input("Enter your mark: "))

if number<35 and number>0:
    print("number is less grade c")
elif number>=35 and number<70:
    print("number is greater than grade b")
else:
    print("number is greater than grade a")