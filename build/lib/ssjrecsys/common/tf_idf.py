# -*- encoding:utf-8 -*-
import math
def TF(freq):
    """
      count term's frequency

      argument `freq` is term's frequency
    """
    return math.sqrt(freq)

def IDF(doc_freq,num_docs):
    """
     count Inverse Document Frequency.
     `doc_freq` is the number of documents in which the term appears.
     `num_docs` is the number of  all documents
    """
    log_value = float(num_docs)/(doc_freq+1)
    return 1+math.log(log_value)
    
def TFIDF_vector(comment,num_docs,keywords=[]):
    """
      count `comment`‘ s feature vector.
      the length of the vector is equal length of keywords
      and the element of the vector is the keyword’s tf-idf
    """
    vector = {}
    #if not provide keywords,then choose the comment as the keywords
    if not keywords:keywords = comment
    #print keywords
    for i,word in enumerate(keywords):
        word.freq = 0
        if word.name not in comment:
            #print i,'--',word.name
            vector[i] = 0.0
        else:
            for com_word in comment:
                if word.name == com_word:
                    word.freq +=1
            #print word.name,':',word.freq
            tf = TF(word.freq)
            #print word.doc_freq,':::',num_docs
            idf = IDF(word.doc_freq,num_docs)
            #print tf,':',idf
            vector[i] = tf*idf
    return vector.values()

def find_word_doc_freq(word,comment_lst):
    """
      count the number of documents in which the term `word` appears.
    """
    doc_freq = 0
    for comment in comment_lst:
        if word in comment:
            doc_freq+=1
    return doc_freq


 