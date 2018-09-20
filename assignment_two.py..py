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
rate = rate / 100 / 12
car_loan = car_loan * 12
monthly_payment = (rate * car_loan) / (1 - (1 + rate) ** -car_loan)



