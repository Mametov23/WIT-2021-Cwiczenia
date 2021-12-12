def is_numeric(arg):
    return isinstance(arg, (int, float))



def is_negative(num):
    return num < 0


def calculate_savings(starting_amount, monthly_payment, monthly_deductions):
    if not is_numeric(starting_amount) or not is_numeric(monthly_payment) or not is_numeric(monthly_deductions):
        raise ValueError("All arguments must be numeric.")
    
    if is_negative(starting_amount) or is_negative(monthly_payment) or is_negative(monthly_deductions):
        raise ValueError("All arguments must be positive numbers.")
    
    return starting_amount + 12 * (monthly_payment - monthly_deductions)
    