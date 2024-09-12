monthly_income = float(input("what is your monthly income?"))
monthly_expenses = float(input("what are your monthly expenses?")) 
monthly_savings = monthly_income - monthly_expenses
annual_savings =  monthly_savings * 12
projected_savings_with_interest = annual_savings + (annual_savings * 0.05)
print(f"projectedsavings after one year, with interest, is : {projected_savings_with_interest}")


          