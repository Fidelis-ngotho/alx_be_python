income = float(input("what is your monthly income?"))
expenses = float(input("what are your monthly expenses?")) 
savings = float(input("what are your  monthly savings?"))
annual_savings = savings * 12
projected_savings_with_interest = annual_savings + (annual_savings * 0.05)
print(f"projectedsavings after one year, with interest, is : {projected_savings_with_interest}")


          