from flask import flash, redirect, request
from flask_app import app
from flask_app.models.mechanic import Mechanic

@app.route('/admin/dashboard/add_mechanic', methods = ['POST'])
def add_mechanic():
    if Mechanic.get_by_any_name(request.form['name']):
        flash('Mechanic already exists.')
        return redirect('/admin/dashboard')
    Mechanic.insert(request.form)
    return redirect('/admin/dashboard')

@app.route('/admin/dashboard/update_mechanic', methods = ['POST'])
def update_mechanic():
    if Mechanic.get_by_any_name(request.form['name']) and \
            Mechanic.get_by_any_name(request.form['name']).id is not \
            int(request.form['mechanic_id']):
        flash('Mechanic already exists.')
        return redirect('/admin/dashboard')
    Mechanic.update(request.form)
    return redirect('/admin/dashboard')