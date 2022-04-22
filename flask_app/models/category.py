import os

#from flask import flash
from flask_app.config.MySQLConnection import connectToMySQL

class Category:
    db = os.environ.get('DATABASE')

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.create_time = data['create_time']
        self.update_time = data['update_time']

#Get Methods -------------------------------------------------------------------
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM categories ORDER BY name;'
        results = connectToMySQL(cls.db).query_db(query)
        categories  = []
        for row in results:
            categories.append(cls(row))
        return categories

    @classmethod
    def get_by_name(cls, name):
        data = {'name': name}
        query = 'SELECT * FROM categories WHERE name = %(name)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return False

#Set Methods -------------------------------------------------------------------
    @classmethod
    def insert(cls, data):
        query = 'INSERT INTO categories (name, create_time, update_time) ' \
            'VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE categories SET name = %(name)s, update_time = NOW() ' \
            'WHERE id = %(category_id)s;'
        connectToMySQL(cls.db).query_db(query, data)
        return 0