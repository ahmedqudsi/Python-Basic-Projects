# To calculate interest
# formula A=P(1+r/n)^t
p=r=t=0

while p <=0:
    p = float(input("Enter principal amount: $"))
    if p<=0:
        print("Principal amount must be greater than 0.")

  

while r <=0:
    r = float(input("Enter annual interest rate: "))
    if r<=0:
        print("Interest rate must be greater than 0.")
    

while t <=0:
    t = int(input("Enter time in years: "))
    if t<=0:
        print("Time must be greater than 0.")

total = p * pow(1 +r/100, t)
print(f"The total amount after {t} years is: {total:,.2f}")