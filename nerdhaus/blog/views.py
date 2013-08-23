# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, request, flash
from flask.ext.login import login_required, current_user

from ..extensions import db
from models import Post, Author
from forms import PostForm


def admin_required():
    pass

blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route('/')
def index():
    posts = ['sweet jesus'] 
    return render_template('blog/index.html', posts=posts)

@blog.route('/post/<int:post_id>')
def post(post_id):
    return 'view one post'

@blog.route('/archive')
def archive():
    return 'view archive'

@blog.route('/admin')
@login_required
def admin():
    return 'access admin backend'

@blog.route('/admin/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    return 'edit that post'

@blog.route('/admin/post/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    return 'delete that post'

@blog.route('/admin/post/new', methods=['GET', 'POST'])
def new():
    form = PostForm()
    if form.validate_on_submit():
       post = Post() 
       post.author = Author()
       post.content = form.content.data
       post.title = form.title.data
       post.author.email = form.author_email.data
       db.session.add(post)
       db.session.commit()
       return redirect(url_for('blog.index'))

    return render_template('blog/new.html', form=form)
