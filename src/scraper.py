import pandas as pd
from google_play_scraper import reviews_all, app
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReviewScraper:
    def __init__(self):
        self.reviews_data = []
    
    def scrape_reviews(self, app_id, app_name, count=500):
        logger.info(f"Scraping reviews for {app_name}")
        
        try:
            reviews = reviews_all(
                app_id,
                lang='en',
                country='et',
                count=count,
                filter_score_with=None
            )
            
            for review in reviews:
                self.reviews_data.append({
                    'review_id': review.get('reviewId', ''),
                    'content': review.get('content', ''),
                    'score': review.get('score', 0),
                    'review_date': review.get('at', ''),
                    'app_name': app_name,
                    'app_id': app_id,
                    'source': 'Google Play Store'
                })
            
            logger.info(f"Scraped {len(reviews)} reviews for {app_name}")
            return len(reviews)
            
        except Exception as e:
            logger.error(f"Error scraping {app_name}: {e}")
            return 0
    
    def save_to_csv(self, filename='data/bank_reviews_raw.csv'):
        if not self.reviews_data:
            logger.warning("No reviews to save!")
            return None
        
        df = pd.DataFrame(self.reviews_data)
        df['review_date'] = df['review_date'].astype(str)
        df.to_csv(filename, index=False)
        logger.info(f"Saved {len(df)} reviews to {filename}")
        return df
    
    def get_summary(self):
        if not self.reviews_data:
            return "No reviews scraped yet."
        
        df = pd.DataFrame(self.reviews_data)
        summary = f"""
        Scraping Summary:
        Total Reviews: {len(df)}
        Unique Apps: {df['app_name'].nunique()}
        """
        return summary
