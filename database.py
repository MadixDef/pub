import sqlite3

def create_db():
    conn = sqlite3.connect('promotions_ads.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS promotions (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    category TEXT,
                    description TEXT,
                    location TEXT,
                    date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS user_preferences (
                    id INTEGER PRIMARY KEY,
                    category TEXT)''')
    conn.commit()
    conn.close()

def insert_promotion(title, category, description, location, date):
    conn = sqlite3.connect('promotions_ads.db')
    c = conn.cursor()
    c.execute("INSERT INTO promotions (title, category, description, location, date) VALUES (?, ?, ?, ?, ?)",
              (title, category, description, location, date))
    conn.commit()
    conn.close()

def get_promotions():
    conn = sqlite3.connect('promotions_ads.db')
    c = conn.cursor()
    c.execute("SELECT * FROM promotions")
    promotions = c.fetchall()
    conn.close()
    return promotions
