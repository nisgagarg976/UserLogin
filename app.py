from flask import Flask, render_template, request, redirect, url_for, session
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user








login_manager = LoginManager()
login_manager.login_view = 'home'
login_manager.init_app(app)





app.config['UPLOADED_PHOTOS_DEST'] = 'uploads/profile_images'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        phone_no = request.form['phone_no']
        password = request.form['password']
        
        password_hash = generate_password_hash(password)
        
        new_user = User(name=name, username=username, email=email, phone_no=phone_no, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = current_user
    if request.method == 'POST':
       
        user.current_year = request.form['current_year']
        user.current_semester = request.form['current_semester']
        user.branch = request.form['branch']
        user.father_name = request.form['father_name']
        user.address = request.form['address']
        
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('edit_profile.html', user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
