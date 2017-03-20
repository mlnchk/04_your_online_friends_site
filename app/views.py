from flask import render_template, flash
from app import app
from .forms import LoginForm
from friends_online import get_all


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s"' % form.openid.data)
        a = get_all(form.openid.data)
        return render_template('login.html', title='fuck', form=form, a=a)
    return render_template('login.html',
                           title='Sign In',
                           form=form)
