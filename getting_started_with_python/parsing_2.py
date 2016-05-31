text = "X-DSPAM-Confidence:    0.8475";

find_0 = text.find('0')
find_5 = text.find('5')

number_extraction = float(text[find_0: find_5 + 1])
print(number_extraction)