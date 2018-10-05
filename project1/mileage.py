#This program helps to calculate miles per gallon (MPG)

s_mile = input("Please input in a number for starting mileage. ")
e_mile = input("Please input in a number for ending mileage. ")
gas = input("Please input a number to take in as ____ gallons consumed. ")

total = (float(e_mile) - float(s_mile))/float(gas)
print ("The car's MPG is: %.3f MPG." % (total))
