import argparse
import logging
import time
import json
from binance.client import Client

# =========================
# 🔑 ADD YOUR NEW API KEYS HERE
# =========================
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET"

# =========================
# LOGGING
# =========================
logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# CLIENT + TIME FIX ✅
# =========================
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# ✅ CORRECT timestamp fix
server_time = client.get_server_time()
system_time = int(time.time() * 1000)
client.timestamp_offset = server_time['serverTime'] - system_time

# =========================
# VALIDATION
# =========================
def validate(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT")

# =========================
# PLACE ORDER
# =========================
def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error: {e}")
        raise

# =========================
# MAIN
# =========================
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate(args.symbol, args.side, args.type, args.quantity, args.price)

        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ SUCCESS")
        print("================================")

        if order:
            print(json.dumps(order, indent=4))
        else:
            print("⚠️ Empty response — check API/Testnet")

        print("================================\n")

    except Exception as e:
        print("\n❌ ERROR:", e)

# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()
