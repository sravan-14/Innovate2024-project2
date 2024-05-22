from currency_converter import CurrencyConverter


def main():
    print("\tThis is currency converter\t")
    print("use country currencys codes like USD,INR,JPY,EUR ect\n")
    amount = int (input("Enter the Amount:"))
    from_currency=input("From Currency code :").upper()
    to_currency=input("to Currency code :").upper()
   
    c=CurrencyConverter()
    converted_amount = c.convert(amount , from_currency , to_currency)
    print(f"This {amount} {from_currency} in {to_currency} is :{converted_amount}")

main()