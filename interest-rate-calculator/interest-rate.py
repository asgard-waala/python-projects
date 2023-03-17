def main():
    print("This is monthly payment loan calculator.")
    principle = float(input("\nEnter the loan amount: "))
    apr = float(input("\nEnter the rate of interest: "))
    years= int(input("\nEnter the number of years: "))
    monthly_interest_rate = apr/1200
    months = years * 12
    monthly_payment = (principle * monthly_interest_rate)/(1-(1+monthly_interest_rate)**(-months))
    print("\nThe monthly payment for this loan is: %.2f "% monthly_payment,"\n")
main()