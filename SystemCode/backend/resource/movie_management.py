from numpy.core import records
from sqliteModel import Movie,RatingRecord,User,Update_database,db
from flask_restful import abort, fields, reqparse, Resource
from itsdangerous.exc import BadSignature, SignatureExpired
from datetime import datetime
import json
# from flask import send_from_directory
from resource.general import general_serializer#pwd_context, reset_password_link, activate_user_link
# from werkzeug.datastructures import FileStorage
from process.svd_predict import *
import os
import random

def general_auth(token):
    #then auto auth part
    try:
        data = general_serializer.loads(token)
    except SignatureExpired:
        return False # valid token, but expired
    except BadSignature:
        return False
    user_email = data["useremail"]
    user = User.query.filter_by(user_email=user_email).first()
    if not user:
        return False
    if user.user_last_token != token:
        return False
    if user.user_activate != True:
        return False
    else:
        return user

def filter_no_url_movie(id_list):
    target_list = []
    for index in id_list:
        movie = Movie.query.filter_by(movie_id=index).first()
        if movie:
            if movie.movie_link and movie.movie_img_link:
                target_list.append(index)
    return target_list

profile_parser = reqparse.RequestParser()
profile_parser.add_argument(
    'token',
    dest='token',
    type=str,
    required=True,
    help='The token',
    location='headers',
)

class Get_Full(Resource):
    def get(self,current_page,page_size):
        target_id_start = (int(current_page)-1)*int(page_size)
        target_id_end = int(current_page)*int(page_size)
        ids = [id[0] for id in Movie.query.with_entities(Movie.movie_id).all()]
        ids = filter_no_url_movie(ids)
        total_number = len(ids)
        target_id_list = ids[target_id_start:target_id_end]
        target_data = []
        for index in target_id_list:
            target_movie = Movie.query.filter_by(movie_id=index).first()
            movie_data = {"id":index,"title":target_movie.movie_name}
            if target_movie.movie_year:
                movie_data["year"] = target_movie.movie_year
            else:
                movie_data["year"] = '2000'
            movie_data['img'] = target_movie.movie_img_link
            movie_data['genre'] = target_movie.movie_type
            movie_data['url'] = target_movie.movie_link
            movie_data['rate'] = (target_movie.movie_average_double_rating)/2
            # for record in target_movie.rating_records:
            #     if record.user == user:
            #         movie_data['user_rate'] = (record.rate_score)/2
            target_data.append(movie_data)
        return {"total":total_number,"data":target_data},200

class Get_recommend(Resource):
    def get(self,current_page,page_size):
        current_page = int(current_page)
        page_size = int(page_size)
        # args = profile_parser.parse_args()
        # token = args.token
        # user = general_auth(token)
        ids = [movie.movie_id for movie in Movie.query.order_by(Movie.movie_average_double_rating).all()]
        ids = filter_no_url_movie(ids)
        total_number = len(ids)
        ids = [ele for ele in reversed(ids)]
        target_id_start = (int(current_page)-1)*int(page_size)
        target_id_end = int(current_page)*int(page_size)
        target_id_list = ids[target_id_start:target_id_end]
        ##todo here add the recommend function
        target_data = []
        for index in target_id_list:
            target_movie = Movie.query.filter_by(movie_id=index).first()
            movie_data = {"id":index,"title":target_movie.movie_name}
            if target_movie.movie_year:
                movie_data["year"] = target_movie.movie_year
            else:
                movie_data["year"] = '2000'
            movie_data['img'] = target_movie.movie_img_link
            movie_data['genre'] = target_movie.movie_type
            movie_data['url'] = target_movie.movie_link
            movie_data['rate'] = (target_movie.movie_average_double_rating)/2
            target_data.append(movie_data)
        return {"total":total_number,"data":target_data},200

class Get_likes(Resource):
    def get(self,current_page,page_size):
        current_page = int(current_page)
        page_size = int(page_size)
        target_id_start = (int(current_page)-1)*int(page_size)
        target_id_end = int(current_page)*int(page_size)
        args = profile_parser.parse_args()
        token = args.token
        print(token)
        user = general_auth(token)
        if not user:
            return {"error":"login failed"},401
        movie_list = get_recommend_movie(user.user_id)
        movie_list = filter_no_url_movie(movie_list)
        total_number = len(movie_list)
        target_data = []
        for index in movie_list[target_id_start:target_id_end]:
            target_movie = Movie.query.filter_by(movie_id=index).first()
            movie_data = {"id":index,"title":target_movie.movie_name}
            if target_movie.movie_year:
                movie_data["year"] = target_movie.movie_year
            else:
                movie_data["year"] = '2000'
            movie_data['img'] = target_movie.movie_img_link
            movie_data['genre'] = target_movie.movie_type
            movie_data['url'] = target_movie.movie_link
            movie_data['rate'] = (target_movie.movie_average_double_rating)/2
            target_data.append(movie_data)
        return {"total":total_number,"data":target_data},200

class Get_rate_history(Resource):
    def get(self,current_page,page_size):
        current_page = int(current_page)
        page_size = int(page_size)
        target_id_start = (int(current_page)-1)*int(page_size)
        target_id_end = int(current_page)*int(page_size)
        args = profile_parser.parse_args()
        token = args.token
        user = general_auth(token)
        if not user:
            return {"error":"login failed"},401
        rate_records = user.rating_records
        target_data = []
        # print(rate_records)
        for record in rate_records:
            # print(record)
            target_movie = record.movie
            if not (target_movie.movie_link and target_movie.movie_img_link):
                continue
            movie_data = {"id":target_movie.movie_id,"title":target_movie.movie_name}
            if target_movie.movie_year:
                movie_data["year"] = target_movie.movie_year
            else:
                movie_data["year"] = '2000'
            movie_data['img'] = target_movie.movie_img_link
            movie_data['genre'] = target_movie.movie_type
            movie_data['url'] = target_movie.movie_link
            movie_data['rate'] = (target_movie.movie_average_double_rating)/2
            movie_data['user_rate'] = (record.rate_score)/2
            target_data.append(movie_data)
        total_number = len(target_data)
        return {"total":total_number,"data":target_data[target_id_start:target_id_end]},200


class Get_movie_detail(Resource):
    def get(self,movie_id):
        try:
            args = profile_parser.parse_args()
            token = args.token
            user = general_auth(token)
        except:
            user = None
        movie_id = int(movie_id)
        target_movie = Movie.query.filter_by(movie_id=movie_id).first()
        if not target_movie:
            return {"information":"not found"},404
        movie_data = {"id":movie_id,"title":target_movie.movie_name}
        if target_movie.movie_year:
            movie_data["year"] = target_movie.movie_year
        else:
            movie_data["year"] = '2000'
        movie_data['img'] = target_movie.movie_img_link
        movie_data['genre'] = target_movie.movie_type
        movie_data['url'] = target_movie.movie_link
        movie_data['rate'] = (target_movie.movie_average_double_rating)/2
        for record in target_movie.rating_records:
            if record.user == user:
                movie_data['user_rate'] = (record.rate_score)/2
        return movie_data

class Calculate_movie_mean(Resource):
    def get(self):
        movie_list = Movie.query.all()
        for movie in movie_list:
            records = movie.rating_records
            total_rate = 0
            total_num = 0
            for record in records:
                total_rate = total_rate+record.rate_score
                total_num += 1
            if total_num == 0:
                movie.movie_average_double_rating = 0
            else:
                movie.movie_average_double_rating = total_rate//total_num
            Update_database()
        return {"information":"finished"},200

sp_parser = reqparse.RequestParser()
sp_parser.add_argument(
    'token',
    dest='token',
    type=str,
    required=True,
    help='The token',
    location='headers',
)
sp_parser.add_argument(
    'rating',
    dest='rating',
    type=float,
    required=True,
    help='The rate',
)
sp_parser.add_argument(
    'movie_id',
    dest='movie_id',
    type=int,
    required=True,
    help='The movie id',
)
class Rating(Resource):
    def post(self):
        args = sp_parser.parse_args()
        token = args.token
        user = general_auth(token)
        if not user:
            return {"error":"login failed"},401
        movie_id = args.movie_id
        rating = args.rating
        movie = Movie.query.filter_by(movie_id=movie_id).first()
        if not movie:
            return {"error":"movie not found"},404
        finished = False
        for record in user.rating_records:
            if record.movie == movie:
                record.rate_score = int(rating*2)
                Update_database()
                finished = True
                # print(record.rate_score)
                break
        if not finished:
            new_record = RatingRecord()
            new_record.rate_score = int(rating*2)
            new_record.user_id = user.user_id
            new_record.movie_id = movie_id
            db.session.add(new_record)
            db.session.commit()
        movie_new = Movie.query.filter_by(movie_id=movie_id).first()
        records = movie_new.rating_records
        total_rate = 0
        total_num = 0
        for record in records:
            total_rate = total_rate+record.rate_score
            total_num += 1
        if total_num == 0:
            movie_new.movie_average_double_rating = 0
        else:
            # print(total_rate)
            movie_new.movie_average_double_rating = total_rate//total_num
        Update_database()
        return {"status":"success"},200