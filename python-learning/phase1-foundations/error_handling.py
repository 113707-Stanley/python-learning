try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Success! Result is {result}")
finally:
    print("Always runs!")