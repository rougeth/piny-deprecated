from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.shortener import Base62


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/piny.db'
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/<url_id>')
def redirect(url_id):
    url = Base62()
    return url.to_decinal(url_id)


if __name__ == '__main__':
    app.run()
