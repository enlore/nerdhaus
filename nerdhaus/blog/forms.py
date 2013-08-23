# -*- coding: utf-8 -*-

from flask.ext.wtf import (Form, TextField, TextAreaField, SubmitField,
        Required, Email)
from flask.ext.wtf.html5 import EmailField

class PostForm(Form):
    title           = TextField(u'Post Title', [Required()])
    content         = TextAreaField(u'Content', [Required()])
    author_email    = TextField(u'Author\'s Email', [Required(), Email()])
    submit          = SubmitField(u'Submit')
