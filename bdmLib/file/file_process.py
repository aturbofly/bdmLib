# -*- encoding:utf-8 -*-
import jieba,sys
from ..models import word as Entry
import re
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
def split_comments(message,stopwords):
    """
     break up a post(chinese)  to words use the jieba
    """
    word_freq = {}
    words = jieba.cut(message)
    words = __cleanse_keywords(words,stopwords)
    return words

def __cleanse_keywords(keywords, stopwords):
    """
       filter invalid word
    """
    cleansed_words = []
    pat = re.compile(r'\d+')
    for keyword in keywords:
        if not keyword.strip():continue
        #print keyword
        if not (pat.match(keyword) or keyword in stopwords):
            cleansed_words.append(keyword)
    return cleansed_words
def get_stopwords(file):
    """

    """
    stopword_lst = []
    for line in open(file):
        stopword_lst.append(line.strip('\r\n').strip().decode('utf-8'))
    return stopword_lst

def find_topwords(comments,top):
    """
    find the top `top` words base on words'frequent 
    the return is a list who's element is a Word object
    """
    word_freq = {}
    for i in xrange(len(comments)):
        for word in comments[i]:
            #print word
            if word in word_freq:
                word_freq[word]+=1
            else:
                word_freq[word] = 1
    if len(word_freq)<top:top = len(word_freq)
    #print 'top:',top
    #print 'word_freq:',word_freq
    top_word_freq = sorted(word_freq.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)[0:top]
    return [Entry.Word(word[0]) for word in top_word_freq]
        


