
from voteapp import app
from flask import redirect, url_for


@app.route('/')
def index():
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0')
