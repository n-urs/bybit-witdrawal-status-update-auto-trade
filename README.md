# Bybit Withdrawal Status Update & Auto-Trade


In this particular example, a Python/Playwright utility that continuously monitors Bybit’s BSC (BEP20) withdrawal status, plays an alert sound when it flips to **“Normal”**, and simultaneously executes an **Open Long** order on the ZKJ\_USDT futures market at Ourbit. You can change the network, Trading pair, Exchange URL, trade direction suitable to ypur own needs

---

## 🔎 Features

* **Real-time monitoring** of Bybit’s deposit/withdrawal page
* **Automated refresh** every 2 seconds
* **Targeted check** for the BSC (BEP20) withdrawal status
* **Instant alert** via `sound.mp3` once status becomes “Normal”
* **Simultaneous trade**: opens a new page on Ourbit and clicks **Open Long**

---

## 🚀 Getting Started

### 1. Prerequisites

* Python **3.8+**
* [Playwright](https://playwright.dev/python/)
* `playsound` for MP3 playback

### 2. Clone the repository

```bash
git clone https://github.com/<your-username>/bybit-withdrawal-status-update-auto-trade.git
cd bybit-withdrawal-status-update-auto-trade
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Place your alert sound

Ensure an `sound.mp3` file is in the project root (next to `monitor_and_trade.py`).

---

## ⚙️ Usage

```bash
python monitor_and_trade.py
```

* A Chromium browser window will open two tabs side by side:

  1. **Bybit**: watching the BSC withdrawal status
  2. **Ourbit**: ready to place the **Open Long** order
* Every 2 seconds the script refreshes Bybit’s status.
* As soon as it reads **“Normal”**, it will:

  1. Play `sound.mp3`
  2. Click **Open Long** on the Ourbit tab
  3. Exit after a brief pause

---

## 🛠 Configuration

* **BYBIT\_URL**: Bybit monitor page
* **OURBIT\_URL**: Ourbit trading page
* **SOUND\_FILE**: MP3 filename for the alert
* Adjust selectors in `monitor_and_trade.py` if Bybit or Ourbit update their DOM structure.

---

## ⚖️ License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
