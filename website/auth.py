from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return 'Logout'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 charaters.', category='error')
        elif len(first_name) < 2:
            flash('Firt name must be greater than 1 charater.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be al least 7 charaters.', category='error')
        else:
            flash('Account created successfully!', category='success')

    return render_template('sign_up.html')
