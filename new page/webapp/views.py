from webapp import app
from flask import render_template


@app.route('/1')
def index():
    return render_template('layout.html')


@app.route('/2')
def index2():
    return render_template('layout2.html')


@app.route('/3')
def index3():
    return render_template('layout3.html')
