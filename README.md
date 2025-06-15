````markdown
# Bybit Withdrawal Status Monitor & Auto-Trade

A lightweight Python & Playwright tool that:

- Opens Bybit’s deposit/withdrawal status page alongside Ourbit’s ZKJ_USDT futures page  
- Polls Bybit every 2 seconds for the **BSC (BEP20)** withdrawal status  
- As soon as status flips to **“Normal”**, it:
  1. Plays your `sound.mp3` alert  
  2. Clicks **Open Long** on the ZKJ_USDT market on Ourbit  
- Exits after confirming the trade and playing the alert  

---

## 🛠️ Requirements

- **Python** 3.8+  
- **Playwright** (for browser automation)  
- **playsound** (for MP3 playback)  

Install dependencies via:

```bash
pip install -r requirements.txt
playwright install
````

---

## 📥 Installation

1. **Clone** the repo

   ```bash
   git clone https://github.com/<your-username>/bybit-withdrawal-status-update-auto-trade.git
   cd bybit-withdrawal-status-update-auto-trade
   ```
2. **Install** Python packages & browser engines

   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. Place your `sound.mp3` in the project root.

---

## 🚀 Usage

```bash
python watch_and_trade.py
```

* **Bybit** tab will auto-refresh and log BSC status every 2s.
* **Ourbit** tab remains open for executing the trade.
* On status = “Normal”:

  * Plays `sound.mp3`
  * Clicks **Open Long** on Ourbit
  * Script exits after a brief pause

---

## ⚙️ Configuration

Edit constants at the top of `watch_and_trade.py` if needed:

```python
BYBIT_URL  = "https://www.bybit.com/en/announcement-info/deposit-withdraw"
OURBIT_URL = "https://futures.ourbit.com/exchange/ZKJ_USDT"
SOUND_FILE = "sound.mp3"
```

---

## 📝 Notes

* You **must** be logged in on both Bybit and Ourbit in your default browser profile.
* The script runs in visible (non-headless) mode for debugging.
* If UI elements change, update the Playwright selectors in the code.

---

## 📄 License

MIT © \[n-urs]

```
```
