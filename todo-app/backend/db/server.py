import sqlite3 

conn = sqlite3.connect('todo.db')
curs = conn.cursor() 

def insert_into_db(item: str, priority: int): 

    insert_query = f"""
        INSERT INTO items(item, priority) 
        VALUES ('{item}', {priority});
    """

    curs.execute(insert_query)
    conn.commit()

def delete_from_db(key: int): 

    delete_query = f"""
        DELETE FROM items WHERE id = {key}; 
    """

    curs.execute(delete_query)
    conn.commit() 

insert_into_db('test', 1)
insert_into_db("not working", 2)

delete_from_db(2)