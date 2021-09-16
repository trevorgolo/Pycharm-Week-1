from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(NameForm=None):
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return '<hi>Hello %s!<hi>' % name

if __name__ == '__main__':
    app.run(debug=True)