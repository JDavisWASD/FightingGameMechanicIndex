import os

#from flask import flash
from flask_app.config.MySQLConnection import connectToMySQL
from flask_app.models.game import Game

class Mechanic:
    db = os.environ.get('DATABASE')

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.alternative = data['alternative']
        self.has_data = data['has_data']
        self.category_id = data['category_id']
        self.create_time = data['create_time']
        self.update_time = data['update_time']

# Get Methods -------------------------------------------------------------------
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM mechanics ORDER BY name;'
        results = connectToMySQL(cls.db).query_db(query)
        mechanics = []
        for row in results:
            mechanics.append(cls(row))
        return mechanics

    @classmethod
    def get_by_any_name(cls, name):
        data = {'name': name}
        query = 'SELECT * FROM mechanics WHERE name = %(name)s OR ' \
            'alternative = %(name)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return False

#    @classmethod
#    def get_by_name(cls, name):
#        data = {'name': name}
#        query = 'SELECT * FROM mechanics WHERE name = %(name)s;'
#        result = connectToMySQL(cls.db).query_db(query, data)
#        if result:
#            return cls(result[0])
#        return False

#    @classmethod
#    def get_by_alternative(cls, alt):
#        data = {'alt': alt}
#        query = 'SELECT * FROM mechanics WHERE alternative = %(alt)s;'
#        result = connectToMySQL(cls.db).query_db(query, data)
#        if result:
#            return cls(result[0])
#        return False

# Set Methods ------------------------------------------------------------------
    @classmethod
    def insert(cls, data):
        query = 'INSERT INTO mechanics (name, alternative, has_data, ' \
            'category_id, create_time, update_time) VALUES (%(name)s, ' \
            '%(alternative)s, %(has_data)s, %(category_id)s, NOW(), NOW());'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE mechanics SET name = %(name)s, ' \
            'alternative = %(alternative)s, has_data = %(has_data)s, ' \
            'category_id = %(category_id)s, update_time = NOW() WHERE ' \
            'id = %(mechanic_id)s;'
        connectToMySQL(cls.db).query_db(query, data)
        Game.update_mechanic_data('', data['mechanic_id'])
        return 0