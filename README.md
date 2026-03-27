# Binance Futures Testnet Trading Bot

## 📌 Overview
This is a Python CLI-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

## ⚙️ Setup

1. Install Python (3.x)

2. Install dependency:
pip install python-binance

3. Get API keys from:
https://testnet.binancefuture.com

4. Add keys in bot.py:
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"

---

## ▶️ Run Commands

### MARKET Order
python bot.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

### LIMIT Order
python bot.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000

---

## ✅ Features

- BUY & SELL support
- MARKET & LIMIT orders
- CLI input (argparse)
- Input validation
- Logging (requests, responses, errors)
- Error handling

---

## 📁 Files

- bot.py
- trading_bot.log
- README.md

---

## 🧠 Notes

- Minimum order value must be ≥ 100 USDT
- Uses Binance Futures Testnet (no real money)

---

## 📊 Sample Output

{
  "orderId": 123456,
  "status": "NEW",
  "symbol": "BTCUSDT"
}
