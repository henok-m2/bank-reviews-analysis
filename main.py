#!/usr/bin/env python3
import sys
import os
import time

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scraper import ReviewScraper

def main():
    print("Starting Bank Reviews Scraper...")
    print("=" * 40)
    
    scraper = ReviewScraper()
    
    # Bank apps with their IDs
    bank_apps = {
        'com.combanketh.mobilebanking': 'Commercial Bank of Ethiopia',
        'com.boa.boaMobileBanking': 'Bank of Abyssinia',
        'com.cr2.amolelight': 'Dashen Bank'
    }
    
    print("Target Apps:")
    for app_id, app_name in bank_apps.items():
        print(f"  - {app_name}: {app_id}")
    print()
    
    # Scrape reviews for each bank
    total_reviews = 0
    for app_id, app_name in bank_apps.items():
        count = scraper.scrape_reviews(app_id, app_name, count=400)
        total_reviews += count
        print(f"Scraped {count} reviews for {app_name}")
        time.sleep(2)  # Be nice to the server
    
    # Save data
    df = scraper.save_to_csv()
    
    # Show summary
    print(scraper.get_summary())
    
    if df is not None:
        print("\nSample of data:")
        print(df[['app_name', 'score', 'content']].head(3))

if __name__ == "__main__":
    main()
