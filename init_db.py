import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Table create karo agar nahi hai toh
c.execute('''
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_type TEXT,
        case_number TEXT,
        year TEXT,
        result TEXT
    )
''')

conn.commit()
conn.close()

print("✅ Database and table created successfully.")
