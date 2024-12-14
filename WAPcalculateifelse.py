num = int(input("Enter Your Number >>"))
num1 = int(input("Enter Your Number >>"))

if num == num1:
    print("They are same")
    sum = num + num1
    print(sum)
elif num<num1:
    print(num1,"is Less Than",num)
    sum = num + num1
    print(sum)
else:
    print(num,"is Greater Than",num1)
    sum =num + num1
    print(sum)     