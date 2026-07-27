user_input = input("Enter an integer: ")

try:
    number = int(user_input)
    print("valid integer:", number)

except ValueError:
    print("Invalid integer")