#!/usr/bin/env python3
"""
1) Open Bybit’s Deposit/Withdrawal page and Ourbit’s TOKEN_USDT futures page side by side.
2) Keep Ourbit open the whole time.
3) Monitor withdrawal status on Bybit every 1.5s.
4) As soon as it flips to “Normal”, play sound.mp3 and click “Open Long” on Ourbit—simultaneously.
"""

import time
import threading
from playsound import playsound
from playwright.sync_api import sync_playwright

BYBIT_URL   = "https://www.bybit.com/en/announcement-info/deposit-withdraw"
OURBIT_URL  = "https://futures.ourbit.com/exchange/TOKEN_USDT"   #INPUT YOUR EXCHANGE AND/OR TOKEN NAME
SOUND_FILE  = "sound.mp3"

def play_alert_sound():
    try:
        playsound(SOUND_FILE)
    except Exception as e:
        print(f"⚠️ Could not play sound.mp3: {e}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Open both pages and keep them alive
        bybit = browser.new_page()
        bybit.goto(BYBIT_URL)
        
        ourbit = browser.new_page()
        ourbit.goto(OURBIT_URL)

        # Prepare Bybit: wait for the refresh icon, expand ZKJ → BSC row
        bybit.wait_for_selector('span[aria-label="redo"]', timeout=15000)
        expand_btn = bybit.locator('tr:has-text("ZKJ Polyhedra Network") button')
        if expand_btn.count():
            expand_btn.first.click()
            bybit.wait_for_selector('td:has-text("BSC (BEP20)")') # SPECIFY WHICH DEPOSIT/WITHDRAWAL CHAIN TO MONITOR

        print("▶ Monitoring BSC withdrawal status on Bybit …")

        while True:
            # Click Bybit’s reload icon
            bybit.click('span[aria-label="redo"]')
            bybit.wait_for_timeout(500)  # wait for update

            # Extract only the BSC withdrawal-status text
            status = bybit.locator(
                '//td[text()="BSC (BEP20)"]'
                '/following-sibling::td[5]'
                '//span[starts-with(@class,"announcement-info-userasset_statusText")]'
            ).inner_text().strip()

            ts = time.strftime("%H:%M:%S")
            print(f"[{ts}] BSC Withdrawal Status → {status}")

            if status.lower() == "normal":
                print("✅  BSC is now NORMAL!  Triggering alert & Open Long…")

                # 1) Play sound in background
                threading.Thread(target=play_alert_sound, daemon=True).start()

                # 2) Click Open Long on Ourbit
                ourbit.wait_for_selector(
                    'button[data-testid="contract-trade-open-long-btn"]',
                    timeout=15000
                )
                ourbit.click('button[data-testid="contract-trade-open-long-btn"]')
                print("▶ Clicked Open Long on Ourbit.")

                break

            # wait rest of 2s cycle
            bybit.wait_for_timeout(500)

        # leave both pages open for a bit so you can see
        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    main()
