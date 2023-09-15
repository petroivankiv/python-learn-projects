from crypto_data import get_coins, Coin


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    """Creates an alert for the given price range of a coin"""

    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top:
                # Add the code you want to be executed if a coin reaches
                print(coin, '!!!Вартість збільшилась!!!')
            elif coin.current_price < bottom:
                # Add the code you want to be executed if a coin reaches
                print(coin, '!!!Вартість зменшилась!!!')
            else:
                print(coin)


if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    # Create a loop for these to create live alerts
    alert('btc', bottom=24000, top=25_000, coins_list=coins)
    alert('eth', bottom=1500, top=1600, coins_list=coins)
    alert('xrp', bottom=0.45, top=0.49, coins_list=coins)
    # alert('lunc', bottom=0.41, top=0.65, coins_list=coins)
    alert('crv', bottom=0.3, top=0.5, coins_list=coins)
    alert('mina', bottom=0.25, top=0.55, coins_list=coins)
    alert('gala', bottom=0.01, top=0.02, coins_list=coins)
    alert('cspr', bottom=0.02, top=0.05, coins_list=coins)
    alert('dydx', bottom=1, top=3, coins_list=coins)
    alert('ht', bottom=2, top=5, coins_list=coins)
