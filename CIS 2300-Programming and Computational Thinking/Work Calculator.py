#Calculate my payment for work
def calculate_pay(rate,hours):
    if hours<=40:
        return rate*hours
    else:
        return (40*rate)+(hours-40)*1.5*rate
def main():
    rate=float(input("Enter the Pay rate:\n"))
    hours=float(input("Enter hours worked:\n"))
    print("The total pay is: $"+str(calculate_pay(rate,hours)))
    
main()
