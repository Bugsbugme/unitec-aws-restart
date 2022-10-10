import webbrowser

pokemon = input("Which pokemon you want?")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

webbrowser.open(url)
