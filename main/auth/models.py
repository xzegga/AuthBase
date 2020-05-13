from ..core import db, guard


class Token(db.Model):
  __tablename__ = 'token'

  id = db.Column(db.Integer, primary_key=True)
  jti = db.Column(db.String(250))
  
  def __init__(self, jti): 
    self.jti = jti 


  @classmethod
  def blacklist_jti(cls, jti):
    token = cls(jti)
    db.session.add(token)    
    db.session.commit()
    return token
    
  @classmethod
  def get_blacklisted(cls):
    return [{'jti': token.jti} for token in  cls.query.all()]