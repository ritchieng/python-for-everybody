score = raw_input("Your score: ")

try:
    score_int = float(score)
    # If try fails, except runs.
except:
    score_int = -1

if 0.90 <= score_int <= 1.00:
    print "A"
elif 0.80 <= score_int < 0.90:
    print "B"
elif 0.70 <= score_int < 0.80:
    print "C"
elif 0.60 <= score_int < 0.70:
    print "D"
elif 0.00 <= score_int < 0.60:
    print "F"
else:
    print "Please enter a score between 0.00 and 1.00."