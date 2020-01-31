from flask import Blueprint, render_template, request, redirect, url_for
from app2.models.Post import Post
from app2.config import db

posts = Blueprint('posts', __name__)


@posts.route('/new', methods=['GET'])
def new():
    return render_template('posts/new.html')


@posts.route('/', methods=['POST'])
def create():
    f = request.form
    post = Post(f['title'], f['body'])

    db.session.add(post)
    db.session.commit()
    return redirect(url_for('posts.new'))


@posts.route('/', methods=['GET'])
def list():
    posts = Post.query.order_by(Post.title)
    return render_template('posts/index.html', posts=posts)


@posts.route('/<int:id>', methods=['DELETE'])
def remove(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.list'))
