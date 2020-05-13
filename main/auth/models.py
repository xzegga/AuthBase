from ..core import db, guard
from ..helpers import JsonSerializer

class Token(db.Model):
  __tablename__ = 'bl_token'

  id = db.Column(db.Integer, primary_key=True)
  token = db.Column(db.String(250))

  @classmethod
  def blacklist_jti(cls, jti):
    _me = cls()
    _me.token = jti
    db.session.add(_me)    
    db.session.commit()
    return cls
    
  @classmethod
  def get_blacklisted(cls):
    return cls.query.all()
