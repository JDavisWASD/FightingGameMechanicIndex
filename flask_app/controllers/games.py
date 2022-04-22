from flask import flash, redirect, request
from flask_app import app
from flask_app.models.game import Game

@app.route('/admin/dashboard/add_game', methods = ['POST'])
def add_game():
#TODO: Uncomment when done testing
#    if Game.get_by_name(request.form['name']):
#        flash('Game already exists.')
#        return redirect('/admin/dashboard')
    game_id = Game.save_game(request.form)
    form = request.form.to_dict()
    mechanics_list = []     #elements as ('mech_id', 'y/n/data')
    for i in range(2, len(form)):
        mechanics_list.append(form.popitem())
    Game.save_mechanics(game_id, mechanics_list)
    return redirect('/admin/dashboard')