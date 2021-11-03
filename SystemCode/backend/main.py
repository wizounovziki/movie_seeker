from configapp import app
from flask_restful import Api
import flask_restful as restful
from resource.login_management import Sign_in,Logout
# from resource.audio_management import Audio_Link,Mixed_upload,Filter_generator,Text_result
# from resource.embedder_management import Embedder_upload,Embedder_list,Embedder_Link
from resource.movie_management import Get_Full,Get_recommend,Get_likes,Get_rate_history,Get_movie_detail,Calculate_movie_mean,Rating

api = restful.Api(app)

# api.add_resource(Sign_up,'/user/sign_up')
api.add_resource(Sign_in,'/user/sign_in')
api.add_resource(Logout,'/user/logout')

api.add_resource(Get_Full,'/full_list/<current_page>/<page_size>')
api.add_resource(Get_recommend,'/recommend/<current_page>/<page_size>')
api.add_resource(Get_likes,'/also_like/<current_page>/<page_size>')
api.add_resource(Get_rate_history,'/rated/<current_page>/<page_size>')
api.add_resource(Get_movie_detail,'/movie_detail/<movie_id>')
api.add_resource(Rating,'/rating')

api.add_resource(Calculate_movie_mean,"/movie/management/itisdangerous")
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4397)