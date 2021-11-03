from sqlalchemy.orm import query
from sqliteModel import Movie,RatingRecord,User,Update_database,db
from scipy import io
import numpy as np
from resource.general import pwd_context
import random
#step1 read user data
mat_path = "ckpoint/mat/newD.mat"
reference_user_path = "ckpoint/reference/u.npy"
reference_movie_path = "ckpoint/reference/i.npy"
reference_user = np.load(reference_user_path)
reference_movie = np.load(reference_movie_path)
"""
#add user
target_user = []
print(reference_user[3068])
print(reference_movie[29])
for i,refer in enumerate(reference_user):
    if refer != -1:
        target_user.append(i+1)
print(target_user)
for user_id in target_user:
    user_email = "user"+str(user_id)+"@test.com"
    user_password = "user"+str(user_id)
    user = User.query.filter_by(user_email=user_email).first()
    if user:
        print("something bad happened")
        print(user_id)
        break
    new_user = User()
    new_user.user_id = user_id
    new_user.user_email = user_email
    new_user.user_password=pwd_context.hash(user_password)
    new_user.user_name = "user"+str(user_id)
    new_user.user_activate = True
    new_user.user_top_secrect = "111"
    db.session.add(new_user)
    db.session.commit()
    print("finished "+str(user_id))
"""
"""
#add movie
target_movie = []
for i,refer in enumerate(reference_movie):
    if refer != -1:
        target_movie.append(i+1)
# print(len(target_movie))
movie_infor = {}
movie_id_path = "movie_titles.txt"
movie_infor_path = "crawlerresult.txt"
movie_list = []
movie_infor_list = []
with open(movie_id_path,"rb") as f:
    movie_list = f.readlines()
with open(movie_infor_path,"rb") as f:
    movie_infor_list = f.readlines()
for movie in movie_list:
    try:
        movie_fixed = movie.decode('UTF-8').strip('\n')
        movie_fixed_list = movie_fixed.split(",")
        if int(movie_fixed_list[0]) in target_movie:
            movie_infor[int(movie_fixed_list[0])] = {"name":movie_fixed_list[2],"year":int(movie_fixed_list[1]),"url":"","img_url":""}
    except:
        movie_list.remove(movie)

for movie in movie_infor_list:
    try:
        movie_fixed = movie.decode('UTF-8').strip('\n')
        movie_fixed_list = movie_fixed.split(",,,")
        if int(movie_fixed_list[0]) in target_movie:
            if movie_infor[int(movie_fixed_list[0])]["name"] != movie_fixed_list[1]:
                print("error happened")
                print(movie_fixed)
            movie_infor[int(movie_fixed_list[0])]["url"] = movie_fixed_list[3]
            movie_infor[int(movie_fixed_list[0])]["img_url"] = movie_fixed_list[2]
    except:
        movie_infor_list.remove(movie)
type_list = ["Action","Adventure","Fantasy","Science Fiction","Crime","Animation","Family","Drama","Romance","Thriller","Comedy","War","Horror","Music","Western"]

for movie_id in target_movie:
    movie = Movie.query.filter_by(movie_id=movie_id).first()
    if movie:
        print("something bad happened")
        print(movie_id)
        continue
    new_movie = Movie()
    new_movie.movie_id = movie_id
    new_movie.movie_name = movie_infor[movie_id]["name"]
    new_movie.movie_link = movie_infor[movie_id]["url"]
    new_movie.movie_img_link = movie_infor[movie_id]["img_url"]
    type_num = random.randint(2,5)
    new_movie.movie_type = ",".join(random.sample(type_list, type_num))
    new_movie.movie_year = movie_infor[movie_id]["year"]
    db.session.add(new_movie)
    db.session.commit()
    print("finished "+str(movie_id))
"""
# movie_list = Movie.query.all()
# for movie in movie_list:
#     if not movie.movie_link:
#         print(movie.movie_id)
# print(reference_movie[4430])
# mat = io.loadmat(mat_path)['X']
# cx = mat.tocoo()
# for u,i,v in zip(cx.row, cx.col, cx.data):
#     print(u,i,v)
#     u = u.item()
#     i = i.item()
#     v = v.item()
#     user_id = u+1
#     movie_id = i+1
#     new_record = RatingRecord()
#     new_record.rate_score = 2*int(v)
#     new_record.user_id = user_id
#     new_record.movie_id = movie_id
#     db.session.add(new_record)
#     db.session.commit()
#     print("finished "+str(user_id)+ " "+str(movie_id) )

# movie_list = Movie.query.all()
# for movie in movie_list:
#     records = movie.rating_records
#     total_rate = 0
#     total_num = 0
#     for record in records:
#         total_rate = total_rate+record.rate_score
#         print(total_rate)
#         total_num += 1
#     if total_num == 0:
#         movie.movie_average_double_rating = 0
#     else:
#         movie.movie_average_double_rating = total_rate//total_num
#     print(movie.movie_average_double_rating)
#     print(movie.movie_id)
#     Update_database()
# movies = Movie.query.all()

# target_movie = []
# for i,refer in enumerate(reference_movie):
#     if refer != -1:
#         target_movie.append(i+1)
# movie_list = []
# for movie in movies:
#     movie_list.append(movie.movie_id)

# print(len(target_movie))
# print(len(movie_list))
# print(movie_list == target_movie)

# movie  = Movie.query.filter_by(movie_id=3323).first()
# print(movie)
# rate_record = RatingRecord.query.filter_by(rate_record_id=31075).first()
# print(rate_record.rate_score)
user_id = 3321#3323
user = User.query.filter_by(user_id=user_id).first()
for record in user.rating_records:
    db.session.delete(record)
    db.session.commit()