from tabulate import tabulate

# --- Calculation functions ---

def simple_interest(principal, rate, years):
    """Simple interest: A = P * (1 + r * t)"""
    return principal * (1 + rate * years)

def compound_interest(principal, rate, years):
    """Compound interest: A = P * (1 + r)^t"""
    return principal * (1 + rate) ** years

def loan_payment(principal, annual_rate, years):
    """Monthly loan payment using EMI formula"""
    monthly_rate = annual_rate / 12
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    emi = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return emi

def growth_table(principal, rate, years):
    """Generate a year-by-year investment growth table"""
    data = []
    amount = principal
    for year in range(1, years + 1):
        amount *= (1 + rate)
        data.append([year, f"${amount:,.2f}"])
    return data

# --- Program starts here ---
print("=== Loan & Investment Calculator ===")
p = float(input("Enter principal amount ($): "))
r = float(input("Enter annual interest rate (%): ")) / 100
t = int(input("Enter time in years: "))

si = simple_interest(p, r, t)
ci = compound_interest(p, r, t)
emi = loan_payment(p, r, t)
growth = growth_table(p, r, t)

summary = [
    ["Principal", f"${p:,.2f}"],
    ["Simple Interest Total", f"${si:,.2f}"],
    ["Compound Interest Total", f"${ci:,.2f}"],
    ["Monthly Loan Payment (EMI)", f"${emi:,.2f}"],
]

print("\n--- Summary ---")
print(tabulate(summary, tablefmt="grid"))

print("\n--- Investment Growth (Compound) ---")
print(tabulate(growth, headers=["Year", "Balance"], tablefmt="fancy_grid"))
