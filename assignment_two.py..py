# Liam Neville
# 09/21/19
# This is assignment one for unit two where the user is able to speak with a chatbot about the costs of buying a car

user = input("What is your name?")
print("hello", user)
print("It's so nice to meet you. My name is Chad")
location = input("Where are you from?")
print("Sounds like a god awful to live")
negative_question = input("How can you live in such a dump?")
number = float(input("Whatever. What is your favorite number?"))
print("My favorite number is 8")
print("Your number minus my number is", number - 8)
car = input("I have another question. What is your dream car?")
print("Oh, that's interesting.")
cost = float(input("What is the price of that car?"))
print("That is a reasonably priced car")
car_loan = float(input("How many years would it take to pay off a loan for that car?"))
rate = float(input("What would be the annual interest rate for the car?"))
# This equation calculates the annual interest rate into months
rate = rate / 100 / 12
# This calculates the years to pay off the car loan into months
car_loan = car_loan * 12
# This is the equation that determines how much the user will pay each month for the car
monthly_payment = (rate * cost) / (1 - (1 + rate) ** -car_loan)
print("Your monthly payment would be", monthly_payment)
print("Your total cost for the car is", car_loan * monthly_payment)
print("It was very nice talking with you. Have an awful day!")