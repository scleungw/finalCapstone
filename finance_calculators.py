# Apply math module
import math

# Request the user to choose either investment or bond they want to do and store the selection into variable called calculation
# The menu introduce the difference of two calculations
calculation=str(input('''Choose either \'investment\' or \'bond\' from the menu below to proceed: \n
investment \t -\tto calculate the amount of interest you'll earn on your investment
bond \t\t - \tto calculate the amount you'll have to pay on a home loan \n'''))

# Standardise the selection input into a recognised valid input by changing all characters into lower letter
calculation=calculation.lower()

''' Display "Thank you for using our service!" if the user input correct selection
    Display "Sorry. Please make sure you select 'investment' or 'bond'." if the user does not type in a valid input
'''
if calculation == "investment" or calculation=="bond":
    print("\n \tThank you for using our service!\n")
else:
    print("Sorry. Please make sure you select \'investment\' or \'bond\'.")

''' If the user choose 'investment', request the user to input the amount of money the user is depositing and store in a variable called amount.
    Request the user to input the interest rate and store in a variable called rate.
    Request the user to input the number of years they plan on investing and store in a variable called years.
    Request the user to input type of interest plan between 'Simple' and 'Compound' and store in a variable called interest.
    Standardise the interest plan selection input into a recognised valid input by changing all characters into lower letter
    Calculate the interest rate from percentage to decimal place form by dividing it by 100

    After that, to check the user has valid input or not.
    Display "Thank you for your investment!" if the user input correct selection
    Display "Sorry. You have not selected 'simple' or 'compound'." if the user does not type in a valid input
    
    If the user selected 'simple' interest plan, calculate the total amount of money by specific equation.
    Display the result to the user
    If the user selected 'compound' inerest plan, calculate the total amount of money by specific equation.
    Display the result to the user
    If the user did not input a valid selection, display "Please try again and make sure you select 'simple' or 'compound'."
'''
if calculation == "investment":
    amount=float(input("Please enter the amount of money you are depositing: "))
    rate=float(input("Please enter the interest rate (as a percentage so you do not need to enter %) : "))
    years=int(input("Please enter the years of plan on investing: "))
    interest=str(input("Please choose \'simple\' or \'compound\' interest plan: "))
    interest=interest.lower()
    rate=rate/100

    if interest == "simple" or interest=="compound":
        print("\n \tThank you for your investment!\n")
    else:
        print("\n \tSorry. You have not selected \'simple\' or \'compound\'.\n")
    
    if interest== "simple":
        total=amount*(1+rate*years)
        print(f"The total amount once {interest} interest has been applied is: {total}")
    elif interest== "compound":
        total=round(amount*math.pow((1+rate),years),2)
        print(f"The total amount once {interest} interest has been applied is: {total}")
    else:
        print("Please try again and make sure you select \'simple\' or \'compound\'.")

''' If the user choose 'Bond', request the present value of user's house and store into a variable called house_value.
    Request the annual interest rate and store into a variable called rate.
    Request the number of months the user plan to repay the bond and store into a variable called months.
    After that calculate the monthly interest rate by dividing annual interest rate by 12.
    Calculate the monthly repayment by specific equation
    Display the monthly repayment
'''

if calculation=="bond":
    house_value=float(input("Please enter the present value of your house: "))
    rate=float(input("Please enter the interest rate (as a percentage so you do not need to enter %) : "))
    months=int(input("Please enter the number of months you plan to repay the bond: "))

    rate=rate/100/12
    repay=round((rate*house_value)/(1-math.pow((1+rate),-months)),2)
    print(f"\nYou will have to repay {repay} each month.")
   