from flask import flash, redirect, request, render_template, session
from flask_app import app
from flask_app.models.admin import Admin
from flask_app.models.category import Category
from flask_app.models.mechanic import Mechanic
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/admin')
def admin():
    if 'user_id' in session:
        session.pop('user_id')
    return render_template('admin.html')

@app.route('/admin/log_in', methods = ['POST'])
def log_in():
    user = Admin.get_by_username(request.form['username'])
    if user and \
            bcrypt.check_password_hash(user.password, request.form['password']):
        session['user_id'] = user.id
        return redirect('/admin/dashboard')

    flash('Incorrect username or password.')
    return redirect('/admin')

@app.route('/admin/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    categories = Category.get_all()
    mechanics = Mechanic.get_all()
    return render_template('dashboard.html', categories = categories, \
        mechanics = mechanics)

#@app.route('/admin/register', methods = ['POST'])
#def register():
#    if not Admin.validate_new_admin(request.form):
#        return redirect('/admin')
#
#    data = {
#        'username': request.form['username'],
#        'password': bcrypt.generate_password_hash(request.form['password']),
#        'email': request.form['email']
#    }
#    session['user_id'] = Admin.insert(data)
#    return redirect('/admin/dashboard')