from app2.config import app, db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(90))
    body = db.Column('body', db.String(255))

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f'<Post: title -> {self.title} body -> {self.body}>'
