from model.svd_more_more import *
"""
this script is for training a new SVD++ model
"""
# def rating_compiler2(tar_name, out_path,special_remove_movie):
#     #this is the dataset reader of netfilx dataset, pls replace it with ur own dataset format
#     #D = dok_matrix((total_no_users, total_no_movies), dtype=np.uint8)
#     D = lil_matrix((total_no_users, total_no_movies), dtype=np.uint8)
#     tar = tarfile.open(tar_name)
#     res_getmembers = tar.getmembers()
#     number = len(res_getmembers)
#     i = 0
#     for member in res_getmembers:
#         f = tar.extractfile(member)
#         if f is not None:    
#             if i % 100 == 0:
#                 print(i, " / ", number)        
#             content = f.read()
#             f.close()
#             D = process_content(content.decode(), D,special_remove_movie)
#         i += 1
#     tar.close()
#     D = csr_matrix(D, dtype=np.float64)
#     io.savemat(out_path, {'X' : D})

path = "ckpoint/mat"
mat_file = path+"/newD.mat"#read the data

mat = io.loadmat(mat_file)['X']
bu,bi,qi,pu,yj = svd_more_more(mat, mat_file)
# print(bu)
np.save(path+"bu.npy",bu)
np.save(path+"bi.npy",bi)
np.save(path+"qi.npy",qi)
np.save(path+"pu.npy",pu)
np.save(path+"yj.npy",yj)
