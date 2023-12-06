"""
To see if the concept of a slice is making sense, it’s time for a programming challenge. In
this challenge, we start with the following string:
months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
Your job is to write a program that allows the user to enter a month number and
print the three-letter abbreviation for that month. For example, if the user enters 1, the
program should print Jan. If the user enters 12, the program should print Dec.
"""

def calMonths():

    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    monthList = []
    for inx in months:
        if inx.isupper():
            index = months.index(inx)
            mnth = months[index : index + 3]
            months = months[index + 3 : ]

            if mnth not in monthList:
                monthList.append(mnth)

    return monthList

# print(monthList)

def callCalenderMonths():
    while True:
        prompt = input("Enter a number to get the month of that number or press 'ENTER' to quit>> ")
        if prompt == "":
            break
        prompt = int(prompt)
        prompt -= 1
        wantedMonth = calMonths()[prompt]
        print(wantedMonth)

    print("You exited program...")


callCalenderMonths()
