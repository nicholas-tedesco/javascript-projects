import sqlite3

conn = sqlite3.connect('todo.db')
curs = conn.cursor()

def print_tables(): 

    select_tables = "SELECT name FROM sqlite_master;"
    results = curs.execute(select_tables)

    print('\nTable Names: ')
    for result in results: 
        print('- ', result[0])

def print_records(): 

    select_query = "SELECT * FROM items;"
    results = curs.execute(select_query)

    print('\nCurrent Records: ')
    for result in results: 
        print(result)

print_tables()
print_records()