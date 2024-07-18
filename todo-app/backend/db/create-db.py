import sqlite3 

conn = sqlite3.connect('todo.db')
curs = conn.cursor() 

drop_tables = "DROP TABLE IF EXISTS items;"
curs.execute(drop_tables)

make_tables = """
    CREATE TABLE items(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        item VARCHAR(50), 
        priority INTEGER
    );
"""

curs.execute(make_tables)
conn.commit() 

conn.close()