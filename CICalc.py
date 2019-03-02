print("Welcome User,")
print("This is a compound interest calculator, made by a student for more students.")
principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate(in %): "))
time_period = float(input("Enter the time period(in Years): "))
amount = 0
amount = principal*((1+(rate/100))**time_period)
print(amount)
amount = 0
