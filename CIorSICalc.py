
def CI():
    principal = float(input("Enter the principal: "))
    rate = float(input("Enter the rate(in %): "))
    time_period = float(input("Enter the time period(in Years): "))
    amount = principal*((1+(rate/100))**time_period)
    print(amount)


def SI():
    principal = float(input("Enter the principal: "))
    rate = float(input("Enter the rate(in %): "))
    time_period = float(input("Enter the time period(in Years): "))
    amount = (principal*rate*time_period)/100
    print(amount)

print("Welcome User,")
print("This is a compound interest and simple interest calculator, made by a student for more students.")

op = input("Enter the operation you want to do (Simple Interest or Compound Interest): ")
if  op.lower() == "si" or "compound interest":
    CI()
elif op.lower() == "si" or "simple interest"