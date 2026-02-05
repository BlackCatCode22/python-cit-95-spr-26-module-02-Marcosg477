# computpay.py
def computpay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = 40 * rate + overtime * rate * 1.5
    else:
        pay = hours * rate
    return pay

try:
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    pay = computpay(hours, rate)
    print("Pay:", pay)
except ValueError:
    print("Error: Please enter numeric input only.")
