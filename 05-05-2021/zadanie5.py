def currency(n):
    switcher = {
        'eur': 4,
        'gbp': 5.26,
        'usd': 3.79,
        'chf': 4.13,
        'jpy100': 3.51 / 100,
    }
    return switcher.get(n);

cash = int(input('podaj ile zlotowek'))
n = input('podaj walute')

wynik = float(cash / currency(n))

print(wynik)