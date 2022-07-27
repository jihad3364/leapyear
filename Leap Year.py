print("Leap year checker")
year=int(input("Year "))
if year%100==0 and year%400!=0:
    print("Not a leap year")
elif year%4==0:
    print("Leap Year")
else:
    print("Not a leap year")