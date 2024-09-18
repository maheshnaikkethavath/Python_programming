def calculate_compound_interest(principal, annual_rate, periods_per_year, years):
    rate_decimal = annual_rate / 100
    # Calculate compound interest
    amount = principal * (1 + rate_decimal / periods_per_year) ** (periods_per_year * years)
    return amount

# Input from the user
principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
periods_per_year = int(input("Enter the number of times interest is compounded per year: "))
years = float(input("Enter the number of years the money is invested: "))
future_value = calculate_compound_interest(principal, annual_rate, periods_per_year, years)
print(f"The amount of money accumulated after {years} years is: ${future_value:.2f}")