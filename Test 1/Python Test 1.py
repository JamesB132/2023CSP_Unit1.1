# Follow the instructions in the lab document to calculate the mortgage information.
# Everytime you have a new value to output to the screen, make sure to use the proper variable from below.
# Starting data and variable setup - DO NOT EDIT
principal = 250000
annualRate = 4.85
numYears = 30
monthlyPayment = 0
totalPayments = 0
totalInterest = 0
# All student work should be between this and the output section.
#DO NOT EDIT ABOVE HERE

#monthly payment

numMonths = numYears * 12
monthlyRate = annualRate * .01 / 12

monthlyPayment = ((monthlyRate * (1 + monthlyRate)**numMonths) / ((1 + monthlyRate)**numMonths - 1)) * principal

#total payments

totalPayments = monthlyPayment * numMonths

#total interest

totalInterest = totalPayments - principal


#DO NOT EDIT BELOW HERE
#Output the data after your calculations here:
print("Principle: " + str(principal))
print("Annual rate: " + str(annualRate))
print("Number of Years: " + str(numYears))
print("Monthly Payment: " + str(monthlyPayment))
print("Total Payments: " + str(totalPayments))
print("Total Interest: " + str(totalInterest))