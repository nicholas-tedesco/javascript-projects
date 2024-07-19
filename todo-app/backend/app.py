from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3 

app = Flask(__name__)
CORS(app)


# functions to interact with database 

def insert_into_db(item: str, priority: int): 

    conn = sqlite3.connect('db/todo.db')
    curs = conn.cursor() 

    insert_query = f"""
        INSERT INTO items(item, priority) 
        VALUES ('{item}', {priority});
    """

    curs.execute(insert_query)
    conn.commit()

    conn.close() 


def delete_from_db(key: int): 

    conn = sqlite3.connect('db/todo.db')
    curs = conn.cursor() 

    delete_query = f"""
        DELETE FROM items WHERE id = {key}; 
    """

    curs.execute(delete_query)
    conn.commit() 

    conn.close() 


# API routing

@app.route('/api/store', methods=['POST'])
def store(): 

    print('Request received at /api/store')

    data = request.get_json()
    item = data['item']
    priority = data['priority']

    insert_into_db(item, priority)

    return jsonify({'message': 'item successfully entered into database!'})


if __name__ == '__main__': 
    app.run() 