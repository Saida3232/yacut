from datetime import datetime

from flask import url_for

from . import db
from .constants import MODEL_FIELDS


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        for field in MODEL_FIELDS:
            if field in data:
                setattr(self, MODEL_FIELDS[field], data[field])

    def to_dict(link):
        return {
            'url': link.original,
            'short_link': url_for('redirect_custom_id',
                                  custom_id=link.short, _external=True)
        }