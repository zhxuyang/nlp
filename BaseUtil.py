#-*-coding:utf-8-*-

class LineGenerator(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for line in open(self.path, 'r'):
            yield line.strip()


class WordsGenerator(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for line in open(self.path, 'r'):
            line = line.strip()
            if line:
                yield line.split(' ')