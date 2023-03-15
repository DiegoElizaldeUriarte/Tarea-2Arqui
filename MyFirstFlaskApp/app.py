from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username[0].isupper() and password.isalnum():
            return redirect(url_for('login_success'))
    return render_template('login.html')


@app.route('/success')
def login_success():
    return 'Login successful!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
