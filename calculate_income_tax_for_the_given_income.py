# Calculate income tax for the given income

# Given income
income = 45000

# Income tax rates
rate1 = 0
rate2 = 10
rate3 = 20

# Income tax slabs
slab1 = 10000
slab2 = 10000

if income <= 10000:
    # No tax for income up to 10,000
    tax_payable = 0
elif income <= 20000:
    # Calculate 10% tax on income between 10,000 and 20,000
    taxable_amount = income - 10000
    tax_payable = taxable_amount * 10 / 100
else:
    # No tax for the first 10,000
    tax_payable = 0

    # Calculate 10% tax on the next 10,000
    tax_payable += 10000 * 10 / 100

    # Calculate 20% tax on the remaining income
    remaining_income = income - 20000
    tax_payable += remaining_income * 20 / 100

print(f"For a taxable income of ${income}, the income tax payable is: ${tax_payable}")