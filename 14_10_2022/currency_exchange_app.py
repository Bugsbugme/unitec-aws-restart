import requests
from currency_symbols import CurrencySymbols

# Asking the user to input the currency they want to convert from and to.
basecur = input("Currency to covert: ").lower()
tocur = input("Currency to convert to: ").lower()

# Getting the currency symbol for the currency that the user inputs.
basecur_symbol = CurrencySymbols.get_symbol(basecur.upper())
tocur_symbol = CurrencySymbols.get_symbol(tocur.upper())

# A dictionary that contains the currency symbols for the currencies that are supported by the API.
# symbols = {
#     "gbp": "£",
#     "nzd": "$",
#     "jpy": "¥",
#     "rub": "₽",
#     "eur": "€",
# }

# Getting the data from the API and checking the status code.
res = requests.get(
    f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{basecur}/{tocur}.json"
)
status = res.status_code

# Checking the status code of the API request. If the status code is 200, then it will print the data.
# If the status code is not 200, then it will print an error message.
if status == 200:
    data = res.json()
    # print(f"{symbols[basecur]}1 {basecur} | {symbols[tocur]}{data[tocur]} {tocur}")
    print(
        f"{basecur.upper()} {basecur_symbol}1 | {tocur.upper()} {tocur_symbol}{data[tocur]}"
    )

else:
    print(f"Error: Status Code {status}")
