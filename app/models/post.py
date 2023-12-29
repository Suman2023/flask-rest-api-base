from marshmallow import Schema, fields

from app import db


class Post(db.Model):
    """
    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.String(500), nullable=False)

    is_sensitive = db.Column(db.Boolean, default=False)
    """

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    is_sensitive = db.Column(db.Boolean, default=False)


class PostSchema(Schema):
    id = fields.Int(required=False)
    text = fields.Str(required=True)
    is_sensitive = fields.Bool(required=False)
