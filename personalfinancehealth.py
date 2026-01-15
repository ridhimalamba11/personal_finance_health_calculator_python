try:
    
    name = input("Enter your name: ")
    mincome = int(input("Enter your monthly income: "))
    mexpense = int(input("Enter your monthly expense: "))

   
    def check_health(mincome, mexpense):
        savings = mincome - mexpense
        sratio = (savings / mincome) * 100

        if sratio > 30:
            status = "Excellent"
        elif sratio > 20:
            status = "Good"
        elif sratio > 10:
            status = "Warning"
        else:
            status = "Critical"

        return savings, sratio, status

  
    savings, sratio, status = check_health(mincome, mexpense)

    
    personalfinance = {
        "name": name,
        "mincome": mincome,
        "mexpense": mexpense,
        "savings": savings,
        "sratio": sratio,
        "status": status
    }

 
    print(" Financial Report/n")
    print(f"Name: {personalfinance['name']}")
    print(f"Savings: {personalfinance['savings']}")
    print(f"Savings Ratio: {personalfinance['sratio']}%")
    print(f"Status: {personalfinance['status']}")

except ValueError:
    print("Error: Please enter valid numeric values.")
except ZeroDivisionError:
    print("Error: Income cannot be zero.")
