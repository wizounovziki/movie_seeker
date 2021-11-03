from types import resolve_bases
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
import warnings
warnings.filterwarnings("ignore")
#6483 is the only error
"""
movie_list_path = "Datasets/download/movie_titles.txt"
result_path = "crawlerresult.txt"

movie_list = []
true_movie_list = {}
with open(movie_list_path,"rb") as f:
    movie_list = f.readlines()
for movie in movie_list:
    try:
        movie_fixed = movie.decode('UTF-8').strip('\n')
        movie_fixed_list = movie_fixed.split(",")
        true_movie_list[int(movie_fixed_list[0])] = movie_fixed_list[2]
    except:
        movie_list.remove(movie)
print(len(true_movie_list))
print(true_movie_list[17768])
"""

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

for i in range(6445,17768):
    try:
        index = i
        movie_title = true_movie_list[i]
        true_name = movie_title.replace(" ","+")
        link = "https://www.imdb.com/find?q="+true_name
        detail_rep = requests.get(url=link,headers = header,verify = False)
        detail_text = detail_rep.content.decode(encoding="utf-8")
        detail_soup = BeautifulSoup(detail_text,features="html.parser")
        target_movie = detail_soup.find("div",id="wrapper").find("div",id="pagecontent").find("div",id="content-2-wide").find("div",id="main").find("div",class_="article").find("div",class_="findSection").find("table",class_="findList").find_all("tr")[0]
        target_movie_image_url = target_movie.find("td",class_="primary_photo").find("a").find("img")["src"]
        target_movie_url = target_movie.find("td",class_="primary_photo").find("a")["href"]
    except:
        print(i)
        with open("spid.txt","a") as f:
            f.write(str(i)+"\n")
        continue
    with open(result_path,"a") as f:
        f.write(str(index)+",,,"+movie_title+",,,"+target_movie_image_url[:-28]+target_movie_image_url[-16:]+",,,"+"https://www.imdb.com"+target_movie_url+"\n")
# name = "Dinosaur Planet"
# true_name = name.replace(" ","+")
# link = "https://www.imdb.com/find?q="+true_name
# detail_rep = requests.get(url=link,headers = header,verify = False)
# detail_text = detail_rep.content.decode(encoding="utf-8")
# detail_soup = BeautifulSoup(detail_text,features="html.parser")
# target_movie = detail_soup.find("div",id="wrapper").find("div",id="pagecontent").find("div",id="content-2-wide").find("div",id="main").find("div",class_="article").find("div",class_="findSection").find("table",class_="findList").find_all("tr")[0]
# target_movie_image_url = target_movie.find("td",class_="primary_photo").find("a").find("img")["src"]
# target_movie_url = target_movie.find("td",class_="primary_photo").find("a")["href"]
# print(target_movie_image_url[:-28]+target_movie_image_url[-16:])
# print("https://www.imdb.com"+target_movie_url)

# movie_detail_page = "https://www.imdb.com"+target_movie_url
# detail_rep_2 = requests.get(url=movie_detail_page,headers = header,verify = False)
# detail_text_2 = detail_rep_2.content.decode(encoding="utf-8")
# detail_soup_2 = BeautifulSoup(detail_text_2,features="html.parser")
# target_detail = detail_soup_2.find("div",id="__next").find("main",role="main").find("div",role="presentation").find("section").find("section").find("div",data-testid="genres")
# print(target_detail)
# detail_infor = target_detail.find("span",id="presentation").text
# # detail_type = target_detail.find()
# print(detail_infor)