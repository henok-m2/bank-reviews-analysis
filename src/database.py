import psycopg2
from psycopg2 import sql
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self, dbname='bank_reviews', user='henok', 
                 password='rich.com', host='localhost', port='5432'):
        self.connection_params = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Establish connection to PostgreSQL database"""
        try:
            self.conn = psycopg2.connect(**self.connection_params)
            self.cursor = self.conn.cursor()
            logger.info("✅ Connected to PostgreSQL database")
            return True
        except Exception as e:
            logger.error(f"❌ Connection failed: {e}")
            return False
    
    def create_tables(self):
        """Create required tables if they don't exist"""
        try:
            # Create banks table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS banks (
                    bank_id SERIAL PRIMARY KEY,
                    bank_name VARCHAR(50) NOT NULL UNIQUE,
                    app_name VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create reviews table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS reviews (
                    review_id VARCHAR(100) PRIMARY KEY,
                    bank_id INTEGER REFERENCES banks(bank_id),
                    review_text TEXT NOT NULL,
                    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
                    review_date DATE,
                    sentiment_label VARCHAR(20),
                    sentiment_score FLOAT,
                    themes TEXT,
                    source VARCHAR(50),
                    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            self.conn.commit()
            logger.info("✅ Tables created successfully")
            return True
        except Exception as e:
            logger.error(f"❌ Table creation failed: {e}")
            self.conn.rollback()
            return False
    
    def insert_banks(self):
        """Insert bank data into banks table"""
        banks_data = [
            ('CBE', 'Commercial Bank of Ethiopia Mobile'),
            ('BOA', 'Bank of Abyssinia Mobile Banking'),
            ('Dashen', 'Dashen Mobile Banking')
        ]
        
        try:
            for bank_name, app_name in banks_data:
                self.cursor.execute("""
                    INSERT INTO banks (bank_name, app_name) 
                    VALUES (%s, %s)
                    ON CONFLICT (bank_name) DO NOTHING
                """, (bank_name, app_name))
            
            self.conn.commit()
            logger.info(f"✅ Inserted {len(banks_data)} banks")
            return True
        except Exception as e:
            logger.error(f"❌ Bank insertion failed: {e}")
            self.conn.rollback()
            return False
    
    def load_analyzed_data(self, csv_path='data/bank_reviews_analyzed.csv'):
        """Load analyzed data from CSV and insert into database"""
        try:
            df = pd.read_csv(csv_path)
            logger.info(f"📊 Loaded {len(df)} reviews from CSV")
            
            # Get bank_id mapping
            self.cursor.execute("SELECT bank_id, bank_name FROM banks")
            bank_mapping = {row[1]: row[0] for row in self.cursor.fetchall()}
            
            inserted_count = 0
            for _, row in df.iterrows():
                bank_id = bank_mapping.get(row['bank'])
                if bank_id:
                    self.cursor.execute("""
                        INSERT INTO reviews 
                        (review_id, bank_id, review_text, rating, review_date, 
                         sentiment_label, sentiment_score, themes, source)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (review_id) DO NOTHING
                    """, (
                        row['review_id'], bank_id, row['review_text'], 
                        row['rating'], row['date'], row['sentiment_label'],
                        row['sentiment_score'], row['themes'], row['source']
                    ))
                    inserted_count += 1
            
            self.conn.commit()
            logger.info(f"✅ Inserted {inserted_count} reviews into database")
            return inserted_count
        except Exception as e:
            logger.error(f"❌ Data insertion failed: {e}")
            self.conn.rollback()
            return 0
    
    def run_queries(self):
        """Run sample queries to verify data"""
        queries = {
            "Total Reviews": "SELECT COUNT(*) FROM reviews",
            "Reviews per Bank": """
                SELECT b.bank_name, COUNT(r.review_id) as review_count
                FROM banks b
                LEFT JOIN reviews r ON b.bank_id = r.bank_id
                GROUP BY b.bank_name
                ORDER BY review_count DESC
            """,
            "Average Rating per Bank": """
                SELECT b.bank_name, AVG(r.rating) as avg_rating
                FROM banks b
                JOIN reviews r ON b.bank_id = r.bank_id
                GROUP BY b.bank_name
                ORDER BY avg_rating DESC
            """,
            "Sentiment Distribution": """
                SELECT sentiment_label, COUNT(*) as count
                FROM reviews
                GROUP BY sentiment_label
                ORDER BY count DESC
            """
        }
        
        results = {}
        for query_name, query in queries.items():
            try:
                self.cursor.execute(query)
                results[query_name] = self.cursor.fetchall()
                logger.info(f"✅ {query_name} query executed")
            except Exception as e:
                logger.error(f"❌ {query_name} query failed: {e}")
                results[query_name] = None
        
        return results
    
    def close(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        logger.info("✅ Database connection closed")

def main():
    """Main function to run the database setup"""
    db = DatabaseManager()
    
    if db.connect():
        # Create tables
        db.create_tables()
        
        # Insert banks
        db.insert_banks()
        
        # Load analyzed data
        db.load_analyzed_data()
        
        # Run verification queries
        results = db.run_queries()
        
        # Print results
        print("\n" + "="*50)
        print("📊 DATABASE VERIFICATION RESULTS")
        print("="*50)
        
        for query_name, result in results.items():
            print(f"\n{query_name}:")
            if result:
                for row in result:
                    print(f"  {row}")
        
        db.close()

if __name__ == "__main__":
    main()
