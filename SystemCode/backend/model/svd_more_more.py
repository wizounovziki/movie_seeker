from utils import pre_processing, compute_sparse_correlation_matrix, path

import numpy as np
from scipy import io, sparse
from math import sqrt, isnan

from datetime import datetime

#################################################
# Non-vectorized way
#################################################
def predict_r_ui(mat, u, i, mu, bu, bi, qi, pu, N_u, yj):
    N_u_sum = yj[N_u].sum(0)
    return mu + bu[u] + bi[0, i] + np.dot(qi[i], (pu[u] + N_u_sum / sqrt(len(N_u))))

def compute_e_ui(mat, u, i, mu, bu, bi, qi, pu, N_u, yj):
    return mat[u, i] - predict_r_ui(mat, u, i, mu, bu, bi, qi, pu, N_u, yj)

def compute_loss(mat, mu, bu, bi, qi, pu, N_u, yj, l_reg6=0.005, l_reg7=0.015):
    loss = 0
    loss_reg = 0
    cx = mat.tocoo()
    for u,i,v in zip(cx.row, cx.col, cx.data):
        r_ui_pred = predict_r_ui(mat, u, i, mu, bu, bi, qi, pu, N_u, yj)
        loss += (mat[u, i] - r_ui_pred) ** 2 
        loss_reg += l_reg6 * ((bu ** 2).sum() + (bi ** 2).sum())
        loss_reg += l_reg7 * ((qi[i]**2).sum() + (pu[u]**2).sum() + (yj[N_u]**2).sum())

    return loss, loss+loss_reg

def svd_more_more(mat, mat_file, gamma1=0.007, gamma2=0.007, gamma3=0.001, l_reg2=100, l_reg6=0.005, l_reg7=0.015, f=50,u_id=15):
    # subsample the matrix to make computation faster
    mat = mat[0:mat.shape[0]//640, 0:mat.shape[1]//4]
    mat = mat[mat.getnnz(1)>0][:, mat.getnnz(0)>0]

    print(mat.shape)
    no_users = mat.shape[0]
    no_movies = mat.shape[1]

    bu_index, bi_index = pre_processing(mat, mat_file)
    
    # Init parameters
    bu = np.random.rand(no_users, 1)  * 2 - 1
    bi = np.random.rand(1, no_movies) * 2 - 1
    qi = np.random.rand(no_movies, f) * 2 - 1
    pu = np.random.rand(no_users, f) * 2 - 1
    yj = np.random.rand(no_movies, f) * 2 - 1

    mu = mat.data[:].mean()

    # Train
    print("Train...")
    n_iter = 30
    cx = mat.tocoo()
    for it in range(n_iter):
        print(it)
        print(datetime.now())
        for u,i,v in zip(cx.row, cx.col, cx.data):
            N_u = bi_index[u]
            e_ui = compute_e_ui(mat, u, i, mu, bu, bi, qi, pu, N_u, yj)

            bu[u] += gamma1 * (e_ui - l_reg6 * bu[u])
            bi[0, i] += gamma1 * (e_ui - l_reg6 * bi[0, i])
            qi[i] += gamma2 * (e_ui * (pu[u] + 1 / sqrt(len(N_u)) * yj[N_u].sum(0)) - l_reg7 * qi[i])
            pu[u] += gamma2 * (e_ui * qi[i] - l_reg7 * pu[u])
            yj[N_u] += gamma2 * (e_ui * 1/ sqrt(len(N_u)) * qi[i] - l_reg7 * yj[N_u])
        gamma1 *= 0.6
        gamma2 *= 0.6
        

        # if it % 10 == 0:
        #   print(it, "\ ", n_iter)         
        #   print("compute loss...")
        #   print(compute_loss(mat, mu, bu, bi, qi, pu, N_u, yj, l_reg6=l_reg6, l_reg7=l_reg7))
    return bu, bi, qi, pu, yj
#################################################


if __name__ == "__main__":
    mat_file = path+"/D.mat"
    mat_file1 = path+"/newD.mat"
    mat_file2 = path+"/referD.mat"
    mat = io.loadmat(mat_file)['X']
    # print(mat)
    # print(mat.shape)
    mat0 = mat[0:mat.shape[0]//640, 0:mat.shape[1]//4]
    # io.savemat(mat_file1, {'X' : mat0})
    # print(mat.shape)
    # # print(mat)
    # # print(len(mat.getnnz(1)>0))
    # # print(len(mat.getnnz(0)>0))
    mat = mat0[mat0.getnnz(1)>0][:, mat0.getnnz(0)>0]
    io.savemat(mat_file2, {'X' : mat})
    # print(mat)
    # print(mat.shape)
    # # print(mat.shape)
    # # # print(mat)
    cx_old = mat0.tocoo()
    target_count = 250
    old_count = 0
    for u,i,v in zip(cx_old.row, cx_old.col, cx_old.data):
        old_count+=1
        if old_count == target_count:
            print(u,i,v)
    print(old_count)
    cx = mat.tocoo()
    new_count = 0
    for u,i,v in zip(cx.row, cx.col, cx.data):
        new_count+=1
        if new_count == target_count:
            print(u,i,v)
    print(new_count)
    # # print(cx)
    # # print(cx.row)
    # # bu_index, bi_index = pre_processing(mat, mat_file)
    # # print(bu_index[0])
    # # print(bi_index[0])
    # # print(bi_index[1])
    # # print(cx.col)
    # # k = {}
    # # for i in cx.col:
    # #     k[i] = 0
    # # print(k)
    # ################################
    # path = "backup/svd/"
    # bu=np.load(path+"bu.npy")
    # bi=np.load(path+"bi.npy")
    # qi=np.load(path+"qi.npy")
    # pu=np.load(path+"pu.npy")
    # yj=np.load(path+"yj.npy")
    # # bu,bi,qi,pu,yj = svd_more_more(mat, mat_file)
    # # # print(bu)
    # # np.save(path+"bu.npy",bu)
    # # np.save(path+"bi.npy",bi)
    # # np.save(path+"qi.npy",qi)
    # # np.save(path+"pu.npy",pu)
    # # np.save(path+"yj.npy",yj)
    # #################################
    # # print(cx.col)
    # # for u,i,v in zip(cx.row, cx.col, cx.data):
    # #     if u == 15:
    # #         print(u,i,v)
    # u_id = 713
    # bu_index, bi_index = pre_processing(mat, mat_file)
    # # true_id = bu_index[u_id]
    # # print(len(bi_index))
    # # print(true_id)
    # mu = mat.data[:].mean()
    # N_u = bi_index[u_id]
    # print(N_u)
    # target = []
    # for i in list(set(cx.col)):
    #     r_ui_pred = predict_r_ui(mat, u_id, i, mu, bu, bi, qi, pu, N_u, yj)
    #     target.append((u_id,i,r_ui_pred[0]))
    # def takeThird(elem):
    #     return elem[2]
    # target.sort(key=takeThird,reverse=True)
    # print(target[0:100])
