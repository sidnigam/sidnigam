# Roman Numeral Calculator

roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

number = 0

romannumber = "MCMXCIV"

for i in range(len(romannumber)-1):
    print(f"roman number is {roman[romannumber[i]]} and next number is {roman[romannumber[i+1]]}")
    if roman[romannumber[i]] < roman[romannumber[i+1]]:
        number -= roman[romannumber[i]]
    else:
        number += roman[romannumber[i]]

number += roman[romannumber[-1]]

print(number)