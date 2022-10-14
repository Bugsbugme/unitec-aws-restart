import requests
from currency_symbols import CurrencySymbols
from fastapi import FastAPI

app = FastAPI(docs_url="/")

# Asking the user to input the currency they want to convert from and to.
# basecur = input("Currency to covert: ").lower()
# tocur = input("Currency to convert to: ").lower()

# Getting the currency symbol for the currency that the user inputs.
# basecur_symbol = CurrencySymbols.get_symbol(basecur.upper())
# tocur_symbol = CurrencySymbols.get_symbol(tocur.upper())

# A dictionary that contains the currency symbols for the currencies that are supported by the API.
# symbols = {
#     "gbp": "£",
#     "nzd": "$",
#     "jpy": "¥",
#     "rub": "₽",
#     "eur": "€",
# }

# Getting the data from the API and checking the status code.
# res = requests.get(
#     f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{basecur}/{tocur}.json"
# )
# status = res.status_code


@app.get("/currency")
def get_quote(from_cur, to_cur):
    """
    It takes in two parameters, from_cur and to_cur, and returns a string that contains the currency
    symbol for the from_cur and to_cur parameters, and the exchange rate between the two currencies.

    :param from_cur: The currency that the user wants to convert from
    :param to_cur: The currency that the user wants to convert to
    :return: a string that contains the currency symbol for the from_cur and to_cur parameters, and the exchange rate between the two currencies.
    :return: the value of the variable "status"
    """
    # Getting the currency symbol for the currency that the user inputs.
    basecur_symbol = CurrencySymbols.get_symbol(from_cur.upper())
    tocur_symbol = CurrencySymbols.get_symbol(to_cur.upper())

    # Getting the data from the API and checking the status code.
    res = requests.get(
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{from_cur}/{to_cur}.json"  # https://github.com/fawazahmed0/currency-api#readme
    )
    status = res.status_code

    if status == 200:
        data = res.json()
        # print(f"{symbols[basecur]}1 {basecur} | {symbols[tocur]}{data[tocur]} {tocur}")
        # print(
        #     f"{basecur.upper()} {basecur_symbol}1 | {tocur.upper()} {tocur_symbol}{data[tocur]}"
        # )
        return f"{from_cur.upper()} {basecur_symbol}1 | {to_cur.upper()} {tocur_symbol}{data[to_cur]}"

    else:
        # print("Error")
        # print(f"Status Code: {status}")
        return f"Error: Status Code {status}"
