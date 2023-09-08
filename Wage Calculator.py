#This program will tell you how muchh money you make
#This program was made by James F. Shields on 08 September 2023
wage = float(input("Enter hourly wage"))
hours = float(input("Enter hours worked per week"))
weeks = float(input("How many weeks do you work"))
gain = float(input("What is your monthly capital gains income?"))
tax =float(input("What is your tax rate with percent?"))
earn = (wage*hours*weeks) + (gain*12)*(tax/100)
print("Your yearly income is",earn, "USD")