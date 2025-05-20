import time

def parse_market_data():
    try:
        with open("market_data.txt", "r") as f:
            lines = f.readlines()
        data = {}
        for line in lines:
            if ":" in line:
                key, value = line.strip().split(":")
                data[key.strip()] = float(value.strip())
        return data
    except Exception as e:
        print(f"Error reading market data: {e}")
        return {}

while True:
    data = parse_market_data()
    if not data:
        time.sleep(5)
        continue

    price = data.get("Price")
    ema_10 = data.get("EMA10")
    ema_20 = data.get("EMA20")
    rsi = data.get("RSI")

    if None in (price, ema_10, ema_20, rsi):
        print("Incomplete data, waiting...")
        time.sleep(5)
        continue

    signal = ""
    if ema_10 > ema_20 and rsi > 50:
        signal = "BUY"
    elif ema_10 < ema_20 and rsi < 50:
        signal = "SELL"

    if signal:
        with open("signal.txt", "w") as f:
            f.write(signal)
        print(f"Signal generated: {signal} at price {price}")

    time.sleep(10)
