# -*- encoding:utf-8 -*-
#from common import similarity
from scikits.crab import metrics
from ..util import constants

def get_recommendation_list(matrix1,matrix2,sim_const,top,threshold,keep_sim):
    recommendation_lists = []
    similarity_matrix = None
    if sim_const == constants.COS:
        similarity_matrix = metrics.cosine_distances(matrix1,matrix2) #similarity.cosine_similarity(matrix1,matrix2)
    elif sim_const == constants.EUCLIDEAN:
        similarity_matrix = metrics.euclidean_distances(matrix1,matrix2) #similarity_matrix = cosine_similarity(matrix1,matrix2)
    elif sim_const == constants.MANHATTAN:
        similarity_matrix = metrics.manhattan_distances(matrix1,matrix2)
    elif sim_const == constants.PEARSON:
        similarity_matrix = metrics.pearson_correlation(matrix1, matrix2)
    else:
        raise ValueError("`"+sim_const+"` is not a valid similarity algorithm code !")
    for i,sim_value_lst in enumerate(similarity_matrix):
        rating_map = {}
        rating_map[i] = {}
        for j,sim_value in enumerate(sim_value_lst):
            rating_map[i][j]=sim_value
        recommendation_list = get_init_recommendations(rating_map,top,threshold,keep_sim)
        recommendation_lists.append(recommendation_list)
    return recommendation_lists
def get_recommendation_list_old(matrix1,matrix2,sim_const,top,threshold,keep_sim):
    """
    form of the return:[(elementA,elementB,rating),(... ...)] 
    """
    recommendation_lists = []
    for i in xrange(len(matrix1)):
        rating_map = {}
        for j in xrange(len(matrix2)):
            sim = 0.0
            if sim_const == constants.COS:
                sim = similarity.cosine_similarity(matrix1[i], matrix2[j])
            elif sim_const == constants.EUCLIDEAN:
                pass
            elif sim_const == constants.MANHATTAN:
                pass
            elif sim_const == constants.PEARSON:
                sim = similarity.pearson_correlation_similarity(matrix1[i], matrix2[j])
            elif sim_const == constants.SPEARMAN:
                pass
            else:
                raise ValueError("`"+sim_const+"` is not a valid similarity algorithm code !")
            
            if i in rating_map:
                rating_map[i][j] = sim
            else:
                rating_map[i] = {}
                rating_map[i][j] = sim
            # if j in rating_map:
            #     rating_map[j][i] = sim
            # else:
            #     rating_map[j] = {}
            #     rating_map[j][i] = sim
        recommendation_list = get_init_recommendations(rating_map,top,threshold,keep_sim)

        recommendation_lists.append(recommendation_list)
    return recommendation_lists

def get_init_recommendations(rating_map,top,threshold,keep_sim):
    """
      
    """
    recommendation_lst = []
    #print rating_map
    for key,value in rating_map.items():
        if threshold:
            if keep_sim:
                recommendation_lst = [item for item in value.items() if item[1]>threshold]
            else:
                recommendation_lst = [item[0] for item in value.items() if item[1]>threshold]
        else:
            recommendation_lst = sorted(value.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)[0:top]
            if not keep_sim:
                recommendation_lst = [item[0] for item in recommendation_lst]
    return recommendation_lst

    
