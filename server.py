from flask_app import app
from flask_app.controllers import admins, categories, home, games, mechanics

if __name__ == '__main__':
    app.run(debug = True)