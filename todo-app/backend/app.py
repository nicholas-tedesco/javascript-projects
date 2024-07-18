from flask import Flask, request, jsonify, send_from_directory
import sqlite3 

app = Flask(__name__, static_folder='../src', static_url_path='')

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


@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/input', methods=['POST'])
def store_input(): 

    data = request.json() 
    item = data.get('item')
    priority = data.get('priority') 

    insert_into_db(item, priority)

    print('that worked')

    return jsonify({'message': 'item successfully entered into database!'})


if __name__ == '__main__': 
    app.run() 