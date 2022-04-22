import os
import re

from flask import flash
from flask_app.config.MySQLConnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Admin:
    db = os.environ.get('DATABASE')

    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.email = data['email']
        self.create_time = data['create_time']
        self.update_time = data['update_time']

#Get Methods -------------------------------------------------------------------
    @classmethod
    def get_by_username(cls, username):
        data = {'username': username}
        query = 'SELECT * FROM admins WHERE username = %(username)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return False

#Set Methods -------------------------------------------------------------------
#    @classmethod
#    def insert(cls, data):
#        query = 'INSERT INTO admins (username, email, password, create_time, ' \
#            'update_time) VALUES (%(username)s, %(email)s, %(password)s, ' \
#            'NOW(), NOW());'
#        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE admins SET email = %(email)s, password =%(password)s, '\
            'update_time = NOW(), WHERE id = %(user_id)s;'
        connectToMySQL(cls.db).query_db(query, data)

#Helper Methods ----------------------------------------------------------------
    @staticmethod
    def validate_email(form):
        is_valid = True
        if form['email'] == '':
            flash('An email is required.')
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash('Invalid email address.')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_password(form):
        is_valid = True
        if form['password'] == '':
            flash('A password is required')
            is_valid = False
        if form['confirm_password'] == '':
            flash('Please confirm your password.')
            is_valid = False
        if form['password'] != form['confirm_password']:
            flash('Passwords don\'t match.')
            is_valid = False
        return is_valid

#    @staticmethod
#    def validate_new_admin(form):
#        is_valid = True
#        if form['username'] == '':
#            flash('A username is required.')
#            is_valid = False
#        if Admin.get_by_username(form['username']):
#            flash('An account with that username already exists.')
#            is_valid = False
#        is_valid = validate_email(form)
#        is_valid = validate_password(form)
#        return is_valid