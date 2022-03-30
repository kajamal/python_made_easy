my_age = input("Enter your age: ")
interest_percentage = input("Enter Interest Rate: ")
print("My age is:", my_age, type(my_age))  # str
print("Interest Percentage:", my_age, type(interest_percentage)) # int

my_age = int(my_age) # Typecasting to int
interest_percentage = float(interest_percentage) # Typecasting to float

if my_age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote. You are eligible to vote after", 18 - my_age, " years")

if interest_percentage > 8:
    print("Too high")
elif interest_percentage >=5 and interest_percentage <= 8:
    print("Acceptable")
else:
    print("OK")
