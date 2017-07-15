#-*-coding:utf-8-*-

# from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def get_tag(fin, tag):
    fout = '%s_%s.dat' % (fin.split('.')[-2], tag)
    f = open(fout, 'w')
    length = len(tag) + 2
    for line in open(fin, 'r'):
        if line[:length] == '<' + tag + '>':
            line = line[length:-(length + 2)]
            f.write(line.decode('gbk', 'ignore').encode('utf8'))
            f.write('\n')
    f.close()


# def get_tag(fin, fout, tag):
#     f = open(fout, 'w')
#     for event, element in etree.iterparse(fin, tag="contenttitle", huge_tree=True):
#         f.write(element.text)
#         f.write('\n')
#         element.clear()
#
#     f.close()


if __name__ == "__main__":
    path = "E:\\pythonproj\\"
    fin = path + "news_tensite_xml.dat"
    tag = "contenttitle"
    get_tag(fin, tag)