# -*- coding: utf-8 -*-

from sqlalchemy import Column
from ..extensions import db
from ..utils import STRING_LEN
from ..user import User

class Post(db.Model):
    id          = Column(db.Integer, primary_key=True)
    title       = Column(db.String(STRING_LEN))
    content     = Column(db.String(STRING_LEN))
    published   = Column(db.Date)
    author_id   = Column(db.Integer, db.ForeignKey('user.id'))
