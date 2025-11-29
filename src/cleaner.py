import pandas as pd
import numpy as np
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCleaner:
    def __init__(self):
        pass
    
    def load_data(self, filepath='data/bank_reviews_raw.csv'):
        try:
            df = pd.read_csv(filepath)
            logger.info(f"Loaded {len(df)} reviews from {filepath}")
            return df
        except FileNotFoundError:
            logger.error(f"File {filepath} not found")
            return None
    
    def clean_data(self, df):
        logger.info("Starting data cleaning...")
        
        # Make a copy
        clean_df = df.copy()
        
        # 1. Remove duplicates based on review_id
        initial_count = len(clean_df)
        clean_df = clean_df.drop_duplicates(subset=['review_id'], keep='first')
        logger.info(f"Removed {initial_count - len(clean_df)} duplicate reviews")
        
        # 2. Handle missing values
        missing_before = clean_df['content'].isna().sum()
        clean_df = clean_df.dropna(subset=['content'])
        logger.info(f"Removed {missing_before} reviews with missing content")
        
        # 3. Convert and format dates (YYYY-MM-DD as required)
        clean_df['review_date'] = pd.to_datetime(clean_df['review_date'], errors='coerce')
        clean_df['date'] = clean_df['review_date'].dt.strftime('%Y-%m-%d')
        
        # 4. Standardize bank names and create required columns
        bank_mapping = {
            'Commercial Bank of Ethiopia': 'CBE',
            'Bank of Abyssinia': 'BOA', 
            'Dashen Bank': 'Dashen'
        }
        clean_df['bank'] = clean_df['app_name'].map(bank_mapping)
        
        # 5. Create final structure with required columns
        final_df = clean_df[[
            'review_id', 'content', 'score', 'date', 'bank'
        ]].rename(columns={
            'content': 'review_text',
            'score': 'rating'
        })
        
        # Add source column as required
        final_df['source'] = 'Google Play Store'
        
        logger.info(f"Cleaning complete. Final dataset: {len(final_df)} reviews")
        return final_df
    
    def save_clean_data(self, clean_df, filepath='data/bank_reviews_clean.csv'):
        clean_df.to_csv(filepath, index=False, encoding='utf-8')
        logger.info(f"Saved cleaned data to {filepath}")
        
        # Show summary
        print("\n" + "="*50)
        print("📊 CLEANED DATA SUMMARY")
        print("="*50)
        print(f"Total Reviews: {len(clean_df)}")
        print("\nReviews per Bank:")
        bank_counts = clean_df['bank'].value_counts()
        for bank, count in bank_counts.items():
            print(f"  - {bank}: {count} reviews")
        print("\nRating Distribution:")
        rating_counts = clean_df['rating'].value_counts().sort_index()
        for rating, count in rating_counts.items():
            print(f"  - {rating} stars: {count} reviews")
        
        return clean_df

def run_cleaning_pipeline():
    cleaner = DataCleaner()
    
    # Load raw data
    raw_df = cleaner.load_data()
    if raw_df is None:
        return
    
    # Clean data
    clean_df = cleaner.clean_data(raw_df)
    
    # Save cleaned data
    cleaner.save_clean_data(clean_df)

if __name__ == "__main__":
    run_cleaning_pipeline()
