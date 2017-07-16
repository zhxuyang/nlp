#-*- coding:utf-8 -*-

from multiprocessing import Pool
import jieba
import sys
import time
from BaseUtil import LineGenerator

reload(sys)
sys.setdefaultencoding('utf8')
# jieba.load_userdict("E:\\pythonproj\\dic.txt")


def cut_sentence(doc):
    return ' '.join(jieba.cut(doc)) + '\n'


if __name__ == "__main__":
    start = time.time()
    p = Pool(8)
    f_in = "E:\\pythonproj\\news_tensite_xml_content.dat"
    tasks = LineGenerator(f_in)
    results = p.imap(cut_sentence, tasks, chunksize=100)
    with open("E:\\pythonproj\\content_words.dat", 'w') as f_out:
        for line in results:
            f_out.write(line)
    end = time.time()
    print end - start