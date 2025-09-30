#!/usr/bin/env python3
"""
IRPF Calculator for Spanish Tax System
Calculates estimated tax results based on employment and freelance income
"""

class IRPFCalculator:
    """Calculator for Spanish IRPF (Income Tax)"""
    
    # 2024 IRPF tax brackets (Estado + Autonómico - using average rates)
    TAX_BRACKETS = [
        (12450, 0.19),
        (20200, 0.24),
        (35200, 0.30),
        (60000, 0.37),
        (300000, 0.45),
        (float('inf'), 0.47)
    ]
    
    def __init__(self):
        self.employment_income = 0
        self.employment_withholding = 0
        self.freelance_income = 0
        self.freelance_withholding = 0
        self.deductible_expenses = 0
    
    def add_employment_income(self, net_monthly, withholding_rate, months=12):
        """
        Add employment income
        
        Args:
            net_monthly: Net monthly salary
            withholding_rate: Withholding rate (e.g., 0.20 for 20%)
            months: Number of months
        """
        gross_monthly = net_monthly / (1 - withholding_rate)
        self.employment_income = gross_monthly * months
        self.employment_withholding = gross_monthly * months * withholding_rate
    
    def add_freelance_income(self, gross_income, withholding_rate=0.15):
        """
        Add freelance income from invoices
        
        Args:
            gross_income: Total gross income from invoices
            withholding_rate: Withholding rate applied (default 15%)
        """
        self.freelance_income = gross_income
        self.freelance_withholding = gross_income * withholding_rate
    
    def set_deductible_expenses(self, expenses):
        """Set deductible expenses for freelance activity"""
        self.deductible_expenses = expenses
    
    def calculate_tax(self, taxable_income):
        """Calculate tax based on progressive brackets"""
        tax = 0
        previous_bracket = 0
        
        for bracket_limit, rate in self.TAX_BRACKETS:
            if taxable_income <= previous_bracket:
                break
            
            taxable_in_bracket = min(taxable_income, bracket_limit) - previous_bracket
            tax += taxable_in_bracket * rate
            previous_bracket = bracket_limit
            
            if taxable_income <= bracket_limit:
                break
        
        return tax
    
    def calculate_result(self):
        """
        Calculate estimated tax result
        
        Returns:
            dict with calculation details
        """
        # Calculate net freelance income (after expenses)
        net_freelance = self.freelance_income - self.deductible_expenses
        
        # Total taxable income
        taxable_income = self.employment_income + net_freelance
        
        # Calculate total tax liability
        total_tax = self.calculate_tax(taxable_income)
        
        # Total withholdings
        total_withholdings = self.employment_withholding + self.freelance_withholding
        
        # Result (negative = to pay, positive = refund)
        result = total_withholdings - total_tax
        
        return {
            'employment_income': self.employment_income,
            'freelance_gross': self.freelance_income,
            'deductible_expenses': self.deductible_expenses,
            'freelance_net': net_freelance,
            'total_taxable': taxable_income,
            'total_tax': total_tax,
            'employment_withholding': self.employment_withholding,
            'freelance_withholding': self.freelance_withholding,
            'total_withholdings': total_withholdings,
            'result': result,
            'status': 'A DEVOLVER' if result > 0 else 'A PAGAR'
        }
    
    def simulate_withholding_change(self, new_withholding_rate):
        """
        Simulate changing freelance withholding rate
        
        Args:
            new_withholding_rate: New withholding rate to test
        
        Returns:
            dict with results for the new rate
        """
        original_withholding = self.freelance_withholding
        self.freelance_withholding = self.freelance_income * new_withholding_rate
        
        result = self.calculate_result()
        result['new_withholding_rate'] = new_withholding_rate
        
        # Restore original
        self.freelance_withholding = original_withholding
        
        return result


def main():
    """Example usage of the calculator"""
    calc = IRPFCalculator()
    
    # Example: Employment income (500€ net/month with 20% withholding)
    calc.add_employment_income(net_monthly=500, withholding_rate=0.20, months=12)
    
    # Example: Freelance income (assuming Q3 invoices)
    # User should replace these values with actual data
    calc.add_freelance_income(gross_income=15000, withholding_rate=0.15)
    
    # Example: Deductible expenses (estimate)
    calc.set_deductible_expenses(3000)
    
    # Calculate with current withholding (15%)
    print("=== CÁLCULO ACTUAL (15% retención facturas) ===")
    result_current = calc.calculate_result()
    for key, value in result_current.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}€")
        else:
            print(f"{key}: {value}")
    
    print("\n=== SIMULACIÓN CON 30% RETENCIÓN ===")
    result_30 = calc.simulate_withholding_change(0.30)
    for key, value in result_30.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}€")
        else:
            print(f"{key}: {value}")
    
    print(f"\nDiferencia en resultado: {result_30['result'] - result_current['result']:.2f}€")


if __name__ == "__main__":
    main()
