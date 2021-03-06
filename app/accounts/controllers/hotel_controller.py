from . import *
from flask import jsonify

user_schema = UserSchema()
user_trip_schema = UserTripSchema()

# """Handles POST and DELETE for users who signed up on app"""
# @accounts.route('/hotels', methods = ['POST', 'DELETE'])
# def users_crud():
#     if request.method == 'POST':
#         f_name = request.args.get('first_name')
#         l_name = request.args.get('last_name')
#         email = request.args.get('email')
#         user = dao.create_user(f_name, l_name, email)
#         return json.dumps({'data': {'user': user_schema.dump(user).data},
#             'success': True})
#     elif request.method == 'DELETE':
#         user_id = request.args.get('id')
#         user = dao.delete_user(user_id)
#         return jsonify({'success': True})


"""Handles GET requests for app users """
@accounts.route('/hotels')
@accounts.route('/hotels/<city>', methods=['GET'])
def get_hotels(city):
    if city is not None:
        hotels = hotel_dao.get_nearby(city, 'lodging')
        return jsonify({'data': hotels, 'success': True})
    else:
        return jsonify({'success' : False})



# """Handles HTTP Requests for User Info"""
# @accounts.route('/users_info', methods = ['GET', 'POST', 'DELETE'])
# def user_info_crud():
#     if request.method == 'POST':
#         user_id = request.args.get('user_id')
#         if user_id:
#             starting = request.arg.get('starting')
#             destination = request.args.get('destination')
#             start_date = request.args.get('start_date')
#             end_date = request.args.get('end_date')
#             cost = request.args.get('cost')
#             num_of_days = request.args.get('num_of_days')
#             user_info = UserTripInfo(starting = starting, destination = destination,
#                 start_date = start_date, end_date = end_date, cost = cost,
#                 num_of_days = num_of_days)
#             return json.dumps({'data': {'user_info': user_trip_schema.dump(user_info)},
#                 'success': True})
#     elif request.method == 'GET':
#         user_trip_id = request.args.get('id')
#         user_info = dao.get_trip_by_id(user_trip_id)
#         return json.dumps({'data': {'user_info': user_info}, 'success': True})
#     else
#         user_trip_id = request.args.get('id')
#         user_info = dao.delete_user_trip(user_trip_id)
#         return json.dumps({'success': True})
