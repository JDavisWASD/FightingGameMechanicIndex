import os

#from flask import flash
from flask_app.config.MySQLConnection import connectToMySQL

class Game:
    db = os.environ.get('DATABASE')

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.abreviation = data['abreviation']
        self.box_art = data['box_art']
        self.create_time = data['create_time']
        self.update_time = data['update_time']

# Get Methods ------------------------------------------------------------------
    @classmethod
    def get_by_name(cls, name):
        data = {'name': name}
        query = 'SELECT * FROM games WHERE name = %(name)s;'
        result = connectToMySQL(cls.db).query_db(query)
        if result:
            return cls(result[0])
        return False

# Set Methods ------------------------------------------------------------------
    @classmethod
    def save_game(cls, data):
        query = 'INSERT INTO games (name, abreviation, create_time, ' \
            'update_time) VALUES (%(name)s, %(abreviation)s, ' \
            'NOW(), NOW());'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def save_mechanics(cls, game_id, mechanics_list):
        data = {'game_id': game_id}
        for mech in mechanics_list:
            data['mechanic_id'] = mech[0]

# If 1 is not 'yes' it is either the data field or the mechanic isn't in this 
# game so we don't care what the value is. Else ensures that a mechanic without
# a data component ends up with nothing in the data field.
            if not mech[1] == 'yes':
                data['data'] = mech[1]
            else:
                data['data'] = ''
            print(data)
            if not data['data'] == 'no':
                query = 'INSERT INTO mechanics_of_games (game_id, ' \
                    'mechanic_id, data, create_time, update_time) VALUES ' \
                    '(%(game_id)s, %(mechanic_id)s, %(data)s, NOW(), NOW());'
                connectToMySQL(cls.db).query_db(query, data)
        return 0

    @classmethod
    def update_mechanic_data(cls, data_field, mechanic_id):
        data = {
            'data_field': data_field,
            'mechanic_id': mechanic_id
            }
        print(data)
        query = 'UPDATE mechanics_of_games SET data = %(data_field)s, ' \
            'update_time = NOW() WHERE mechanic_id = %(mechanic_id)s;'
        connectToMySQL(cls.db).query_db(query, data)
        return 0