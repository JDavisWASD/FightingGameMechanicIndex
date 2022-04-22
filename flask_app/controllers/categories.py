from flask import flash, redirect, request
from flask_app import app
from flask_app.models.category import Category

@app.route('/admin/dashboard/add_category', methods = ['POST'])
def add_category():
    if Category.get_by_name(request.form['name']):
        flash('Category already exists.')
        return redirect('/admin/dashboard')
    Category.insert(request.form)
    return redirect('/admin/dashboard')

@app.route('/admin/dashboard/update_mechanic', methods = ['POST'])
def update_category():
    if Category.get_by_name(request.form['name']) and \
            Category.get_by_name(request.form['name']).id is not \
            int(request.form['category_id']):
        flash('Category already exists.')
        return redirect('/admin/dashboard')
    Category.update(request.form)
    return redirect('/admin/dashboard')