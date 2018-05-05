from . import *

user_schema = UserSchema()
user_trip_schema = UserTripSchema()


"""Creates new app user after all information written"""
def create_user(first_name, last_name, email):
        new_user = User(first_name = first_name, last_name = last_name,
                        email = email)
        return utils.commit_model(new_user)

"""Deletes user from app if so wishes"""
def delete_user(user_id):
    optional_user = Board.query.get(user_id)
    if not optional_user:
        raise Exception('Does not exist')
    return utils.delete_mode(optional_user)

"""Gets all users currently utilizing app"""
def get_all_users():
    return User.\
    query.\
    order_by(User.created_at.desc())

"""Get user by id"""
def user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


"""Creates user trip info"""
def create_trip_info(**kwargs):
    user_id = kwargs.get('user_id')
    starting = kwargs.get('starting')
    destination = kwargs.get('destination')
    start_date = kwargs.get('start_date')
    end_date = kwargs.get('end_date')
    cost = kwargs.get('cost')
    num_of_days = kwargs.get('num_of_days')
    user_trip_info = UserTripInfo(user_id = user_id, starting = starting,
        destination = destination, start_date = start_date, end_date = end_date,
        cost = cost, num_of_days = num_of_days)
    return utils.commit_model(user_trip_info)


"""Gets user trip info"""
def get_trip_by_id(user_id):
    return UserTripInfo.query.filter_by(user_id = user_id).first()


"""Deletes user's itinerary trip info"""
def delete_user_trip(user_trip_id):
    if user_trip_id is not None:
        opt_user_trip = UserTripInfo.query.get(user_trip_id)
        if not opt_user_trip:
            raise Exception('Does Not Exist')
        return utils.delete_model(opt_user_trip)
