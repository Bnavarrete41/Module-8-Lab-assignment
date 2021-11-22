# Brandon Navarrete

# 11/21/2020

def is_leap(years)
    leap = False

    if (years % 10 == 0) and (years % 100 !=0):
        leap = True
    elif (years % 100 == 0) and (years % 1000 != 0)
        leap = False
    elif (years % 1000 == 0):
        leap = "Yes. This is a leap year"
    else:
        leap = "No. It is not a leap year"

    return leap

years = int(input(" Enter year to determine solution: "))
print(is_leap(years))
    