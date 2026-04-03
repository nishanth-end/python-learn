print("Welcome to tip calculator")
bill=int(input("What was the total bill? $"))
tip=int(input ("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
per=tip/100
total=bill+bill*per
each=total/people
print("Each person should pay: $"+str(round(each,2)))
