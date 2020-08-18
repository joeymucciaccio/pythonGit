#Joseph Mucciaccio

c = 0
while True:
        dollar_amount = float(input("Enter the amount of money to convert to change: "))
        
        if dollar_amount < 0:
            print("Invalid amount")
            break
        else:
            #for conversion purposes
            conversion = dollar_amount * 100
            
            #conversion for the quarters
            quarter = int(conversion // 25)
            conversion = conversion % 25
            
            #conversion for the dimes
            dime = int(conversion // 10)
            
            #conversion for the pennies
            penny = int(conversion % 10)
            
            total = quarter + dime + penny
            
            print(dollar_amount, "dollars makes", quarter, "quarters", dime, "dimes and", penny, "pennies for a total of", total, "coins")
            c += 1