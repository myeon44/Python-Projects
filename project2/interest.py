#This program takes inputs from the user and calculates the compound interest

principal_amount = input("Please input in your principal amount, or initial investment: $")
annual_interest_rate = input("Please input in your annual nominal interest rate as a decimal: ")
num_times = input("Please input in the number of times the interest is compounded per year: ")
num_years = input("Please input in the number of years: ")

#initializes the string taken in by user as integer and float variables
principal_amount = float(principal_amount)
annual_interest_rate = float(annual_interest_rate)
num_times = int(num_times)
num_years = int(num_years)


#variable called total holds the value after calculating compound interest
total = (principal_amount*(1 + (annual_interest_rate/num_times))**(num_times*num_years))


#prints out the total
print ("Final investment is: $%.2f" %(total))
