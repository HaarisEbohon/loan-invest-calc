import sys
import os

# Add the parent folder (where main.py is) to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import simple_interest, compound_interest, loan_payment

def test_simple():
    assert round(simple_interest(1000, 0.05, 2), 2) == 1100.00

def test_compound():
    assert round(compound_interest(1000, 0.05, 2), 2) == 1102.50

def test_emi_zero_rate():
    assert round(loan_payment(1200, 0.0, 1), 2) == 100.00
