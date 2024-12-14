while True:

 num1 = float(input("Enter First Number >> "))
 num2 = float(input("Enter Second Number >> "))

 print("""
What You Want To Do?
Choose:
+.Addition
-.Subtraction
*.Multiplication
/.Division
%.Reminder
**.Power
!.Exit""")

 choice = (input("Make a Choice : "))
 if choice == "+":
    add = num1 + num2 
    print(f"Addition is {add}")
 elif choice == "-":
    sub = num1 - num2
    print(f"Subtraction is {sub}")
 elif choice == "*":
    mul = num1 * num2
    print(f"Multiplication is {mul}")
 elif choice == "/":
    div = num1  / num2
    print(f"Division is {div}")
 elif choice == "%":
    rem = num1%num2
    print(f" Reminder id {rem}")
 elif choice == "**":
        pow = num1 ** num2
        print(f"Power is {pow}")
 elif choice == "!":
     print("Thanks for using Calculator")
 else:
     print("Wrong Choice")
 response = (input("Enter ! to Exit:"))
 if response == "!":
  break

