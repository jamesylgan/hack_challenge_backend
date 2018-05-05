from . import *

class User(Base):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(255), nullable = False)
  last_name = db.Column(db.String(255), nullable = False)

  """Adding more column info to traveler planner"""
  email = db.Column(db.String(128), nullable =False, unique =True)
  tripinfo = db.relationship('UserTripInfo', backref = 'users')


  def __init__(self, **kwargs):
      self.first_name = kwargs.get('first_name')
      self.last_name = kwargs.get('last_name')
      self.email = kwargs.get('email')
      tripinfo = []


  def __repr__(self):
      return str(self.__dict__)


class UserTripInfo(Base):
    __tablename__ = 'tripinfos'
    id            = db.Column(db.Integer, primary_key = True)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'),
                    nullable = False)
    starting      = db.Column(db.String(255), nullable = False)
    destination   = db.Column(db.String(255), nullable = False)
    start_date    = db.Column(db.String(255), nullable = False)
    end_date      = db.Column(db.String(255), nullable = False)
    cost          = db.Column(db.Integer)
    num_of_days   = db.Column(db.Integer)


    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.starting = kwargs.get('starting')
        self.destination = kwargs.get('destination')
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')
        self.cost = kwargs.get('cost')
        self.num_of_days = kwargs.get('num_of_days')



class UserSchema(ModelSchema):
  class Meta:
    model = User

class UserTripSchema(ModelSchema):
    class Meta:
        model = UserTripInfo
