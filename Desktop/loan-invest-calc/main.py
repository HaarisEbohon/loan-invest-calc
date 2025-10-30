# main.py
from tabulate import tabulate

# -----------------------------
# Functions
# -----------------------------

def simple_interest(principal, rate, years):
    return principal * (1 + rate * years)

def compound_interest(principal, rate, years):
    return principal * (1 + rate) ** years

def loan_payment(principal, annual_rate, years):
    """
    Calculate monthly payment (EMI) for a loan
    principal: loan amount
    annual_rate: annual interest rate (e.g., 0.05)
    years: number of years
    """
    if annual_rate == 0:
        return principal / (years * 12)
    
    monthly_rate = annual_rate / 12
    n = years * 12
    emi = principal * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)
    return emi

def investment_growth(principal, rate, years):
    """Return a list of year-by-year compound balances"""
    balances = []
    for y in range(1, years + 1):
        balances.append(round(compound_interest(principal, rate, y), 2))
    return balances

# -----------------------------
# Main interactive code
# -----------------------------

if __name__ == "__main__":
    print("=== Loan & Investment Calculator ===")
    try:
        p = float(input("Enter principal amount ($): "))
        r = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))
        t = int(input("Enter number of years: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        exit(1)

    si = simple_interest(p, r, t)
    ci = compound_interest(p, r, t)
    emi = loan_payment(p, r, t)
    growth = investment_growth(p, r, t)

    # Print summary table
    summary_table = [
        ["Principal", f"${p:,.2f}"],
        ["Simple Interest Total", f"${si:,.2f}"],
        ["Compound Interest Total", f"${ci:,.2f}"],
        ["Monthly Loan Payment (EMI)", f"${emi:,.2f}"]
    ]
    print("\n--- Summary ---")
    print(tabulate(summary_table, tablefmt="grid"))

    # Print investment growth
    growth_table = [[y + 1, bal] for y, bal in enumerate(growth)]
    print("\n--- Investment Growth (Compound) ---")
    print(tabulate(growth_table, headers=["Year", "Balance"], tablefmt="fancy_grid"))
