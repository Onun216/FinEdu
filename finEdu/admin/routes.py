from finEdu import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin/admin.html')
