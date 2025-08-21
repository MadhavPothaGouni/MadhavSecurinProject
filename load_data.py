import json
import sqlite3

# Connect to SQLite
conn = sqlite3.connect("recipes.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent TEXT,
    country_state TEXT,
    cuisine TEXT,
    title TEXT,
    url TEXT,
    rating REAL,
    total_time INTEGER,
    prep_time INTEGER,
    cook_time INTEGER,
    description TEXT
)
""")

# Load JSON
with open("US_recipes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Insert records
for recipe in data.values():   # <-- important fix
    cur.execute("""
    INSERT INTO recipes (continent, country_state, cuisine, title, url, rating, total_time, prep_time, cook_time, description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        recipe.get("Contient"),
        recipe.get("Country_State"),
        recipe.get("cuisine"),
        recipe.get("title"),
        recipe.get("URL"),
        recipe.get("rating"),
        recipe.get("total_time"),
        recipe.get("prep_time"),
        recipe.get("cook_time"),
        recipe.get("description"),
    ))

conn.commit()
conn.close()
