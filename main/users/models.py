# -*- coding: utf-8 -*-
"""
    main.users.models
    ~~~~~~~~~~~~~~~~~~~~~
    User models
"""
import datetime
from ..core import db, guard
from ..helpers import JsonSerializer


class UserJsonSerializer(JsonSerializer):
  #'phone_number', 'address_1', 'address_2', 'address_3', 'country', 'state', 'zipcode'
  __json_public__ = ['id', 'username', 'first_name', 'last_name', 'roles']


class User(UserJsonSerializer, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True, unique=True)
  password = db.Column(db.String(256), nullable=False)  
  email = db.Column(db.String(120))
  first_name = db.Column(db.String(120), nullable=False)    
  last_name = db.Column(db.String(120), nullable=False)   
  phone_number = db.Column(db.String(20)) 
  skype = db.Column(db.String(35)) 
  address_1 = db.Column(db.String(120))  
  address_2 = db.Column(db.String(120))  
  address_3 = db.Column(db.String(120))  
  city = db.Column(db.String(120))  
  country = db.Column(db.String(120))  
  state = db.Column(db.String(120))  
  zipcode = db.Column(db.String(5))  
  is_active = db.Column(db.Boolean, default=True, server_default='true')
  last_login_at = db.Column(db.DateTime())
  registered_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
  roles = db.Column(db.Text, nullable=False)


  @property
  def rolenames(self):
      try:
          return self.roles.split(',')
      except Exception:
          return []

  @classmethod
  def lookup(cls, username):
    return cls.query.filter(((cls.username == username) | (cls.email == username))).one_or_none()

    #return cls.query.filter_by(username=username).one_or_none()

  @classmethod
  def identify(cls, id):
      return cls.query.get(id)

  @property
  def identity(self):
      return self.id


  def is_valid(self):
    return self.is_active

