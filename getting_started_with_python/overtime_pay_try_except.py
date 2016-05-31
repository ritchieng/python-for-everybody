# Employees get 1.5x the hourly rate for hours work above 40 hours.
# Error message for non-number input.
# One prompt then quit. No loop for this!

# Concepts: if, elif, else, try, except, input and print


hrs = raw_input("Enter Hours: ")
hrs_int = float(hrs)

hourly_rate = raw_input("Hourly Rate: ")
hourly_rate_int = float(hourly_rate)
overtime_multiplier = 1.5
hourly_overtime = hourly_rate_int * overtime_multiplier

if hrs_int <= 40:
    gross_pay = hrs_int * hourly_rate_int
    print gross_pay
else:
    hrs_over = hrs_int - 40
    gross_pay_overtime = (40 * hourly_rate_int) + (hrs_over * hourly_overtime)
    print gross_pay_overtime

