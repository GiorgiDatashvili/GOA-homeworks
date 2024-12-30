EXCHANGE_RATE_GEL_TO_USD = 0.36 
EXCHANGE_RATE_USD_TO_GEL = 2.8
print("Currency Exchange System")
print("1 to Convert USD to GEL")
print("2 to Convert GEL to USD")
choice = input("Enter 1 or 2: ")
if choice == "1":
    amount_usd = float(input("Enter amount in USD: "))
    print(f"{amount_usd} USD is {amount_usd * EXCHANGE_RATE_USD_TO_GEL} GEL.")
elif choice == "2":
    amount_gel = float(input("Enter amount in GEL: "))
    print(f"{amount_gel} GEL is {amount_gel * EXCHANGE_RATE_GEL_TO_USD} USD.")
else:
    print("Invalid choice. Choose 1 or 2")


    amount_gel = float(input("Enter amount in GEL: "))
    print(f"{amount_gel} GEL is {amount_gel * EXCHANGE_RATE_GEL_TO_USD} USD.")