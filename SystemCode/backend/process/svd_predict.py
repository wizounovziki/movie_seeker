import os
import numpy as np
from scipy import io
from itertools import groupby
from operator import itemgetter
import pickle
from math import sqrt
#attention: the user_id and movie_id in reference start from 0, which means need +1 to be into database
mat_path = "ckpoint/mat/newD.mat"
refer_path = "ckpoint/mat/referD.mat"
svd_path = "ckpoint/svd/"
reference_user_path = "ckpoint/reference/u.npy"
reference_movie_path = "ckpoint/reference/i.npy"
bu=np.load(svd_path+"bu.npy")
bi=np.load(svd_path+"bi.npy")
qi=np.load(svd_path+"qi.npy")
pu=np.load(svd_path+"pu.npy")
yj=np.load(svd_path+"yj.npy")
reference_user = np.load(reference_user_path)
reference_movie = np.load(reference_movie_path)
mat = io.loadmat(refer_path)['X']

def pre_processing(mat):
    bu_index_file = svd_path+"bu_index.data"
    bi_index_file = svd_path+"bi_index.data"

    if not (os.path.isfile(bu_index_file) and os.path.isfile(bi_index_file)):

        print("Pre-processing...")
        mat_nonzero = mat.nonzero()
        print("   make bi indexes...")
        bi_index = []
        for k, g in groupby(zip(mat_nonzero[0], mat_nonzero[1]), itemgetter(0)):
          to_add = list(map(lambda x:int(x[1]), list(g)))
          bi_index.append(to_add)

        print("   make bu indexes...")
        bu_index = []
        indexes = np.argsort(mat_nonzero[1])
        for k, g in groupby(zip(mat_nonzero[1][indexes], mat_nonzero[0][indexes]), itemgetter(0)):
          to_add = list(map(lambda x:int(x[1]), list(g)))
          bu_index.append(to_add)    

        with open(bi_index_file, "wb") as fp:
            pickle.dump(bi_index, fp)
        with open(bu_index_file, "wb") as fp:
            pickle.dump(bu_index, fp)
    else:
        with open(bi_index_file, "rb") as fp:
            bi_index = pickle.load(fp)
        with open(bu_index_file, "rb") as fp:
            bu_index = pickle.load(fp)

    print("Pre-processing done.")
    return bu_index, bi_index

def predict_r_ui(mat, u, i, mu, bu, bi, qi, pu, N_u, yj):
    N_u_sum = yj[N_u].sum(0)
    return mu + bu[u] + bi[0, i] + np.dot(qi[i], (pu[u] + N_u_sum / sqrt(len(N_u))))

def get_reference_movie_list(target):
    movie_list = []
    for i in target:
        original_index = np.where(reference_movie==i[1])
        movie_list.append(original_index[0][0].item()+1)
    return movie_list

def get_recommend_movie(userid):
    index_userid = userid-1
    u_id = reference_user[index_userid]
    if u_id == -1:
        return []
    bu_index, bi_index = pre_processing(mat)
    mu = mat.data[:].mean()
    N_u = bi_index[u_id]
    cx = mat.tocoo()
    target = []
    for i in list(set(cx.col)):
        r_ui_pred = predict_r_ui(mat, u_id, i, mu, bu, bi, qi, pu, N_u, yj)
        target.append((u_id,i,r_ui_pred[0]))
    def takeThird(elem):
        return elem[2]
    target.sort(key=takeThird,reverse=True)
    final_list = get_reference_movie_list(target[0:50])
    print(final_list)
    return final_list

    
