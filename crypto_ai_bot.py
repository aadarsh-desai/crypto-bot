import ccxt
import time
import numpy as np
from sklearn.linear_model import LogisticRegression

# ✅ Binance API Setup
exchange = ccxt.binance({
    'apiKey': '6c99a27e5727d38011a37f9ccec4a31a581a9bb7c3c7e8ecf054d7ba1da3abfa',
    'secret': '7c2fde9aa087dc224f6488f31873ff32a67f786ca387bea81e2fc70cbde75f78',
    'enableRateLimit': True
})

symbol = 'SOL/USDT'
leverage = 10
exchange.fapiPrivate_post_leverage({'symbol': symbol.replace("/", ""), 'leverage': leverage})

# ✅ Dummy AI Model Training (Upgrade later with real data)
X = np.array([[50, 30], [60, 40], [55, 35], [45, 25]])  # RSI, MACD dummy
y = np.array([1, 1, 0, 0])  # 1 = Buy, 0 = No Buy
model = LogisticRegression()
model.fit(X, y)

while True:
    try:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        print(f"Live Price: {price}")

        # ✅ Dummy RSI / MACD value (replace with real calculations later)
        rsi = np.random.randint(40, 70)
        macd = np.random.randint(20, 50)

        ai_decision = model.predict([[rsi, macd]])

        if ai_decision[0] == 1:
            print("AI Says: BUY")
            # ✅ Place Buy Order - Test with small qty
            order = exchange.create_market_buy_order(symbol, 0.1)
            print("Buy Executed:", order)

        else:
            print("AI Says: No Trade")

        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(15)
