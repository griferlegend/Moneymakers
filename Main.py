import os
import requests
from bs4 import BeautifulSoup
import time

# Safely mapped inside the code array
DISCORD_WEBHOOK_URL = "https://discord.com"

def auto_deal_hunter():
    print("🤖 Live Web Scraping Engine Initialized...")
    
    # Infinite execution loop that handles the 24/7 automation completely on its own
    while True:
        print("🤖 Bot is executing an automatic live network scan...")
        
        # Unblocked public aggregator stream tracking trapstar and corteiz under £50 by newly listed
        url = "https://ebay.co.uk"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, 'xml') # Parse the live XML data structure
            listings = soup.find_all('item')
            
            items_sent = 0
            
            for item in listings:
                title = item.find('title').text.strip()
                if "shop on ebay" in title.lower():
                    continue
                    
                # Extract the 100% real checkout listing URL link
                link = item.find('link').text.strip()
                
                # Construct the premium card payload packet
                msg = f"⚡ **AUTOMATED RADAR SNIPE (UNDER £50)** ⚡\n\n👕 **Item:** {title}\n👉 [SNIPE THE REAL LISTING NOW]({link})"
                
                # Shoot the data payload packet over to your Moneymakers server
                requests.post(DISCORD_WEBHOOK_URL, json={"content": msg})
                print(f"✅ Auto-dispatched: {title[:25]}...")
                
                items_sent += 1
                if items_sent >= 5: # Lock it perfectly to your 5 per hour rule
                    break
                    
            print("💤 Cycle complete. Bot is entering active background sleep for 1 hour...")
            # Sleep for exactly 3600 seconds (1 hour) before crawling the web again completely on its own
            time.sleep(3600)
            
        except Exception as e:
            print(f"Network Scan Error: {e}")
            time.sleep(60) # Retry in 1 minute if the marketplace drops the connection

if __name__ == "__main__":
    auto_deal_hunter()
