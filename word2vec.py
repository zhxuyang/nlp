#-*- coding:utf-8 -*-

from gensim.models import Word2Vec
import sys
import time
from BaseUtil import WordsGenerator

reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == "__main__":
    start = time.time()
    f_in = "E:\\pythonproj\\content_words.dat"
    words = WordsGenerator(f_in)
    model = Word2Vec(words, min_count=5, size=200, workers=8)
    model.save('E:\\pythonproj\\word2vector.model')
    end = time.time()
    print end - start