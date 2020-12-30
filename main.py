#pip is a package manager for python
#to install a package, we'll use the command 'pip3 install ${packageName}'
#we installed both flask-sqlalchemy and flask as packages here

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)