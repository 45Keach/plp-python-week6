def get_number():
    try:
        return int(input("Enter a whole number: "))
    except ValueError:
        return "Not a number"


print(get_number())
