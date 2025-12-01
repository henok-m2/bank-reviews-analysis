import psycopg2
import pandas as pd

def verify_database():
    conn = psycopg2.connect(
        dbname='bank_reviews',
        user='postgres',
        host='localhost',
        port='5432'
    )
    
    queries = {
        "1. Total Reviews": "SELECT COUNT(*) as total FROM reviews",
        "2. Banks in Database": "SELECT bank_id, bank_name, app_name FROM banks ORDER BY bank_id",
        "3. Reviews per Bank": """
            SELECT b.bank_name, COUNT(r.review_id) as review_count
            FROM banks b
            LEFT JOIN reviews r ON b.bank_id = r.bank_id
            GROUP BY b.bank_name
            ORDER BY review_count DESC
        """,
        "4. Sample Reviews with Sentiment": """
            SELECT r.review_id, b.bank_name, 
                   LEFT(r.review_text, 100) as preview,
                   r.rating, r.sentiment_label, r.themes
            FROM reviews r
            JOIN banks b ON r.bank_id = b.bank_id
            LIMIT 10
        """,
        "5. Database Schema": """
            SELECT table_name, column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position
        """
    }
    
    print("🔍 DATABASE VERIFICATION")
    print("=" * 60)
    
    for name, query in queries.items():
        print(f"\n{name}:")
        try:
            df = pd.read_sql_query(query, conn)
            if len(df) > 0:
                print(df.to_string(index=False))
            else:
                print("No data returned")
        except Exception as e:
            print(f"Error: {e}")
    
    conn.close()
    print("\n" + "=" * 60)
    print("✅ Verification complete!")

if __name__ == "__main__":
    verify_database()
