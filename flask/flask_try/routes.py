

from flask import render_template, url_for, flash, redirect
from flask_try.forms import RegistrationForm, LoginForm
from flask_try import app

tests = [
	{'experiment':'Kolsky',
	'strain_rate':1000,
	'material':'magnesium'
	},
	{'experiment':'Plate impact',
	'strain_rate':100000,
	'material':'magnesium'
	},
	{'experiment':'MTS',
	'strain_rate':0.001,
	'material':'magnesium'
	}
	]


@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html',tests = tests)


@app.route("/about")
def about():
    return render_template('about.html',title = 'About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
