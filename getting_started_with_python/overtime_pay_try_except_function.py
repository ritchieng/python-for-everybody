# Employees get 1.5x the hourly rate for hours work above 40 hours.
# Error message for non-number input.
# One prompt then quit. No loop for this!

# Concepts: if, elif, else, try, except, input, print, and function


hourly_rate = raw_input("Hourly rate: ")
hourly_rate_int = float(hourly_rate)

hours = raw_input("Number of hours: ")
hours_int = float(hours)


def computepay(h, r):
    overtime_r = r * 1.5

    if h < 40:
        return h * r
    else:
        return (40 * r) + (h - 40) * overtime_r

p = computepay(hours_int, hourly_rate_int)
print p
