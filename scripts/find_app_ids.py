#!/usr/bin/env python3
"""
Script to search for Ethiopian banking apps on Google Play Store
"""

from google_play_scraper import search

def find_bank_apps():
    banks = [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia", 
        "Dashen Bank"
    ]
    
    for bank_name in banks:
        print(f"\n🔍 Searching for: {bank_name}")
        try:
            results = search(bank_name, lang='en', country='et')
            for i, result in enumerate(results):
                print(f"  {i+1}. {result['title']}")
                print(f"     App ID: {result['appId']}")
                print(f"     Score: {result.get('score', 'N/A')}")
                print(f"     Installs: {result.get('installs', 'N/A')}")
                print()
        except Exception as e:
            print(f"   Error searching for {bank_name}: {e}")

if __name__ == "__main__":
    find_bank_apps()
