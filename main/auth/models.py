from ..core import db, guard
from ..helpers import JsonSerializer


class UserJsonSerializer(JsonSerializer):

  __json_public__ = ['id', 'token']


class Token(UserJsonSerializer, db.Model):
  __tablename__ = 'bl_token'

  id = db.Column(db.Integer, primary_key=True)
  token = db.Column(db.String(250))

  @classmethod
  def blacklist_jti(jti):
    # token = guard.extract_jwt_token(jti)["jti"]
    # guard.create(token)
    pass
    
  @classmethod
  def get_blacklisted(jti):
    # token = guard.extract_jwt_token(jti)["jti"]   
    # all_token = guard.all(token)
    pass
