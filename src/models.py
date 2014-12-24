from .piny import db


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(40))
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Url(db.model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    url = db.Column(db.String(200))
    customized = db.Column(db.Boolean)
    url_customized = db.Column(db.String(30))

    def __init__(self, url, customized=False, url_custom=None):
        self.url = url
        self.customized = customized
        self.url_customized = url_custom

    def __repr__(self):
        return '<Url %r>' % self.url
