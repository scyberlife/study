print("**Welcome to the program for determining the zodiac sign based on date of birth**")
day = input('Enter day: ')
mon = input('Enter month: ')
# concatenating numeric values as strings provides uniqueness
sum = mon + day
# since input data may contain any characters, we perform a check
if sum.isnumeric():
    sum = int(sum)
    # further exclude non-existent dates and months
    if (31 < int(day)) or (12 < int(mon)):
        sum *= 0
    # two ranges are selected so that it is possible to enter |01.01|1.1|1.01|
    if 11 <= int(sum) <= 19 or 101 <= int(sum) <= 120 or \
            1223 <= int(sum) <= 1231:
        print("Capricorn")
    elif 21 <= sum <= 29 or 121 <= sum <= 219:
        print("Aquarius")
    elif 31 <= sum <= 39 or 220 <= sum <= 320:
        print("Pisces")
    elif 41 <= sum <= 49 or 321 <= sum <= 420:
        print("Aries")
    elif 51 <= sum <= 59 or 421 <= sum <= 521:
        print("Taurus")
    elif 61 <= sum <= 69 or 522 <= sum <= 621:
        print("Gemini")
    elif 71 <= sum <= 79 or 622 <= sum <= 722:
        print("Cancer")
    elif 81 <= sum <= 89 or 723 <= sum <= 821:
        print("Leo")
    elif 91 <= sum <= 99 or 822 <= sum <= 923:
        print("Virgo")
    elif 101 <= sum <= 109 or 924 <= sum <= 1023:
        print("Libra")
    elif 111 <= sum <= 119 or 1024 <= sum <= 1122:
        print("Scorpio")
    elif 121 <= sum <= 129 or 1123 <= sum <= 1222:
        print("Sagittarius")
    else:
        print("Hint: There are no more than 31 days in a month, and there are 12 months in a year,"\
              " and they cannot be 0")
else:
    print("Hint: Values can only consist of integers and positive numbers")
