from database import get_db

db = get_db()
db.execute("""
CREATE TABLE IF NOT EXISTS companies (
    id TEXT PRIMARY KEY,
    name TEXT,
    api_key TEXT
)
""")
db.commit()
db.close()
