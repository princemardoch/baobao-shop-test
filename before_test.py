import json
import base64
import logging
import sqlite3

from logging_setup import logging_




def blob_create():
    with open('product.png', 'rb') as r:
        img_data = r.read()
        return img_data

def create_table():
    try:
        with sqlite3.connect('test.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE test(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                test blob )''')
    except sqlite3.OperationalError as e:
        logging.error(e)
        return 'failed_create'
    except Exception as e:
        logging.critical(e)
        return 'unknown_error'

def insert(json):
    try:
        with sqlite3.connect('test.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
        INSERT INTO test (test) VALUES(?)
    ''', (json,))
            conn.commit()
        print('ok')
        return 'success_write'
    except sqlite3.OperationalError as e:
        logging.warning(e)
        return 'wirte_failed'
    except Exception as e:
        logging.critical(e)
        return 'unknown_error'
    
if __name__ == '__main__':
    img = blob_create()
    with open('product_.jpg', 'w+') as w:
        w.write(img)