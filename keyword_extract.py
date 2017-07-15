#-*- coding:utf-8 -*-

from multiprocessing import Pool
import jieba
import jieba.analyse
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')
jieba.load_userdict("E:\\pythonproj\\dic.txt")

def get_tags(doc):
    tags = jieba.analyse.extract_tags(doc, topK = 5, withWeight = False, allowPOS = ('Ng','n','nr','ns','nt','nz','s','un','j'))
    return doc + '\t' + ','.join(tags)


class TaskGenerator(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for line in open(self.path, 'r'):
            yield line.strip()

if __name__ == "__main__":
    start = time.time()
    p = Pool(8)
    f_in = "E:\\pythonproj\\titles.txt"
    tasks = TaskGenerator(f_in)
    results = p.map(get_tags, tasks)
    with open("E:\\pythonproj\\keywords.txt", 'w') as f_out:
        for line in results:
            f_out.write(line)
            f_out.write('\n')
    end = time.time()
    print end - start