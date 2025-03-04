from flask import Flask, request, jsonify, send_from_directory, Response
from flask_cors import CORS
import json
import sqlite3 

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False


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


def delete_from_db(priority: int): 

    conn = sqlite3.connect('db/todo.db')
    curs = conn.cursor() 

    delete_query = f"""
        DELETE FROM items WHERE priority = {priority}; 
    """

    curs.execute(delete_query)
    conn.commit() 

    conn.close() 


def get_from_db(): 

    conn = sqlite3.connect('db/todo.db')
    curs = conn.cursor() 

    get_query = """
        SELECT * FROM items ORDER BY priority; 
    """

    curs.execute(get_query)
    res = curs.fetchall() 

    conn.close() 

    return res 


# API routing

@app.route('/api/store', methods=['POST'])
def store(): 

    print('Request received at /api/store')

    data = request.get_json()
    item = data['item']
    priority = data['priority']

    # if (not valid_insert): 
    #     rearrange_db()

    insert_into_db(item, priority)

    return jsonify({'message': 'item successfully entered into database!'})


@app.route('/api/items', methods=['GET'])
def items(): 

    print('Request received at /api/items')

    items = get_from_db() 
    
    json_items = {}
    for item in items: 
        json_items[item[1]] = item[2]

    json_data = json.dumps(json_items, sort_keys=False)
    return Response(json_data, mimetype='application/json')


@app.route('/api/delete/<priority>', methods=['DELETE'])
def delete(priority): 

    print('Request received at /api/delete')
    
    delete_from_db(priority)

    return jsonify({'message': 'item successfully deleted'})


if __name__ == '__main__': 
    app.run() 