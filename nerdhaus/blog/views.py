# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, request, flash
from flask.ext.login import login_required, current_user

from ..extensions import db


def admin_required():
    pass

blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route('/')
def index():
    return 'blog index'

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
@login_required
def new():
    return 'create new post'
