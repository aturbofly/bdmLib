# -*- encoding:utf-8 -*-
import sys,json,time
from ..file import file_process
from ..common import tf_idf
from ..util import constants
from ..models.word import Word
import pubUtil

def TFIDFBasedRecs_old(message_lst,num_features=1000,sim=constants.COS,top = 10):
    """
      content(tf/idf)-based recommendation algorithm.

      Parameters
      ------------
       `message_lst` —— a list who's element is a post(aritle,etc)  
      `num_features`——length of the Feature vector 
      `sim`—— the similarity algorithm
      'top'——the length of the recommendation list
      `message`:a post that has not split.
      `comment`:the post that has split to word
    """
    comment_lst = []
    for message in message_lst:
        comment = file_process.split_comments(message)
        #print json.dumps(comment, encoding="UTF-8", ensure_ascii=False)
        comment_lst.append(comment)
    tf_idf_matrix = TFIDF_matrix(comment_lst,num_features)
   # print tf_idf_matrix
    #sys.exit(-1)
    rating_map = pubUtil.count_similarity_based_matrix(tf_idf_matrix,tf_idf_matrix,sim)
    recommendation_lsts = pubUtil.return_init_recommendations(rating_map,top)
    print rating_map
    print recommendation_lsts

def TFIDFBasedRecs(source_matrix,be_recommend_matrix=None,sim=constants.PEARSON,threshold = None,top = 10,keep_sim = False):
    """
     content(tf/idf)-based recommendation algorithm.

     Parameters
     ------------
     The only must argument is `source_matrix`—— contain all items should give recommendation
      `be_recommend_matrix`——  the items should be recommended
      `sim`——the similarity algorithm,the default is cosine similarity
      `threshold`——the similarity threshold，is not give by default.if give this argument,then choose recommend items that greater 
                                than this value, or give the top `top` items as recommendation list
      `top`——the length of the recommendation list that the items are choosed based the similarity
      `keep_sim`——need or not to keep the similarity value in the recommendation list
    Returns
    ---------
    Return many list of recommended items
    """
    if not be_recommend_matrix:be_recommend_matrix = source_matrix
    start1 = time.clock()
    recommendation_lsts = pubUtil.get_recommendation_list(source_matrix,be_recommend_matrix,sim,top,threshold,keep_sim)
    start2 = time.clock()
    print '获取推荐列表耗时: ',str(start2-start1)
    print recommendation_lsts
def TFIDF_matrix(message_lst,num_features=1000):
    """
     a matrix who's element is word‘s tf/idf.
     for example,if there are 500 posts,and the vector's length is 1000,
     then ,the matrix is a 500×1000
    """
    comment_lst = []
    stopwords = file_process.get_stopwords(sys.path[0]+'/file/stops.txt')
    start1 = time.clock()
    for message in message_lst:
        comment = file_process.split_comments(message,stopwords)
        #print json.dumps(comment, encoding="UTF-8", ensure_ascii=False)
        comment_lst.append(comment)
    start2 = time.clock()
    print '分词耗时: ',str(start2-start1)
    matrix = []
    #the number of posts
    num_docs = len(comment_lst)
    start1 = time.clock()
    top_words = file_process.find_topwords(comment_lst,num_features)
    start2 = time.clock()
    print '找特征词耗时: ',str(start2-start1)
    start1 = time.clock()
    for word in top_words:
        #print word.name,':',word.freq,':',word.doc_freq
        word.doc_freq = tf_idf.find_word_doc_freq(word.name,comment_lst)
    start2 = time.clock()
    print '计算词的doc freq耗时: ',str(start2-start1)
    print '开始求特征矩阵... ...'
    start1 = time.clock()
    for comment in comment_lst:
       vector = tf_idf.TFIDF_vector(comment,num_docs,top_words)
       matrix.append(vector)
    start2 = time.clock()
    print '得到tf/idf特征矩阵耗时: ',str(start2-start1)
    return matrix


            
        
