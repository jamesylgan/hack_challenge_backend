from . import *

"""NOT ACTUAL HOTEL CLASS USED FROM FLASKPLATE"""

class Hotel(Base):
  __tablename__ = 'sessions'

  id      = db.Column(db.Integer, primary_key=True, unique =True, index =True)
  address = db.Column(db.String(40))
  rating  = db.Column(db.Integer)
  name    = db.column(db.String(40))
  city    = db.Column(db.String(40), nullable=False)

  def __init__(self, **kwargs):
    self.address  = kwargs.get('address', None)
    self.rating   = kwargs.get('rating', None)
    self.name     = kwargs.get('name', None)
    self.city     = kwargs.get('city', None)
    

  def __repr__(self):
    return str(self.__dict__)

  def _urlsafe_base_64(self):
    return hashlib.sha1(os.urandom(64)).hexdigest()


class HotelSchema(ModelSchema):
  class Meta:
    model = Hotel
