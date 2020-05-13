from ..core import db, guard
from ..helpers import JsonSerializer


class TokenJsonSerializer(JsonSerializer):
  __json_public__ = ['id', 'jti']


class Token(TokenJsonSerializer, db.Model):
  __tablename__ = 'token'

  id = db.Column(db.Integer, primary_key=True)
  jti = db.Column(db.String(250))
  
  def __init__(self, jti): 
    self.jti = jti 

  def __repr__(self):
    return "<Token '{}'>".format(self.jti)


  @classmethod
  def blacklist_jti(cls, jti):
    token = cls(jti)
    db.session.add(token)    
    db.session.commit()
    return token
    
  @classmethod
  def get_blacklisted(cls):
    return [token.to_json() for token in  cls.query.all()]