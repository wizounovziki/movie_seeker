from configapp import db
import logging_loader
from datetime import datetime

logger = logging_loader.Logger(name="mysql_logger",logname='log/mysql.log').logger
class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.INTEGER,primary_key=True)
    #basic part:
    user_email = db.Column(db.String(255),nullable=False)
    user_password = db.Column(db.String(255),nullable=False)
    # user_reference_id = db.Column(db.INTEGER,primary_key=True)
    #information part
    user_name = db.Column(db.String(255))
    user_other_info = db.Column(db.String(2047))
    #security
    user_activate = db.Column(db.Boolean, default=False, nullable=False)
    user_last_token = db.Column(db.String(255),nullable=True)
    user_last_activate_time = db.Column(db.DateTime,nullable=True)
    user_top_secrect = db.Column(db.String(255),nullable=False)

class Movie(db.Model):
    __tablename__ = "movie"
    movie_id = db.Column(db.INTEGER,primary_key=True)
    movie_name = db.Column(db.String(255),nullable=False)
    movie_link = db.Column(db.String(255),nullable=True)
    movie_img_link = db.Column(db.String(255),nullable=True)
    movie_type = db.Column(db.String(255),nullable=True)
    movie_year = db.Column(db.INTEGER,nullable=True)
    movie_other_info = db.Column(db.String(255),nullable=True)
    movie_average_double_rating = db.Column(db.INTEGER,nullable=True)

class RatingRecord(db.Model):
    __tablename__="rating"
    rate_record_id = db.Column(db.INTEGER,primary_key=True)
    rate_score = db.Column(db.INTEGER)
    #attention: rate score is double, to be suitable to 4.5
    user_id = db.Column(db.INTEGER,db.ForeignKey("user.user_id"))
    user = db.relationship('User',backref=db.backref('rating_records'))
    movie_id = db.Column(db.INTEGER,db.ForeignKey("movie.movie_id"))
    movie = db.relationship('Movie',backref=db.backref('rating_records'))

def Update_database():
    db.session.commit()

if __name__ == "__main__":
    db.create_all()