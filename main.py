#pip is a package manager for python
#to install a package, we'll use the command 'pip3 install ${packageName}'
#we installed both flask-sqlalchemy and flask as packages here

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)