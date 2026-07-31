def add_two_numbers() -> int:
    s=input() # input converts everythig into string
    k=s.split(",") # Split is a dilimmitter it breaks inputted string into separate list but remember they are still a string data type
    num1 = int(k[0]) # Here I a converting every splite that is a list to a int
    num2 = int(k[1])

    return num1 + num2 # here the sum is happeing



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
